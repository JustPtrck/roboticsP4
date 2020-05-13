#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from ariac_flexbe_states.find_correct_bin import FindPart
from ariac_support_flexbe_states.equal_state import EqualState
from ariac_support_flexbe_states.replace_state import ReplaceState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Wed May 13 2020
@author: Patrick Verwimp
'''
class FindPartSM(Behavior):
	'''
	WIP part finder
edits location
switches arm choice when needed
	'''


	def __init__(self):
		super(FindPartSM, self).__init__()
		self.name = 'Find Part'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:625 y:34, x:36 y:176, x:34 y:79
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed', 'part_not_in_bin'], input_keys=['move_group_prefix', 'part_type', 'agv_id'], output_keys=['bin', 'move_group_prefix', 'camera_topic', 'camera_frame', 'ref_frame'])
		_state_machine.userdata.part_type = []
		_state_machine.userdata.agv_id = []
		_state_machine.userdata.bin = ''
		_state_machine.userdata.move_group_prefix = []
		_state_machine.userdata.arm1 = '/ariac/arm1'
		_state_machine.userdata.arm2 = '/ariac/arm2'
		_state_machine.userdata.camera_topic = ''
		_state_machine.userdata.camera_frame = ''
		_state_machine.userdata.ref_frame = ''

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:157 y:25
			OperatableStateMachine.add('FindPart',
										FindPart(time_out=0.5),
										transitions={'in_range': 'finished', 'out_of_range': 'Arm1Active?', 'failed': 'failed', 'not_found': 'part_not_in_bin'},
										autonomy={'in_range': Autonomy.Off, 'out_of_range': Autonomy.Off, 'failed': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'part_type': 'part_type', 'agv_id': 'agv_id', 'bin': 'bin', 'camera_topic': 'camera_topic', 'camera_frame': 'camera_frame', 'ref_frame': 'ref_frame'})

			# x:145 y:154
			OperatableStateMachine.add('Arm1Active?',
										EqualState(),
										transitions={'true': 'SwitchArmTo2', 'false': 'SwitchArmTo1'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'arm1', 'value_b': 'move_group_prefix'})

			# x:342 y:108
			OperatableStateMachine.add('SwitchArmTo1',
										ReplaceState(),
										transitions={'done': 'finished'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'arm1', 'result': 'move_group_prefix'})

			# x:342 y:185
			OperatableStateMachine.add('SwitchArmTo2',
										ReplaceState(),
										transitions={'done': 'finished'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'arm2', 'result': 'move_group_prefix'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
