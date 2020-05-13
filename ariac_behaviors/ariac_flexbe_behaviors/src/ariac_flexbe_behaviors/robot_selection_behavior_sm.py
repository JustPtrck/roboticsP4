#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from ariac_support_flexbe_states.equal_state import EqualState
from ariac_support_flexbe_states.replace_state import ReplaceState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Wed May 13 2020
@author: Wessel Koolen
'''
class robot_selection_behaviorSM(Behavior):
	'''
	Dit behavior wordt gebruikt voor het selecteren van de juiste robotarm
	'''


	def __init__(self):
		super(robot_selection_behaviorSM, self).__init__()
		self.name = 'robot_selection_behavior'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:501 y:113, x:89 y:300
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'], input_keys=['arm_id'], output_keys=['move_group_prefix'])
		_state_machine.userdata.prefix_arm1 = 'ariac/arm1'
		_state_machine.userdata.prefix_arm2 = 'ariac/arm2'
		_state_machine.userdata.arm1 = 'arm1'
		_state_machine.userdata.arm2 = 'arm2'
		_state_machine.userdata.arm_id = ''
		_state_machine.userdata.move_group_prefix = ''

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:41 y:41
			OperatableStateMachine.add('RobotEqualState',
										EqualState(),
										transitions={'true': 'RobotValueState', 'false': 'RobotEqualState_2'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'arm_id', 'value_b': 'arm1'})

			# x:239 y:40
			OperatableStateMachine.add('RobotValueState',
										ReplaceState(),
										transitions={'done': 'finished'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'prefix_arm1', 'result': 'move_group_prefix'})

			# x:41 y:161
			OperatableStateMachine.add('RobotEqualState_2',
										EqualState(),
										transitions={'true': 'RobotValueState_2', 'false': 'failed'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'arm_id', 'value_b': 'arm2'})

			# x:242 y:160
			OperatableStateMachine.add('RobotValueState_2',
										ReplaceState(),
										transitions={'done': 'finished'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'prefix_arm2', 'result': 'move_group_prefix'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
