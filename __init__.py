bl_info = {
    "name": "Organozation Folder Addons",
    "author": "Chat and Trystan Serhii",
    "version": (0, 1),
    "blender": (4, 5, 0),
    "lacotion": "View3D > N-Panel",
    "description": "Create the folder stucrure",
    "catagory": "System"
}

import bpy
from . import ui_panels, operators

classes = (
    ui_panels.PROJECT_PT_MainPanel,
    operators.PROJECT_OT_CreateFolders,
)

def register():
    for clc in classes:
        bpy.utils.register_class(cls)

    bpy.types.Scene.project_path = bpy.props.StringProperty(
        name="Path",
        subtype="DIR_PATH",
        default=""
    )
    bpy.types.Scene.project_name = bpy.props.StringProperty(
        name="Name of folder",
        default=""
    )
    bpy.types.Scene.create_textures = bpy.props.BoolProperty(name="", default=True)
    bpy.types.Scene.create_models = bpy.props.BoolProperty(name="", default=True)
    bpy.types.Scene.create_references = bpy.props.BoolProperty(name="", default=True)
    bpy.types.Scene.create_renders = bpy.props.BoolProperty(name="", default=True)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

    del bpy.types.Scene.project_path
    del bpy.types.Scene.project_name
    del bpy.types.Scene.create_textures
    del bpy.types.Scene.create_models
    del bpy.types.Scene.create_references
    del bpy.types.Scene.create_renders   