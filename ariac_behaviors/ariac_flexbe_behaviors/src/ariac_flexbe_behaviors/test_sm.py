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
from ariac_flexbe_behaviors.find_part_sm import FindPartSM
from ariac_flexbe_behaviors.transport_part_from_bin_to_agv_1_sm import transport_part_from_bin_to_agv_1SM
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Wed May 13 2020
@author: das
'''
class testSM(Behavior):
	'''
	sc
	'''


	def __init__(self):
		super(testSM, self).__init__()
		self.name = 'test'

		# parameters of this behavior

		# references to used behaviors
		self.add_behavior(FindPartSM, 'Find Part')
		self.add_behavior(transport_part_from_bin_to_agv_1SM, 'transport_part_from_bin_to_agv_1')

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:690 y:301, x:130 y:365
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])
		_state_machine.userdata.config_name_home = 'home'
		_state_machine.userdata.move_group = 'manipulator'
		_state_machine.userdata.move_group_prefix = '/ariac/arm1'
		_state_machine.userdata.action_topic = '/move_group'
		_state_machine.userdata.robot_name = ''
		_state_machine.userdata.agv_id = 'agv1'
		_state_machine.userdata.part_type = 'piston_rod_part'
		_state_machine.userdata.camera_topic = ''
		_state_machine.userdata.camera_frame = ''
		_state_machine.userdata.ref_frame = ''
		_state_machine.userdata.bin = ''

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:30 y:40
			OperatableStateMachine.add('Home',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'Find Part', 'planning_failed': 'failed', 'control_failed': 'failed', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_home', 'move_group': 'move_group', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:369 y:69
			OperatableStateMachine.add('Find Part',
										self.use_behavior(FindPartSM, 'Find Part'),
										transitions={'to_agv': 'transport_part_from_bin_to_agv_1', 'failed': 'failed', 'part_not_in_bin': 'failed', 'transfer': 'MoveToPart_2'},
										autonomy={'to_agv': Autonomy.Inherit, 'failed': Autonomy.Inherit, 'part_not_in_bin': Autonomy.Inherit, 'transfer': Autonomy.Inherit},
										remapping={'move_group_prefix': 'move_group_prefix', 'part_type': 'part_type', 'agv_id': 'agv_id', 'bin': 'bin', 'camera_topic': 'camera_topic', 'camera_frame': 'camera_frame', 'ref_frame': 'ref_frame'})

			# x:488 y:206
			OperatableStateMachine.add('MoveToPart_2',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'finished', 'planning_failed': 'failed', 'control_failed': 'failed', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'bin', 'move_group': 'move_group', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:613 y:68
			OperatableStateMachine.add('transport_part_from_bin_to_agv_1',
										self.use_behavior(transport_part_from_bin_to_agv_1SM, 'transport_part_from_bin_to_agv_1'),
										transitions={'finished': 'finished', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit},
										remapping={'bin': 'bin', 'move_group_prefix': 'move_group_prefix', 'camera_topic': 'camera_topic', 'camera_frame': 'camera_frame', 'ref_frame': 'ref_frame', 'agv_id': 'agv_id', 'part_type': 'part_type'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
