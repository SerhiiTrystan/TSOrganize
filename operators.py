import bpy, os


FOLDER_STRUCTURE = {
    "Textures": ["", "", ""],
    "Models": ["", "", ""],
    "References": ["", ""],
    "Renders": ["", ""]
}

class PROJECT_OT_CREATEFOLDERS(bpy.types.Operator):
    bl_idname = ""
    bl_label = ""
    bl_description = ""
    bl_options = ""

    def execute(self, context):
        scene = context.scene

        if not scene.project_path or not scene.project_name:
            self.report({'ERROR'}, "Select the folder path")
            return {'CANCELLED'}

        project_folder = os.path.join(scene.project_path, scene.project_name)
        
        try:
            os.makedirs(project_folder, exist_ok=True)
        except Exception as e:
            self.report({'ERROR'}, f"Errors of creation: {e}")
            return {'CANCELLED'}

        folders = []
        if scene.create_textures:
            folders.append("Textures")
        if scene.create_models:
            folders.append("Models")
        if scene.create_references:
            folders.append("References")
        if scene.create_renders:
            folders.append("Renders")
        
        for folder in folders:
            folder_path = os.path.join(project_folder, folder)
            os.makedirs(folder_path, exist_ok=True)

            subfolders = FOLDER_STRUCTURE.get(folder, [])
            for subfolder in subfolders:
                subfolders_path = od.path.join(folder_path, subfolder)
                os.makedirs(subfolder_path, exist_ok=True)
        
        self.report({'INFO'}, f"Project created: {project_folder}")
        return {'FINISHED'}

