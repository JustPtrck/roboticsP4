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
from ariac_flexbe_states.srdf_state_to_moveit_ariac_state import SrdfStateToMoveitAriac
from ariac_flexbe_states.set_conveyorbelt_power_state import SetConveyorbeltPowerState
from ariac_flexbe_states.detect_part_camera_ariac_state import DetectPartCameraAriacState
from flexbe_states.wait_state import WaitState
from ariac_flexbe_states.moveit_to_joints_dyn_ariac_state import MoveitToJointsDynAriacState
from ariac_flexbe_states.gripper_control import GripperControl
from ariac_flexbe_states.compute_grasp_ariac_state import ComputeGraspAriacState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Thu Apr 23 2020
@author: Gerard Harkema
'''
class transport_part_from_belt_to_bin_stateSM(Behavior):
	'''
	Transports a part from pelt to a its own bin.
	'''


	def __init__(self):
		super(transport_part_from_belt_to_bin_stateSM, self).__init__()
		self.name = 'transport_part_from_belt_to_bin_state'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:448 y:497, x:101 y:396
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])
		_state_machine.userdata.arm_id = ''
		_state_machine.userdata.power_on = 80
		_state_machine.userdata.power_off = 0
		_state_machine.userdata.config_name_home = 'home'
		_state_machine.userdata.move_group = 'manipulator'
		_state_machine.userdata.move_group_prefix1 = '/ariac/arm1'
		_state_machine.userdata.action_topic = '/move_group'
		_state_machine.userdata.robot_name = ''
		_state_machine.userdata.joint_values = []
		_state_machine.userdata.joint_names = []
		_state_machine.userdata.move_group_prefix2 = '/ariac/arm2'
		_state_machine.userdata.ref_frame = 'arm1_linear_arm_actuator'
		_state_machine.userdata.camera_topic = '/ariac/logical_camera_belt1'
		_state_machine.userdata.camera_frame = 'logical_camera_belt1_frame'
		_state_machine.userdata.part_type = 'disk_part'
		_state_machine.userdata.pose = []
		_state_machine.userdata.config_name_belt = 'robotBelt'
		_state_machine.userdata.sensor_topic = '/ariac/break_beam_1'
		_state_machine.userdata.tool_link = 'ee_link'
		_state_machine.userdata.part_offset = 0.04
		_state_machine.userdata.part_rotation = 0

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:32 y:30
			OperatableStateMachine.add('StartAssignment',
										StartAssignment(),
										transitions={'continue': 'TurnOnConveyor'},
										autonomy={'continue': Autonomy.Off})

			# x:522 y:27
			OperatableStateMachine.add('MoveR2home',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'MoveR1Belt', 'planning_failed': 'failed', 'control_failed': 'failed', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_home', 'move_group': 'move_group', 'move_group_prefix': 'move_group_prefix2', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:176 y:29
			OperatableStateMachine.add('TurnOnConveyor',
										SetConveyorbeltPowerState(),
										transitions={'continue': 'MoveR1Home', 'fail': 'failed'},
										autonomy={'continue': Autonomy.Off, 'fail': Autonomy.Off},
										remapping={'power': 'power_on'})

			# x:360 y:28
			OperatableStateMachine.add('MoveR1Home',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'MoveR2home', 'planning_failed': 'failed', 'control_failed': 'failed', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_home', 'move_group': 'move_group', 'move_group_prefix': 'move_group_prefix1', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:690 y:25
			OperatableStateMachine.add('MoveR1Belt',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'DetectPart', 'planning_failed': 'failed', 'control_failed': 'failed', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_belt', 'move_group': 'move_group', 'move_group_prefix': 'move_group_prefix1', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:863 y:25
			OperatableStateMachine.add('DetectPart',
										DetectPartCameraAriacState(time_out=0.5),
										transitions={'continue': 'TurnOffConveyor', 'failed': 'WaitRetry', 'not_found': 'WaitRetry'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'ref_frame': 'ref_frame', 'camera_topic': 'camera_topic', 'camera_frame': 'camera_frame', 'part': 'part_type', 'pose': 'pose'})

			# x:715 y:141
			OperatableStateMachine.add('WaitRetry',
										WaitState(wait_time=0.1),
										transitions={'done': 'DetectPart'},
										autonomy={'done': Autonomy.Off})

			# x:1127 y:363
			OperatableStateMachine.add('MoveToPart',
										MoveitToJointsDynAriacState(),
										transitions={'reached': 'EnableGripper', 'planning_failed': 'failed', 'control_failed': 'EnableGripper'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'move_group_prefix': 'move_group_prefix1', 'move_group': 'move_group', 'action_topic': 'action_topic', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1136 y:455
			OperatableStateMachine.add('EnableGripper',
										GripperControl(enable=True),
										transitions={'continue': 'MoveHome', 'failed': 'failed', 'invalid_id': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'invalid_id': Autonomy.Off},
										remapping={'arm_id': 'arm_id'})

			# x:1115 y:267
			OperatableStateMachine.add('ComputeGrasp',
										ComputeGraspAriacState(joint_names=['linear_arm_actuator_joint', 'shoulder_pan_joint', 'shoulder_lift_joint', 'elbow_joint', 'wrist_1_joint', 'wrist_2_joint', 'wrist_3_joint']),
										transitions={'continue': 'MoveToPart', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'move_group': 'move_group', 'move_group_prefix': 'move_group_prefix1', 'tool_link': 'tool_link', 'pose': 'pose', 'offset': 'part_offset', 'rotation': 'part_rotation', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1081 y:544
			OperatableStateMachine.add('MoveHome',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'finished', 'planning_failed': 'failed', 'control_failed': 'finished', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_home', 'move_group': 'move_group', 'move_group_prefix': 'move_group_prefix1', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1043 y:58
			OperatableStateMachine.add('TurnOffConveyor',
										SetConveyorbeltPowerState(),
										transitions={'continue': 'DetectPart_2', 'fail': 'failed'},
										autonomy={'continue': Autonomy.Off, 'fail': Autonomy.Off},
										remapping={'power': 'power_off'})

			# x:1071 y:136
			OperatableStateMachine.add('DetectPart_2',
										DetectPartCameraAriacState(time_out=0.5),
										transitions={'continue': 'ComputeGrasp', 'failed': 'failed', 'not_found': 'WaitRetry'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'ref_frame': 'ref_frame', 'camera_topic': 'camera_topic', 'camera_frame': 'camera_frame', 'part': 'part_type', 'pose': 'pose'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
