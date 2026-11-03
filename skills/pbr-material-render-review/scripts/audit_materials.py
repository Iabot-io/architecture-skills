"""Read-only Blender material preflight. Run with blender -b file --python ... -- ..."""
import argparse
import json
import sys
from pathlib import Path


def upstream(node, visited=None):
    visited = set() if visited is None else visited
    if node in visited:
        return visited
    visited.add(node)
    for socket in node.inputs:
        for link in socket.links:
            if link.is_valid and not link.is_muted:
                upstream(link.from_node, visited)
    return visited


def socket_sources(socket):
    result = set()
    for link in socket.links:
        if link.is_valid and not link.is_muted:
            result.update(upstream(link.from_node))
    return result


def active_uv(mesh):
    layer = next((u for u in mesh.uv_layers if u.active_render), None)
    return layer.name if layer else ""


def audit_scene(bpy, required):
    scene = bpy.context.scene
    issues = []
    materials = []
    assigned = {}
    def issue(code, material, detail):
        issues.append({"code": code, "material": material, "detail": detail})
    for obj in scene.objects:
        if obj.type != "MESH" or obj.hide_render:
            continue
        used = {face.material_index for face in obj.data.polygons}
        for index in used:
            if index < len(obj.material_slots) and obj.material_slots[index].material:
                material = obj.material_slots[index].material
                assigned.setdefault(material.name, []).append(obj)
    for name in required:
        if name not in assigned:
            issue("REQUIRED_MATERIAL_NOT_ASSIGNED", name, "No visible mesh faces use this material")
    for layer in scene.view_layers:
        if layer.use and layer.material_override and required:
            issue("VIEW_LAYER_MATERIAL_OVERRIDE", layer.material_override.name, layer.name)
    for name, objects in sorted(assigned.items()):
        material = bpy.data.materials[name]
        entry = {"name": name, "objects": [o.name for o in objects], "images": [], "normal_maps": []}
        materials.append(entry)
        if not material.use_nodes:
            if name in required:
                issue("REQUIRED_MATERIAL_HAS_NO_NODES", name, "Material nodes disabled")
            continue
        outputs = [n for n in material.node_tree.nodes if n.type == "OUTPUT_MATERIAL"
                   and n.is_active_output and n.target in ("ALL", "CYCLES")]
        nodes = set()
        for output in outputs:
            nodes.update(socket_sources(output.inputs["Surface"]))
        images = [n for n in nodes if n.type == "TEX_IMAGE" and not n.mute]
        if name in required and not images:
            issue("NODE_GROUP_REQUIRES_INSPECTION" if any(n.type == "GROUP" for n in nodes) else "NO_CONNECTED_IMAGE_TEXTURE", name, "No directly inspectable image reaches the active surface output")
        for node in images:
            image = node.image
            if image is None:
                issue("IMAGE_NODE_EMPTY", name, node.name)
                continue
            packed = bool(image.packed_file or len(image.packed_files))
            entry["images"].append({"node": node.name, "image": image.name,
                                    "size": list(image.size), "packed": packed,
                                    "projection": node.projection,
                                    "color_space": image.colorspace_settings.name})
            if not all(image.size):
                issue("IMAGE_WITHOUT_PIXELS", name, image.name)
            if image.source == "FILE" and not packed:
                issue("IMAGE_NOT_PACKED", name, image.name)
        for normal in (n for n in nodes if n.type == "NORMAL_MAP" and not n.mute):
            normal_images = [n for n in socket_sources(normal.inputs["Color"]) if n.type == "TEX_IMAGE"]
            entry["normal_maps"].append({"node": normal.name, "space": normal.space,
                                         "uv_map": normal.uv_map})
            for image_node in normal_images:
                image = image_node.image
                if image and image.colorspace_settings.name not in ("Non-Color", "Raw"):
                    issue("NORMAL_IMAGE_COLOR_SPACE", name, image.name)
                if normal.space != "TANGENT":
                    continue
                coords = socket_sources(image_node.inputs["Vector"])
                non_uv = any(n.type == "TEX_COORD" and any(
                    link.to_node in coords | {image_node} and link.from_socket.name != "UV"
                    for output_socket in n.outputs for link in output_socket.links) for n in coords)
                explicit_uv = [n.uv_map for n in coords if n.type == "UVMAP" and n.uv_map]
                if image_node.projection != "FLAT" or non_uv:
                    issue("TANGENT_NORMAL_PROJECTION_MISMATCH", name, image_node.name)
                for obj in objects:
                    normal_uv = normal.uv_map or active_uv(obj.data)
                    texture_uv = explicit_uv[0] if explicit_uv else active_uv(obj.data)
                    available = {u.name for u in obj.data.uv_layers}
                    if not normal_uv or normal_uv not in available or texture_uv not in available:
                        issue("NORMAL_UV_MISSING", name, obj.name)
                    elif normal_uv != texture_uv:
                        issue("NORMAL_UV_MISMATCH", name, obj.name + ": " + texture_uv + " / " + normal_uv)
    return {"file": bpy.data.filepath, "scene": scene.name, "engine": scene.render.engine,
            "materials": materials, "issues": issues, "structural_ok": not issues,
            "visual_review_required": True,
            "limitation": "Checks connectivity and portability, not appearance, physical scale or photographic quality"}


def main():
    import bpy
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", required=True)
    parser.add_argument("--require-texture", action="append", default=[])
    args = parser.parse_args(sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else [])
    report = audit_scene(bpy, set(args.require_texture))
    Path(args.out).write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"report": args.out, "structural_ok": report["structural_ok"],
                      "issues": report["issues"], "visual_review_required": True}, ensure_ascii=False))
    if report["issues"]:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
