import pytest
import bpy

def test_scene_structure():
    """Test scene has required collections"""
    bpy.ops.wm.read_homefile(use_empty=True)
    
    # Create collections
    bpy.data.collections.new("ASSETS")
    
    assert "ASSETS" in [c.name for c in bpy.data.collections]

def test_naming_convention():
    """Test object naming validation"""
    bpy.ops.wm.read_homefile(use_empty=True)
    
    # Add object
    bpy.ops.mesh.primitive_cube_add()
    cube = bpy.context.active_object
    cube.name = "CH_hero"
    
    # Test naming
    assert cube.name.startswith("CH_")
