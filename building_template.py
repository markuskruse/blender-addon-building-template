bl_info = {
    "name": "Building template",
    "blender": (2, 80, 0),
    "category": "Object",
}

import bpy


class BuildingTemplate(bpy.types.Operator):
    """Create a rect building template in 3D printing scale"""      # Use this as a tooltip for menu items and buttons.
    bl_idname = "object.building_template"        # Unique identifier for buttons and menu items to reference.
    bl_label = "Building template"         # Display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}  # Enable undo for the operator.

    width: bpy.props.IntProperty(name="Width", default=100, min=30, max=300)
    length: bpy.props.IntProperty(name="Length", default=80, min=30, max=300)
    height: bpy.props.IntProperty(name="Height", default=50, min=10, max=200)

    def execute(self, context):        # execute() is called when running the operator.

        # The original script
        scene = context.scene
        # create a new object, make the correct dimensions
        bpy.ops.mesh.primitive_cube_add(size=1, location=scene.cursor.location)
        bpy.ops.object.editmode_toggle()
        bpy.ops.transform.resize(value=(self.length, self.width, self.height))
        bpy.ops.transform.translate(value=(0, 0, self.height/2))
        bpy.ops.object.editmode_toggle()

        return {'FINISHED'}            # Lets Blender know the operator finished successfully.

def menu_func(self, context):
    self.layout.operator(BuildingTemplate.bl_idname)

def register():
    bpy.utils.register_class(BuildingTemplate)
    bpy.types.VIEW3D_MT_add.append(menu_func) 

def unregister():
    bpy.utils.unregister_class(BuildingTemplate)


# This allows you to run the script directly from Blender's Text editor
# to test the add-on without having to install it.
if __name__ == "__main__":
    register()
