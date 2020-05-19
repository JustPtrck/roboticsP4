#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from ariac_flexbe_states.offset_calc import part_offsetCalc
from ariac_flexbe_states.srdf_state_to_moveit_ariac_state import SrdfStateToMoveitAriac
from ariac_flexbe_states.compute_grasp_ariac_state import ComputeGraspAriacState
from ariac_flexbe_states.gripper_control import GripperControl
from ariac_flexbe_states.detect_part_camera_ariac_state import DetectPartCameraAriacState
from ariac_flexbe_states.moveit_to_joints_dyn_ariac_state import MoveitToJointsDynAriacState
from ariac_flexbe_states.get_object_pose import GetObjectPoseState
from ariac_flexbe_states.ComputeDropPartOffsetGraspAriacState import ComputeDropPartOffsetGraspAriacState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Wed Apr 22 2020
@author: Gerard Harkema
'''
class transport_part_from_bin_to_agv_2SM(Behavior):
	'''
	Transports a order part from a bin to its desired agv
	'''


	def __init__(self):
		super(transport_part_from_bin_to_agv_2SM, self).__init__()
		self.name = 'transport_part_from_bin_to_agv_2'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:620 y:659, x:597 y:393
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'], input_keys=['bin', 'move_group_prefix', 'camera_topic', 'camera_frame', 'ref_frame', 'agv_id', 'part_type', 'part_pose'])
		_state_machine.userdata.config_name_home = 'home'
		_state_machine.userdata.move_group_prefix = []
		_state_machine.userdata.move_group = 'manipulator'
		_state_machine.userdata.action_topic = '/move_group'
		_state_machine.userdata.robot_name = ''
		_state_machine.userdata.agv_id = []
		_state_machine.userdata.joint_values = []
		_state_machine.userdata.joint_names = []
		_state_machine.userdata.bin = []
		_state_machine.userdata.part_type = ''
		_state_machine.userdata.config_name_tray = 'tray1PreDrop'
		_state_machine.userdata.pose = []
		_state_machine.userdata.part_offset = 0.08
		_state_machine.userdata.part_rotation = 0
		_state_machine.userdata.tool_link = 'ee_link'
		_state_machine.userdata.arm_id = 'arm2'
		_state_machine.userdata.camera_topic = []
		_state_machine.userdata.camera_frame = []
		_state_machine.userdata.ref_frame = []
		_state_machine.userdata.part_pose = []
		_state_machine.userdata.agv_pose = []

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:93 y:87
			OperatableStateMachine.add('OffsetCalc',
										part_offsetCalc(),
										transitions={'succes': 'MoveToHome', 'unknown_id': 'failed'},
										autonomy={'succes': Autonomy.Off, 'unknown_id': Autonomy.Off},
										remapping={'part_type': 'part_type', 'part_offset': 'part_offset'})

			# x:247 y:61
			OperatableStateMachine.add('MoveToHome',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'DetectPartPose', 'planning_failed': 'failed', 'control_failed': 'failed', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_home', 'move_group': 'move_group', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:648 y:61
			OperatableStateMachine.add('MoveBin',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'ComputeGrasp', 'planning_failed': 'failed', 'control_failed': 'failed', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'bin', 'move_group': 'move_group', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1123 y:281
			OperatableStateMachine.add('MoveToTray',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'GetAgvPose', 'planning_failed': 'failed', 'control_failed': 'failed', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_tray', 'move_group': 'move_group', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:808 y:60
			OperatableStateMachine.add('ComputeGrasp',
										ComputeGraspAriacState(joint_names=['linear_arm_actuator_joint', 'shoulder_pan_joint', 'shoulder_lift_joint', 'elbow_joint', 'wrist_1_joint', 'wrist_2_joint', 'wrist_3_joint']),
										transitions={'continue': 'MoveToPart', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'move_group': 'move_group', 'move_group_prefix': 'move_group_prefix', 'tool_link': 'tool_link', 'pose': 'pose', 'offset': 'part_offset', 'rotation': 'part_rotation', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1061 y:134
			OperatableStateMachine.add('GripperEnabled',
										GripperControl(enable=True),
										transitions={'continue': 'MoveToHome_2', 'failed': 'MoveToPart', 'invalid_id': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'invalid_id': Autonomy.Off},
										remapping={'arm_id': 'arm_id'})

			# x:423 y:55
			OperatableStateMachine.add('DetectPartPose',
										DetectPartCameraAriacState(time_out=.5),
										transitions={'continue': 'MoveBin', 'failed': 'failed', 'not_found': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'ref_frame': 'ref_frame', 'camera_topic': 'camera_topic', 'camera_frame': 'camera_frame', 'part': 'part_type', 'pose': 'pose'})

			# x:982 y:61
			OperatableStateMachine.add('MoveToPart',
										MoveitToJointsDynAriacState(),
										transitions={'reached': 'GripperEnabled', 'planning_failed': 'failed', 'control_failed': 'GripperEnabled'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'move_group_prefix': 'move_group_prefix', 'move_group': 'move_group', 'action_topic': 'action_topic', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1126 y:214
			OperatableStateMachine.add('MoveToHome_2',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'MoveToTray', 'planning_failed': 'failed', 'control_failed': 'MoveToHome_2', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_home', 'move_group': 'move_group', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1023 y:566
			OperatableStateMachine.add('GripperDisabled',
										GripperControl(enable=False),
										transitions={'continue': 'MoveToHome_3', 'failed': 'failed', 'invalid_id': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'invalid_id': Autonomy.Off},
										remapping={'arm_id': 'arm_id'})

			# x:932 y:632
			OperatableStateMachine.add('MoveToHome_3',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'finished', 'planning_failed': 'failed', 'control_failed': 'MoveToHome_3', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_home', 'move_group': 'move_group', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1112 y:356
			OperatableStateMachine.add('GetAgvPose',
										GetObjectPoseState(object_frame='kit_tray_2', ref_frame='arm2_linear_arm_actuator'),
										transitions={'continue': 'ComputeDrop', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'pose': 'agv_pose'})

			# x:1042 y:497
			OperatableStateMachine.add('MoveR1ToDrop',
										MoveitToJointsDynAriacState(),
										transitions={'reached': 'GripperDisabled', 'planning_failed': 'failed', 'control_failed': 'MoveR1ToDrop'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'move_group_prefix': 'move_group_prefix', 'move_group': 'move_group', 'action_topic': 'action_topic', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1007 y:426
			OperatableStateMachine.add('ComputeDrop',
										ComputeDropPartOffsetGraspAriacState(joint_names=['linear_arm_actuator_joint', 'shoulder_pan_joint', 'shoulder_lift_joint', 'elbow_joint', 'wrist_1_joint', 'wrist_2_joint', 'wrist_3_joint']),
										transitions={'continue': 'MoveR1ToDrop', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'move_group': 'move_group', 'move_group_prefix': 'move_group_prefix', 'tool_link': 'tool_link', 'part_pose': 'part_pose', 'pose': 'agv_pose', 'offset': 'part_offset', 'rotation': 'part_rotation', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
