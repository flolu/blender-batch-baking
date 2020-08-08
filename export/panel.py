import bpy


class ExportPanel(bpy.types.Panel):
    bl_label = 'Batch Export'
    bl_idname = 'MAIN_PT_batch_exporter'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Export'

    def draw(self, context):
        layout = self.layout

        row = layout.column()
        row.prop(context.scene, 'export_out_path', text='Output')

        box = layout.box()
        col = box.column(align=True)
        row = col.row(align=True)
        row.prop(context.scene, "export_type_obj", icon="BLANK1", text="obj")
        row.prop(context.scene, "export_type_fbx", icon="BLANK1", text="fbx")
        # TODO more types
        # row.prop(context.scene, "export_type_glb", icon="BLANK1", text="glb")
        # row.prop(context.scene, "export_type_gltf", icon="BLANK1", text="gltf")
        # row.prop(context.scene, "export_type_dae", icon="BLANK1", text="dae")
        row = col.row(align=True)

        row = layout.row()
        row.operator('batch_export.export', text='Export')