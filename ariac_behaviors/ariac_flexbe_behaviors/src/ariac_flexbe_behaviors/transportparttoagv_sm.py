#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from ariac_flexbe_states.choose_arm import chooseArm
from ariac_flexbe_behaviors.transport_part_from_bin_to_agv_1_sm import transport_part_from_bin_to_agv_1SM
from ariac_flexbe_behaviors.transferparts_sm import TransferPartsSM
from ariac_support_flexbe_states.equal_state import EqualState
from ariac_flexbe_behaviors.find_part_sm import FindPartSM
from ariac_flexbe_behaviors.transport_part_from_bin_to_agv_2_sm import transport_part_from_bin_to_agv_2SM
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Wed May 13 2020
@author: Patrick Verwimp
'''
class TransportPartToAgvSM(Behavior):
	'''
	Transports part from bin to AGV
	'''


	def __init__(self):
		super(TransportPartToAgvSM, self).__init__()
		self.name = 'TransportPartToAgv'

		# parameters of this behavior

		# references to used behaviors
		self.add_behavior(transport_part_from_bin_to_agv_1SM, 'transport_part_from_bin_to_agv_1')
		self.add_behavior(TransferPartsSM, 'TransferParts')
		self.add_behavior(FindPartSM, 'Find Part')
		self.add_behavior(transport_part_from_bin_to_agv_2SM, 'transport_part_from_bin_to_agv_2')

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:1045 y:65, x:489 y:361
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'], input_keys=['agv_id', 'part_type', 'pose_on_agv'])
		_state_machine.userdata.config_name_home = 'home'
		_state_machine.userdata.move_group = 'manipulator'
		_state_machine.userdata.move_group_prefix = ''
		_state_machine.userdata.action_topic = '/move_group'
		_state_machine.userdata.robot_name = ''
		_state_machine.userdata.agv_id = ''
		_state_machine.userdata.part_type = 'pulley_part'
		_state_machine.userdata.camera_topic = ''
		_state_machine.userdata.camera_frame = ''
		_state_machine.userdata.ref_frame = ''
		_state_machine.userdata.bin = ''
		_state_machine.userdata.agv1 = 'agv1'
		_state_machine.userdata.pose_on_agv = []

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:71 y:27
			OperatableStateMachine.add('CorrectArm_2',
										chooseArm(),
										transitions={'continue': 'Find Part', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'agv_id': 'agv_id', 'move_group_prefix': 'move_group_prefix'})

			# x:716 y:17
			OperatableStateMachine.add('transport_part_from_bin_to_agv_1',
										self.use_behavior(transport_part_from_bin_to_agv_1SM, 'transport_part_from_bin_to_agv_1'),
										transitions={'finished': 'finished', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit},
										remapping={'bin': 'bin', 'move_group_prefix': 'move_group_prefix', 'camera_topic': 'camera_topic', 'camera_frame': 'camera_frame', 'ref_frame': 'ref_frame', 'agv_id': 'agv_id', 'part_type': 'part_type', 'pose_on_agv': 'pose_on_agv'})

			# x:538 y:108
			OperatableStateMachine.add('TransferParts',
										self.use_behavior(TransferPartsSM, 'TransferParts'),
										transitions={'finished': 'CorrectArm', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit},
										remapping={'move_group_prefix': 'move_group_prefix', 'part_type': 'part_type', 'bin': 'bin', 'camera_topic': 'camera_topic', 'camera_frame': 'camera_frame', 'agv_id': 'agv_id', 'ref_frame': 'ref_frame'})

			# x:321 y:112
			OperatableStateMachine.add('CorrectArm',
										chooseArm(),
										transitions={'continue': 'Find Part', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'agv_id': 'agv_id', 'move_group_prefix': 'move_group_prefix'})

			# x:540 y:34
			OperatableStateMachine.add('Agv1?',
										EqualState(),
										transitions={'true': 'transport_part_from_bin_to_agv_1', 'false': 'transport_part_from_bin_to_agv_2'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'agv1', 'value_b': 'agv_id'})

			# x:304 y:34
			OperatableStateMachine.add('Find Part',
										self.use_behavior(FindPartSM, 'Find Part'),
										transitions={'to_agv': 'Agv1?', 'failed': 'failed', 'part_not_in_bin': 'failed', 'transfer': 'TransferParts'},
										autonomy={'to_agv': Autonomy.Inherit, 'failed': Autonomy.Inherit, 'part_not_in_bin': Autonomy.Inherit, 'transfer': Autonomy.Inherit},
										remapping={'move_group_prefix': 'move_group_prefix', 'part_type': 'part_type', 'agv_id': 'agv_id', 'bin': 'bin', 'camera_topic': 'camera_topic', 'camera_frame': 'camera_frame', 'ref_frame': 'ref_frame'})

			# x:718 y:105
			OperatableStateMachine.add('transport_part_from_bin_to_agv_2',
										self.use_behavior(transport_part_from_bin_to_agv_2SM, 'transport_part_from_bin_to_agv_2'),
										transitions={'finished': 'finished', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit},
										remapping={'bin': 'bin', 'move_group_prefix': 'move_group_prefix', 'camera_topic': 'camera_topic', 'camera_frame': 'camera_frame', 'ref_frame': 'ref_frame', 'agv_id': 'agv_id', 'part_type': 'part_type', 'pose_on_agv': 'pose_on_agv'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
