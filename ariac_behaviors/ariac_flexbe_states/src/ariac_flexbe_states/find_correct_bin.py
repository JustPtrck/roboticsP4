#!/usr/bin/env python
import rospy
import rostopic
import inspect

from flexbe_core import EventState, Logger
from osrf_gear.msg import LogicalCameraImage, Model
from flexbe_core.proxy import ProxySubscriberCached
'''

Created on May 13 2020

@author: Patrick Verwimp 2132138

'''

class FindPart(EventState):
	'''
	Checks camera's and returns the correct location
	Extra info

	-- time_out	float 	Time which needs to have passed since the behavior started.
	># part_type	string	part to find
	># agv_id	string	agv for shipment

	#> bin		string	part location bin
	#> camera_topic	string	set camera
	#> camera_frame	string	set camera frame
	#> ref_frame	string	set ref

	<= in_range 			Part in range
	<= out_of_range			Part out of range
	<= failed 				Example for a failure outcome.
	<= not_found				a

	'''

	def __init__(self, time_out = 0.5):
		# Declare outcomes, input_keys, and output_keys by calling the super constructor with the corresponding arguments.
		super(FindPart, self).__init__(input_keys = ['part_type', 'agv_id'], outcomes = ['in_range', 'out_of_range', 'failed', 'not_found'], output_keys = ['bin','camera_topic','camera_frame','ref_frame'])

		# Store state parameter for later use.
		self._wait = time_out


	def execute(self, userdata):
		# This method is called periodically while the state is active.
		# Main purpose is to check state conditions and trigger a corresponding outcome.
		# If no outcome is returned, the state will stay active.

 		# One of the outcomes declared above.
		if userdata.agv_id == "agv2":
		   	for i in [1,2,3,4,5,6]:
				self._topic = "/ariac/logical_camera_bin"+str(i)

				self._start_time = rospy.Time.now()

				(msg_path, msg_topic, fn) = rostopic.get_topic_type(self._topic)

				if msg_topic == self._topic:
					msg_type = self._get_msg_from_path(msg_path)
					self._sub = ProxySubscriberCached({self._topic: msg_type})
				elapsed = rospy.get_rostime() - self._start_time;
				while (elapsed.to_sec() < self._wait):
					elapsed = rospy.get_rostime() - self._start_time;
					if self._sub.has_msg(self._topic):
						message = self._sub.get_last_msg(self._topic)
						for model in message.models:
							if model.type == userdata.part_type:
								userdata.bin = "bin"+str(i)+"PreGrasp"
								userdata.camera_topic = "/ariac/logical_camera_bin"+str(i)
								userdata.camera_frame = "logical_camera_bin"+str(i)+"_frame"
								Logger.loginfo("bin"+str(i)+"PreGrasp")
								if i > 3:
									userdata.ref_frame = "arm1_linear_arm_actuator"
									Logger.loginfo("Part out of range")
									return 'out_of_range'
								userdata.ref_frame = "arm2_linear_arm_actuator"
								return 'in_range'
			Logger.loginfo("part_type not found")
		   	return 'not_found'
		if userdata.agv_id == "agv1":
		   	for i in [6,5,4,3,2,1]:
				self._topic = "/ariac/logical_camera_bin"+str(i)

				self._start_time = rospy.Time.now()

				(msg_path, msg_topic, fn) = rostopic.get_topic_type(self._topic)

				if msg_topic == self._topic:
					msg_type = self._get_msg_from_path(msg_path)
					self._sub = ProxySubscriberCached({self._topic: msg_type})
				elapsed = rospy.get_rostime() - self._start_time;
				while (elapsed.to_sec() < self._wait):
					elapsed = rospy.get_rostime() - self._start_time;
					if self._sub.has_msg(self._topic):
						message = self._sub.get_last_msg(self._topic)
						for model in message.models:
							if model.type == userdata.part_type:
								userdata.bin = "bin"+str(i)+"PreGrasp"
								userdata.camera_topic = "/ariac/logical_camera_bin"+str(i)
								userdata.camera_frame = "logical_camera_bin"+str(i)+"_frame"
								Logger.loginfo("bin"+str(i)+"PreGrasp")
								if i < 4:
									userdata.ref_frame = "arm2_linear_arm_actuator"
									Logger.loginfo("Part out of range")
									return 'out_of_range'
								userdata.ref_frame = "arm1_linear_arm_actuator"
								return 'in_range'
			Logger.loginfo("part_type not found")
		   	return 'not_found'

	def on_enter(self, userdata):
		# This method is called when the state becomes active, i.e. a transition from another state to this one is taken.
		# It is primarily used to start actions which are associated with this state.

		# The following code is just for illustrating how the behavior logger works.
		# Text logged by the behavior logger is sent to the operator and displayed in the GUI.
		pass # Nothing to do in this example.

	def on_exit(self, userdata):
		# This method is called when an outcome is returned and another state gets active.
		# It can be used to stop possibly running processes started by on_enter.

		pass # Nothing to do in this example.


	def on_start(self):
		# This method is called when the behavior is started.
		# If possible, it is generally better to initialize used resources in the constructor
		# because if anything failed, the behavior would not even be started.

		# In this example, we use this event to set the correct start time.
		self._start_time = rospy.Time.now()



	def on_stop(self):
		# This method is called whenever the behavior stops execution, also if it is cancelled.
		# Use this event to clean up things like claimed resources.

		pass # Nothing to do in this example.



	def _get_msg_from_path(self, msg_path):
		'''
		Created on 11.06.2013

		@author: Philipp Schillinger
		'''
		msg_import = msg_path.split('/')
		msg_module = '%s.msg' % (msg_import[0])
		package = __import__(msg_module, fromlist=[msg_module])
		clsmembers = inspect.getmembers(package, lambda member: inspect.isclass(member) and member.__module__.endswith(msg_import[1]))
		return clsmembers[0][1]
