#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from ariac_flexbe_states.detect_part_camera_ariac_state import DetectPartCameraAriacState
from ariac_support_flexbe_states.replace_state import ReplaceState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Wed May 13 2020
@author: Wessel Koolen
'''
class camera_detect_partSM(Behavior):
	'''
	Behavior finding part, outputting part location
	'''


	def __init__(self):
		super(camera_detect_partSM, self).__init__()
		self.name = 'camera_detect_part'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:677 y:290, x:12 y:267
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'], input_keys=['part_type', 'agv_id'], output_keys=['arm_id', 'move_group_prefix', 'config_name_bin'])
		_state_machine.userdata.config_name_bin = ''
		_state_machine.userdata.part_type = ''
		_state_machine.userdata.agv_id = ''
		_state_machine.userdata.arm_id = ''
		_state_machine.userdata.move_group_prefix = ''
		_state_machine.userdata.config_name_bin = ''
		_state_machine.userdata.camera_topic1 = '/ariac/logical_camera_bin1'
		_state_machine.userdata.camera_topic2 = '/ariac/logical_camera_bin2'
		_state_machine.userdata.camera_topic3 = '/ariac/logical_camera_bin3'
		_state_machine.userdata.camera_topic4 = '/ariac/logical_camera_bin4'
		_state_machine.userdata.camera_topic5 = '/ariac/logical_camera_bin5'
		_state_machine.userdata.camera_topic6 = '/ariac/logical_camera_bin6'
		_state_machine.userdata.camera_frame = 'logical_camera_frame'
		_state_machine.userdata.camera_ref_frame = ''

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:101 y:40
			OperatableStateMachine.add('DetectPartCamera',
										DetectPartCameraAriacState(time_out=1.0),
										transitions={'continue': 'ReplaceTransferBin', 'failed': 'failed', 'not_found': 'DetectPartCamera_2'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'ref_frame': 'camera_ref_frame', 'camera_topic': 'camera_topic1', 'camera_frame': 'camera_frame', 'part': 'part_type', 'pose': 'pose'})

			# x:322 y:41
			OperatableStateMachine.add('ReplaceTransferBin',
										ReplaceState(),
										transitions={'done': 'finished'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'config_name_bin', 'result': 'bin1PreGrasp'})

			# x:101 y:117
			OperatableStateMachine.add('DetectPartCamera_2',
										DetectPartCameraAriacState(time_out=1.0),
										transitions={'continue': 'ReplaceTransferBin_2', 'failed': 'failed', 'not_found': 'DetectPartCamera_3'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'ref_frame': 'camera_ref_frame', 'camera_topic': 'camera_topic2', 'camera_frame': 'camera_frame', 'part': 'part_type', 'pose': 'pose'})

			# x:322 y:121
			OperatableStateMachine.add('ReplaceTransferBin_2',
										ReplaceState(),
										transitions={'done': 'finished'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'config_name_bin', 'result': 'bin2PreGrasp'})

			# x:101 y:209
			OperatableStateMachine.add('DetectPartCamera_3',
										DetectPartCameraAriacState(time_out=1.0),
										transitions={'continue': 'ReplaceTransferBin_3', 'failed': 'failed', 'not_found': 'DetectPartCamera_4'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'ref_frame': 'camera_ref_frame', 'camera_topic': 'camera_topic3', 'camera_frame': 'camera_frame', 'part': 'part_type', 'pose': 'pose'})

			# x:322 y:207
			OperatableStateMachine.add('ReplaceTransferBin_3',
										ReplaceState(),
										transitions={'done': 'finished'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'config_name_bin', 'result': 'bin3PreGrasp'})

			# x:101 y:301
			OperatableStateMachine.add('DetectPartCamera_4',
										DetectPartCameraAriacState(time_out=1.0),
										transitions={'continue': 'ReplaceTransferBin_4', 'failed': 'failed', 'not_found': 'DetectPartCamera_5'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'ref_frame': 'camera_ref_frame', 'camera_topic': 'camera_topic4', 'camera_frame': 'camera_frame', 'part': 'part_type', 'pose': 'pose'})

			# x:326 y:304
			OperatableStateMachine.add('ReplaceTransferBin_4',
										ReplaceState(),
										transitions={'done': 'finished'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'config_name_bin', 'result': 'bin4PreGrasp'})

			# x:101 y:393
			OperatableStateMachine.add('DetectPartCamera_5',
										DetectPartCameraAriacState(time_out=1.0),
										transitions={'continue': 'ReplaceTransferBin_5', 'failed': 'failed', 'not_found': 'DetectPartCamera_6'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'ref_frame': 'camera_ref_frame', 'camera_topic': 'camera_topic5', 'camera_frame': 'camera_frame', 'part': 'part_type', 'pose': 'pose'})

			# x:328 y:392
			OperatableStateMachine.add('ReplaceTransferBin_5',
										ReplaceState(),
										transitions={'done': 'finished'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'config_name_bin', 'result': 'bin5PreGrasp'})

			# x:101 y:485
			OperatableStateMachine.add('DetectPartCamera_6',
										DetectPartCameraAriacState(time_out=1.0),
										transitions={'continue': 'ReplaceTransferBin_6', 'failed': 'failed', 'not_found': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'ref_frame': 'camera_ref_frame', 'camera_topic': 'camera_topic6', 'camera_frame': 'camera_frame', 'part': 'part_type', 'pose': 'pose'})

			# x:327 y:488
			OperatableStateMachine.add('ReplaceTransferBin_6',
										ReplaceState(),
										transitions={'done': 'finished'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'config_name_bin', 'result': 'bin6PreGrasp'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
