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
from ariac_flexbe_behaviors.find_part_sm import FindPartSM
from ariac_flexbe_behaviors.transport_part_from_bin_to_agv_1_sm import transport_part_from_bin_to_agv_1SM
from ariac_flexbe_behaviors.transferparts_sm import TransferPartsSM
from ariac_flexbe_states.choose_arm import chooseArm
from ariac_flexbe_states.srdf_state_to_moveit_ariac_state import SrdfStateToMoveitAriac
from ariac_flexbe_behaviors.transport_part_from_bin_to_arv_2_sm import transport_part_from_bin_to_arv_2SM
from ariac_support_flexbe_states.equal_state import EqualState
from ariac_flexbe_states.end_assignment_state import EndAssignment
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Wed May 13 2020
@author: Patrick Verwimp
'''
class MainSM(Behavior):
	'''
	sc
	'''


	def __init__(self):
		super(MainSM, self).__init__()
		self.name = 'Main'

		# parameters of this behavior

		# references to used behaviors
		self.add_behavior(FindPartSM, 'Find Part')
		self.add_behavior(transport_part_from_bin_to_agv_1SM, 'transport_part_from_bin_to_agv_1')
		self.add_behavior(TransferPartsSM, 'TransferParts')
		self.add_behavior(transport_part_from_bin_to_arv_2SM, 'transport_part_from_bin_to_arv_2')

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:1116 y:214, x:130 y:365
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])
		_state_machine.userdata.config_name_home = 'home'
		_state_machine.userdata.move_group = 'manipulator'
		_state_machine.userdata.move_group_prefix = ''
		_state_machine.userdata.action_topic = '/move_group'
		_state_machine.userdata.robot_name = ''
		_state_machine.userdata.agv_id = 'agv2'
		_state_machine.userdata.part_type = 'pulley_part'
		_state_machine.userdata.camera_topic = ''
		_state_machine.userdata.camera_frame = ''
		_state_machine.userdata.ref_frame = ''
		_state_machine.userdata.bin = ''
		_state_machine.userdata.agv1 = 'agv1'

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:30 y:103
			OperatableStateMachine.add('Start',
										StartAssignment(),
										transitions={'continue': 'CorrectArm_2'},
										autonomy={'continue': Autonomy.Off})

			# x:369 y:69
			OperatableStateMachine.add('Find Part',
										self.use_behavior(FindPartSM, 'Find Part'),
										transitions={'to_agv': 'Agv1?', 'failed': 'failed', 'part_not_in_bin': 'failed', 'transfer': 'TransferParts'},
										autonomy={'to_agv': Autonomy.Inherit, 'failed': Autonomy.Inherit, 'part_not_in_bin': Autonomy.Inherit, 'transfer': Autonomy.Inherit},
										remapping={'move_group_prefix': 'move_group_prefix', 'part_type': 'part_type', 'agv_id': 'agv_id', 'bin': 'bin', 'camera_topic': 'camera_topic', 'camera_frame': 'camera_frame', 'ref_frame': 'ref_frame'})

			# x:800 y:27
			OperatableStateMachine.add('transport_part_from_bin_to_agv_1',
										self.use_behavior(transport_part_from_bin_to_agv_1SM, 'transport_part_from_bin_to_agv_1'),
										transitions={'finished': 'End', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit},
										remapping={'bin': 'bin', 'move_group_prefix': 'move_group_prefix', 'camera_topic': 'camera_topic', 'camera_frame': 'camera_frame', 'ref_frame': 'ref_frame', 'agv_id': 'agv_id', 'part_type': 'part_type'})

			# x:550 y:180
			OperatableStateMachine.add('TransferParts',
										self.use_behavior(TransferPartsSM, 'TransferParts'),
										transitions={'finished': 'CorrectArm', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit},
										remapping={'move_group_prefix': 'move_group_prefix', 'part_type': 'part_type', 'bin': 'bin', 'camera_topic': 'camera_topic', 'camera_frame': 'camera_frame', 'agv_id': 'agv_id', 'ref_frame': 'ref_frame'})

			# x:337 y:173
			OperatableStateMachine.add('CorrectArm',
										chooseArm(),
										transitions={'continue': 'Find Part', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'agv_id': 'agv_id', 'move_group_prefix': 'move_group_prefix'})

			# x:189 y:62
			OperatableStateMachine.add('Home',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'Find Part', 'planning_failed': 'failed', 'control_failed': 'failed', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_home', 'move_group': 'move_group', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:769 y:224
			OperatableStateMachine.add('transport_part_from_bin_to_arv_2',
										self.use_behavior(transport_part_from_bin_to_arv_2SM, 'transport_part_from_bin_to_arv_2'),
										transitions={'finished': 'End', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit},
										remapping={'bin': 'bin', 'move_group_prefix': 'move_group_prefix', 'camera_topic': 'camera_topic', 'camera_frame': 'camera_frame', 'ref_frame': 'ref_frame', 'agv_id': 'agv_id', 'part_type': 'part_type'})

			# x:549 y:19
			OperatableStateMachine.add('Agv1?',
										EqualState(),
										transitions={'true': 'transport_part_from_bin_to_agv_1', 'false': 'transport_part_from_bin_to_arv_2'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'agv1', 'value_b': 'agv_id'})

			# x:1059 y:360
			OperatableStateMachine.add('End',
										EndAssignment(),
										transitions={'continue': 'finished'},
										autonomy={'continue': Autonomy.Off})

			# x:37 y:41
			OperatableStateMachine.add('CorrectArm_2',
										chooseArm(),
										transitions={'continue': 'Home', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'agv_id': 'agv_id', 'move_group_prefix': 'move_group_prefix'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
