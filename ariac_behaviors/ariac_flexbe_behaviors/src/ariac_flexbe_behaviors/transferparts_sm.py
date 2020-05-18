#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from ariac_flexbe_states.srdf_state_to_moveit_ariac_state import SrdfStateToMoveitAriac
from ariac_flexbe_states.detect_part_camera_ariac_state import DetectPartCameraAriacState
from ariac_flexbe_states.compute_grasp_ariac_state import ComputeGraspAriacState
from ariac_flexbe_states.offset_calc import part_offsetCalc
from ariac_flexbe_states.moveit_to_joints_dyn_ariac_state import MoveitToJointsDynAriacState
from ariac_flexbe_states.gripper_control import GripperControl
from ariac_support_flexbe_states.equal_state import EqualState
from ariac_support_flexbe_states.replace_state import ReplaceState
from ariac_flexbe_states.choose_arm_id import chooseArmID
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Thu May 14 2020
@author: Patrick Verwimp
'''
class TransferPartsSM(Behavior):
	'''
	Moves parts to transferbin
	'''


	def __init__(self):
		super(TransferPartsSM, self).__init__()
		self.name = 'TransferParts'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:811 y:574, x:283 y:395
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'], input_keys=['move_group_prefix', 'part_type', 'bin', 'camera_topic', 'camera_frame', 'agv_id', 'ref_frame'])
		_state_machine.userdata.agv_id = []
		_state_machine.userdata.part_type = []
		_state_machine.userdata.move_group = 'manipulator'
		_state_machine.userdata.move_group_prefix = []
		_state_machine.userdata.action_topic = '/move_group'
		_state_machine.userdata.robot_name = ''
		_state_machine.userdata.bin = []
		_state_machine.userdata.camera_topic = []
		_state_machine.userdata.camera_frame = []
		_state_machine.userdata.ref_frame = []
		_state_machine.userdata.tool_link = 'ee_link'
		_state_machine.userdata.arm_id = ''
		_state_machine.userdata.config_name_home = 'home'
		_state_machine.userdata.pose = []
		_state_machine.userdata.part_offset = 0.08
		_state_machine.userdata.rotation = 0
		_state_machine.userdata.agv1 = 'agv1'
		_state_machine.userdata.bin3 = 'transferBin3'
		_state_machine.userdata.bin4 = 'transferBin4'
		_state_machine.userdata.joint_values = []
		_state_machine.userdata.joint_names = []

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:30 y:40
			OperatableStateMachine.add('MoveToHome',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'ArmId', 'planning_failed': 'failed', 'control_failed': 'failed', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_home', 'move_group': 'move_group', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:306 y:28
			OperatableStateMachine.add('MoveToBin',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'DetectPartPose', 'planning_failed': 'failed', 'control_failed': 'failed', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'bin', 'move_group': 'move_group', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:453 y:26
			OperatableStateMachine.add('DetectPartPose',
										DetectPartCameraAriacState(time_out=0.5),
										transitions={'continue': 'ComputeGrasp', 'failed': 'failed', 'not_found': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'ref_frame': 'ref_frame', 'camera_topic': 'camera_topic', 'camera_frame': 'camera_frame', 'part': 'part_type', 'pose': 'pose'})

			# x:659 y:29
			OperatableStateMachine.add('ComputeGrasp',
										ComputeGraspAriacState(joint_names=['linear_arm_actuator_joint', 'shoulder_pan_joint', 'shoulder_lift_joint', 'elbow_joint', 'wrist_1_joint', 'wrist_2_joint', 'wrist_3_joint']),
										transitions={'continue': 'MoveToPart', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'move_group': 'move_group', 'move_group_prefix': 'move_group_prefix', 'tool_link': 'tool_link', 'pose': 'pose', 'offset': 'part_offset', 'rotation': 'rotation', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:177 y:27
			OperatableStateMachine.add('PartOffset',
										part_offsetCalc(),
										transitions={'succes': 'MoveToBin', 'unknown_id': 'failed'},
										autonomy={'succes': Autonomy.Off, 'unknown_id': Autonomy.Off},
										remapping={'part_type': 'part_type', 'part_offset': 'part_offset'})

			# x:825 y:30
			OperatableStateMachine.add('MoveToPart',
										MoveitToJointsDynAriacState(),
										transitions={'reached': 'EnableGripper', 'planning_failed': 'failed', 'control_failed': 'EnableGripper'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'move_group_prefix': 'move_group_prefix', 'move_group': 'move_group', 'action_topic': 'action_topic', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1033 y:60
			OperatableStateMachine.add('EnableGripper',
										GripperControl(enable=True),
										transitions={'continue': 'agv1?', 'failed': 'MoveToPart', 'invalid_id': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'invalid_id': Autonomy.Off},
										remapping={'arm_id': 'arm_id'})

			# x:1012 y:345
			OperatableStateMachine.add('MoveToTransferBin',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'DisableGripper', 'planning_failed': 'failed', 'control_failed': 'failed', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'bin', 'move_group': 'move_group', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1018 y:130
			OperatableStateMachine.add('agv1?',
										EqualState(),
										transitions={'true': 'bin4', 'false': 'bin3'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'agv1', 'value_b': 'agv_id'})

			# x:880 y:207
			OperatableStateMachine.add('bin3',
										ReplaceState(),
										transitions={'done': 'MoveToHome_3'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'bin3', 'result': 'bin'})

			# x:880 y:273
			OperatableStateMachine.add('bin4',
										ReplaceState(),
										transitions={'done': 'MoveToHome_3'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'bin4', 'result': 'bin'})

			# x:1034 y:438
			OperatableStateMachine.add('DisableGripper',
										GripperControl(enable=False),
										transitions={'continue': 'MoveToHome_2', 'failed': 'failed', 'invalid_id': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'invalid_id': Autonomy.Off},
										remapping={'arm_id': 'arm_id'})

			# x:942 y:514
			OperatableStateMachine.add('MoveToHome_2',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'finished', 'planning_failed': 'failed', 'control_failed': 'failed', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_home', 'move_group': 'move_group', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1074 y:235
			OperatableStateMachine.add('MoveToHome_3',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'MoveToTransferBin', 'planning_failed': 'failed', 'control_failed': 'MoveToHome_3', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_home', 'move_group': 'move_group', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:30 y:102
			OperatableStateMachine.add('ArmId',
										chooseArmID(),
										transitions={'continue': 'PartOffset', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'move_group_prefix': 'move_group_prefix', 'arm_id': 'arm_id'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
