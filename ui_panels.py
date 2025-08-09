import bpy

class PROJECT_PT_MainPanel(bpy.types.Panel):
    bl_label = "Project Folder Creator"
    bl_idname = "PROJECT_PT_main_panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Project Tools"

    def draw (self, context):
        layout = self.layout
        scene = context.scene

        layout.prop(scene, "project_path")
        layout.prop(scene, "project_name")

        layout.label(text="Choose folder")
        layout.prop(scene, "create_textures")
        layout.prop(scene, "create_models")
        layout.prop(scene, "create_references")
        layout.prop(scene, "create_renders")

        layout.operator("project.create_folders", icon="FILE_FOLDED")

        
    