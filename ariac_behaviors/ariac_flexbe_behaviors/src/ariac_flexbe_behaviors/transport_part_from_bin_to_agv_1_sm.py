#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from ariac_flexbe_states.start_assignment_state import StartAssignment
from ariac_flexbe_states.end_assignment_state import EndAssignment
from ariac_flexbe_behaviors.transport_part_form_bin_to_agv_state_sm import transport_part_form_bin_to_agv_stateSM
from ariac_flexbe_states.srdf_state_to_moveit_ariac_state import SrdfStateToMoveitAriac
from ariac_flexbe_states.compute_grasp_ariac_state import ComputeGraspAriacState
from ariac_flexbe_states.gripper_control import GripperControl
from ariac_flexbe_states.detect_part_camera_ariac_state import DetectPartCameraAriacState
from ariac_flexbe_states.moveit_to_joints_dyn_ariac_state import MoveitToJointsDynAriacState
from ariac_flexbe_states.offset_calc import part_offsetCalc
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Wed Apr 22 2020
@author: Gerard Harkema
'''
class transport_part_from_bin_to_agv_1SM(Behavior):
	'''
	Transorts a part vorm it's bin to the selecte agv
	'''


	def __init__(self):
		super(transport_part_from_bin_to_agv_1SM, self).__init__()
		self.name = 'transport_part_from_bin_to_agv_1'

		# parameters of this behavior

		# references to used behaviors
		self.add_behavior(transport_part_form_bin_to_agv_stateSM, 'transport_part_form_bin_to_agv_state')

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:1241 y:669, x:517 y:426
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'], input_keys=['bin', 'move_group_prefix', 'camera_topic', 'camera_frame', 'ref_frame', 'agv_id', 'part_type'])
		_state_machine.userdata.agv_id = []
		_state_machine.userdata.part_type = []
		_state_machine.userdata.pose_on_agv = []
		_state_machine.userdata.config_name_home = 'home'
		_state_machine.userdata.move_group = 'manipulator'
		_state_machine.userdata.move_group_prefix = []
		_state_machine.userdata.action_topic = '/move_group'
		_state_machine.userdata.robot_name = ''
		_state_machine.userdata.joint_values = []
		_state_machine.userdata.joint_names = []
		_state_machine.userdata.config_name_bin = bin
		_state_machine.userdata.config_name_tray2PreDrop = 'tray2PreDrop'
		_state_machine.userdata.pose = []
		_state_machine.userdata.part_offset = 0.080
		_state_machine.userdata.part_rotation = 0
		_state_machine.userdata.tool_link = 'ee_link'
		_state_machine.userdata.arm_id = 'arm1'
		_state_machine.userdata.camera_topic = []
		_state_machine.userdata.camera_frame = []
		_state_machine.userdata.ref_frame = []
		_state_machine.userdata.config_name_safety = 'safety'
		_state_machine.userdata.bin = []

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:52 y:43
			OperatableStateMachine.add('StartAssignment',
										StartAssignment(),
										transitions={'continue': 'OffsetCalc'},
										autonomy={'continue': Autonomy.Off})

			# x:1050 y:651
			OperatableStateMachine.add('EndAssignment',
										EndAssignment(),
										transitions={'continue': 'finished'},
										autonomy={'continue': Autonomy.Off})

			# x:826 y:576
			OperatableStateMachine.add('transport_part_form_bin_to_agv_state',
										self.use_behavior(transport_part_form_bin_to_agv_stateSM, 'transport_part_form_bin_to_agv_state'),
										transitions={'finished': 'EndAssignment', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit},
										remapping={'part_type': 'part_type', 'agv_id': 'agv_id', 'pose_on_agv': 'pose_on_agv'})

			# x:205 y:45
			OperatableStateMachine.add('MoveR1Home',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'DetectPartPose', 'planning_failed': 'failed', 'control_failed': 'failed', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_home', 'move_group': 'move_group', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:657 y:31
			OperatableStateMachine.add('MoveBin5PreGrasp',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'ComputeGraspRobot1', 'planning_failed': 'failed', 'control_failed': 'ComputeGraspRobot1', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'bin', 'move_group': 'move_group', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1081 y:402
			OperatableStateMachine.add('MoveTray2PreDrop',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'GripperDisabled', 'planning_failed': 'failed', 'control_failed': 'failed', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_tray2PreDrop', 'move_group': 'move_group', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:805 y:73
			OperatableStateMachine.add('ComputeGraspRobot1',
										ComputeGraspAriacState(joint_names=['linear_arm_actuator_joint', 'shoulder_pan_joint', 'shoulder_lift_joint', 'elbow_joint', 'wrist_1_joint', 'wrist_2_joint', 'wrist_3_joint']),
										transitions={'continue': 'MoveR1Bin5Pick', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'move_group': 'move_group', 'move_group_prefix': 'move_group_prefix', 'tool_link': 'tool_link', 'pose': 'pose', 'offset': 'part_offset', 'rotation': 'part_rotation', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1043 y:214
			OperatableStateMachine.add('GripperEnabled',
										GripperControl(enable=True),
										transitions={'continue': 'MoveR1SafePos', 'failed': 'failed', 'invalid_id': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'invalid_id': Autonomy.Off},
										remapping={'arm_id': 'arm_id'})

			# x:425 y:30
			OperatableStateMachine.add('DetectPartPose',
										DetectPartCameraAriacState(time_out=.5),
										transitions={'continue': 'MoveBin5PreGrasp', 'failed': 'failed', 'not_found': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'ref_frame': 'ref_frame', 'camera_topic': 'camera_topic', 'camera_frame': 'camera_frame', 'part': 'part_type', 'pose': 'pose'})

			# x:924 y:141
			OperatableStateMachine.add('MoveR1Bin5Pick',
										MoveitToJointsDynAriacState(),
										transitions={'reached': 'GripperEnabled', 'planning_failed': 'failed', 'control_failed': 'GripperEnabled'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'move_group_prefix': 'move_group_prefix', 'move_group': 'move_group', 'action_topic': 'action_topic', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1065 y:294
			OperatableStateMachine.add('MoveR1SafePos',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'MoveTray2PreDrop', 'planning_failed': 'failed', 'control_failed': 'failed', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_safety', 'move_group': 'move_group', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:111 y:130
			OperatableStateMachine.add('OffsetCalc',
										part_offsetCalc(),
										transitions={'succes': 'MoveR1Home', 'unknown_id': 'failed'},
										autonomy={'succes': Autonomy.Off, 'unknown_id': Autonomy.Off},
										remapping={'part_type': 'part_type', 'part_offset': 'part_offset'})

			# x:936 y:464
			OperatableStateMachine.add('GripperDisabled',
										GripperControl(enable=False),
										transitions={'continue': 'transport_part_form_bin_to_agv_state', 'failed': 'failed', 'invalid_id': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'invalid_id': Autonomy.Off},
										remapping={'arm_id': 'arm_id'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
