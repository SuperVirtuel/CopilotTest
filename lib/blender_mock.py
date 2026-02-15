"""Very small mock of the parts of Blender's bpy API used by tests."""

class MeshOps:
    def __init__(self):
        self.primitive_cube_added = False
        self.last_location = None

    def primitive_cube_add(self, location=(0, 0, 0)):
        self.primitive_cube_added = True
        self.last_location = tuple(location)


class WMOps:
    def __init__(self):
        self.last_saved = None

    def save_mainfile(self, filepath=None):
        # record the path that would have been saved
        self.last_saved = filepath


class Ops:
    def __init__(self):
        self.mesh = MeshOps()
        self.wm = WMOps()


# top-level objects to mimic bpy
ops = Ops()

# convenience aliases (some scripts import bpy.ops directly)
class _BpyModule:
    pass

bpy = _BpyModule()
setattr(bpy, "ops", ops)

# expose expected names for 'import bpy'
# When tests inject this module into sys.modules as 'bpy', code doing 'import bpy' will receive this object.
