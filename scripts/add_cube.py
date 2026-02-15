"""Script that adds a cube to a Blender scene and saves the file. Designed to work with a small bpy mock for unit tests."""

try:
    import bpy
except Exception:
    # When running outside Blender, expect tests to inject a mock 'bpy' module
    import sys
    bpy = sys.modules.get('bpy')
    if bpy is None:
        raise ImportError(
            "bpy module not available; when running outside Blender, "
            "inject a mock 'bpy' into sys.modules before importing this script."
        )


def add_cube_and_save(filepath: str = 'scene.blend', location=(0, 0, 0)) -> None:
    """Add a cube to the scene and save to filepath.

    This uses bpy.ops.mesh.primitive_cube_add and bpy.ops.wm.save_mainfile.
    In tests, a lightweight mock of bpy is provided.
    """
    bpy.ops.mesh.primitive_cube_add(location=location)
    bpy.ops.wm.save_mainfile(filepath=filepath)


if __name__ == '__main__':
    add_cube_and_save('scene.blend', (0, 0, 0))