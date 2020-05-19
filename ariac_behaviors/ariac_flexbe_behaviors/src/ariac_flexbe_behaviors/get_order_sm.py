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
from ariac_logistics_flexbe_states.get_part_from_products_state import GetPartFromProductsState
from ariac_flexbe_behaviors.transportparttoagv_sm import TransportPartToAgvSM
from ariac_support_flexbe_states.add_numeric_state import AddNumericState
from ariac_support_flexbe_states.equal_state import EqualState
from ariac_flexbe_behaviors.notify_shipment_ready_sm import notify_shipment_readySM
from ariac_flexbe_states.messageLogger import MessageLogger
from ariac_logistics_flexbe_states.get_products_from_shipment_state import GetProductsFromShipmentState
from ariac_logistics_flexbe_states.get_order_state import GetOrderState
from ariac_support_flexbe_states.replace_state import ReplaceState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Sun Apr 19 2020
@author: Gerard Harkema
'''
class get_orderSM(Behavior):
	'''
	Tests the starting and stopping of the assignment
	'''


	def __init__(self):
		super(get_orderSM, self).__init__()
		self.name = 'get_order'

		# parameters of this behavior

		# references to used behaviors
		self.add_behavior(TransportPartToAgvSM, 'TransportPartToAgv')
		self.add_behavior(notify_shipment_readySM, 'notify_shipment_ready')

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:667 y:540, x:729 y:205
		_state_machine = OperatableStateMachine(outcomes=['finished', 'fail'])
		_state_machine.userdata.shipments = []
		_state_machine.userdata.part_type = ''
		_state_machine.userdata.material_locations = []
		_state_machine.userdata.number_of_shipments = 0
		_state_machine.userdata.order_id = ''
		_state_machine.userdata.products = []
		_state_machine.userdata.number_of_products = 0
		_state_machine.userdata.agv_id = ''
		_state_machine.userdata.shipment_type = ''
		_state_machine.userdata.pose = []
		_state_machine.userdata.product_index = 0
		_state_machine.userdata.shipment_index = 1
		_state_machine.userdata.add_one = 1
		_state_machine.userdata.part_pose = []
		_state_machine.userdata.zero = 0

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:30 y:40
			OperatableStateMachine.add('Start',
										StartAssignment(),
										transitions={'continue': 'GetOrder'},
										autonomy={'continue': Autonomy.Off})

			# x:905 y:34
			OperatableStateMachine.add('GetProductPose',
										GetPartFromProductsState(),
										transitions={'continue': 'message_3', 'invalid_index': 'fail'},
										autonomy={'continue': Autonomy.Off, 'invalid_index': Autonomy.Off},
										remapping={'products': 'products', 'index': 'product_index', 'type': 'part_type', 'pose': 'part_pose'})

			# x:1091 y:123
			OperatableStateMachine.add('TransportPartToAgv',
										self.use_behavior(TransportPartToAgvSM, 'TransportPartToAgv'),
										transitions={'finished': 'IncrementProductIndex', 'failed': 'fail'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit},
										remapping={'agv_id': 'agv_id', 'part_type': 'part_type', 'part_pose': 'part_pose'})

			# x:1095 y:229
			OperatableStateMachine.add('IncrementProductIndex',
										AddNumericState(),
										transitions={'done': 'ShipmentReady?'},
										autonomy={'done': Autonomy.Off},
										remapping={'value_a': 'product_index', 'value_b': 'add_one', 'result': 'product_index'})

			# x:1092 y:486
			OperatableStateMachine.add('IncrementShipmentIndex',
										AddNumericState(),
										transitions={'done': 'notify_shipment_ready'},
										autonomy={'done': Autonomy.Off},
										remapping={'value_a': 'shipment_index', 'value_b': 'add_one', 'result': 'shipment_index'})

			# x:1094 y:329
			OperatableStateMachine.add('ShipmentReady?',
										EqualState(),
										transitions={'true': 'ResetProductIndex', 'false': 'GetProductPose'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'product_index', 'value_b': 'number_of_products'})

			# x:474 y:461
			OperatableStateMachine.add('OrderReady?',
										EqualState(),
										transitions={'true': 'ResetShiptIndex', 'false': 'GetProductsShipment'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'shipment_index', 'value_b': 'number_of_shipments'})

			# x:857 y:483
			OperatableStateMachine.add('notify_shipment_ready',
										self.use_behavior(notify_shipment_readySM, 'notify_shipment_ready'),
										transitions={'finished': 'OrderReady?', 'failed': 'fail'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})

			# x:402 y:33
			OperatableStateMachine.add('message',
										MessageLogger(),
										transitions={'continue': 'GetProductsShipment'},
										autonomy={'continue': Autonomy.Off},
										remapping={'message': 'order_id'})

			# x:766 y:40
			OperatableStateMachine.add('message_2',
										MessageLogger(),
										transitions={'continue': 'GetProductPose'},
										autonomy={'continue': Autonomy.Off},
										remapping={'message': 'shipment_type'})

			# x:1090 y:36
			OperatableStateMachine.add('message_3',
										MessageLogger(),
										transitions={'continue': 'TransportPartToAgv'},
										autonomy={'continue': Autonomy.Off},
										remapping={'message': 'part_type'})

			# x:560 y:34
			OperatableStateMachine.add('GetProductsShipment',
										GetProductsFromShipmentState(),
										transitions={'continue': 'message_2', 'invalid_index': 'fail'},
										autonomy={'continue': Autonomy.Off, 'invalid_index': Autonomy.Off},
										remapping={'shipments': 'shipments', 'index': 'shipment_index', 'shipment_type': 'shipment_type', 'agv_id': 'agv_id', 'products': 'products', 'number_of_products': 'number_of_products'})

			# x:203 y:32
			OperatableStateMachine.add('GetOrder',
										GetOrderState(),
										transitions={'continue': 'message'},
										autonomy={'continue': Autonomy.Off},
										remapping={'order_id': 'order_id', 'shipments': 'shipments', 'number_of_shipments': 'number_of_shipments'})

			# x:1090 y:407
			OperatableStateMachine.add('ResetProductIndex',
										ReplaceState(),
										transitions={'done': 'IncrementShipmentIndex'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'zero', 'result': 'product_index'})

			# x:338 y:318
			OperatableStateMachine.add('ResetShiptIndex',
										ReplaceState(),
										transitions={'done': 'GetOrder'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'zero', 'result': 'shipment_index'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
