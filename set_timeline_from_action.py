bl_info = {
    "name": "Set Timeline Range from Action",
    "author": "Your Name",
    "version": (1, 0),
    "blender": (3, 6, 0),
    "location": "3D View > Sidebar > Animation Tab",
    "description": "Automatically sets the timeline range based on the selected Action's frame range.",
    "category": "Animation",
}

import bpy

def set_timeline_range_from_action(context):
    obj = context.object
    
    # ตรวจสอบว่ามีแอคชันที่เลือกในแทร็กหรือไม่
    if obj and obj.animation_data and obj.animation_data.action:
        action = obj.animation_data.action
        frame_start = int(action.frame_range[0])
        frame_end = int(action.frame_range[1])
        
        # ตั้งค่า Timeline Range
        context.scene.frame_start = frame_start
        context.scene.frame_end = frame_end
        
        self_report_message = f"Timeline set to Action: '{action.name}', Frames: {frame_start}-{frame_end}"
        print(self_report_message)
        return self_report_message
    else:
        self_report_message = "No Action selected on the active object."
        print(self_report_message)
        return self_report_message


class ANIM_OT_SetTimelineFromAction(bpy.types.Operator):
    """Set Timeline Range from Selected Action"""
    bl_idname = "anim.set_timeline_from_action"
    bl_label = "Set Timeline from Action"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        message = set_timeline_range_from_action(context)
        self.report({'INFO'}, message)
        return {'FINISHED'}


class ANIM_PT_SetTimelinePanel(bpy.types.Panel):
    """Panel to Trigger Timeline Range Update"""
    bl_label = "Set Timeline from Action"
    bl_idname = "ANIM_PT_set_timeline_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Animation'
    
    def draw(self, context):
        layout = self.layout
        layout.label(text="Set Timeline Range:")
        layout.operator(ANIM_OT_SetTimelineFromAction.bl_idname)


def register():
    bpy.utils.register_class(ANIM_OT_SetTimelineFromAction)
    bpy.utils.register_class(ANIM_PT_SetTimelinePanel)


def unregister():
    bpy.utils.unregister_class(ANIM_OT_SetTimelineFromAction)
    bpy.utils.unregister_class(ANIM_PT_SetTimelinePanel)


if __name__ == "__main__":
    register()
