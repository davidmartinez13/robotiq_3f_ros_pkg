#!/usr/bin/env python

import rospy
import roslib;
roslib.load_manifest('robotiq_3f_gripper_control')
from robotiq_3f_gripper_articulated_msgs.msg import Robotiq3FGripperRobotInput as inputMsg
from robotiq_3f_gripper_articulated_msgs.msg import Robotiq3FGripperRobotOutput as outputMsg

from time import sleep

#################################################
# NOTE:This program assumes simple control mode #
#################################################

class Robotic3fGripperDriver(object):
    def __init__(self):
        self._command_pub = rospy.Publisher('Robotiq3FGripperRobotOutput', outputMsg, queue_size=1)
        rospy.Subscriber("Robotiq3FGripperRobotInput", inputMsg, self._gripper_status_callback, queue_size=1)
        self._gripper_status = inputMsg()
        self._command = outputMsg()
        self._timeout = 30

    def _gripper_status_callback(self, msg):
        self._gripper_status = msg

    def _is_activated(self):
        if self._gripper_status.gACT == 0:
            return False
        elif self._gripper_status.gIMC == 0:
            return False
        else:
            return True

    def reset(self):
        self._command = outputMsg()
        self._command.rACT = 0
        self._command_pub.publish(self._command)

    def activate(self):
        self._command = outputMsg()
        self._command.rACT = 1
        self._command.rGTO = 1
        self._command.rSPA = 255
        self._command.rFRA = 150
        self._command_pub.publish(self._command)

    def open_hand(self):
        self._command.rPRA = 0
        self._command_pub.publish(self._command)

    def close_hand(self):
        self._command.rPRA = 255
        self._command_pub.publish(self._command)

    def set_mode(self, mode):
        if mode == 'basic':
            self._command.rMOD = 0
        elif mode == 'pinch':
            self._command.rMOD = 1
        elif mode == 'wide':
            self._command.rMOD = 2
        elif mode == 'scissor':
            self._command.rMOD = 3
        else:
            return
        self._command_pub.publish(self._command)

    def set_position(self, position):
        self._command.rPRA = int(position)
        if self._command.rPRA > 255:
            self._command.rPRA = 255
        elif self._command.rPRA < 0:
            self._command.rPRA = 0
        self._command_pub.publish(self._command)

    def set_speed(self, speed):
        self._command.rSPA = int(speed)
        if self._command.rSPA > 255:
            self._command.rSPA = 255
        elif self._command.rSPA < 0:
            self._command.rSPA = 0
        self._command_pub.publish(self._command)

    def set_torque(self, torque):
        self._command.rFRA = int(torque)
        if self._command.rFRA > 255:
            self._command.rFRA = 255
        elif self._command.rFRA < 0:
            self._command.rFRA = 0
        self._command_pub.publish(self._command)

    def get_mode(self):
        mode = self._gripper_status.gMOD
        if mode == 0:
            return 'basic'
        elif mode == 1:
            return 'pinch'
        elif mode == 2:
            return 'wide'
        elif mode == 3:
            return 'scissor'
    # TODO: fix pos request not updating
    def get_position_target(self):
        return int(self._gripper_status.gPRA)
        sleep(0.5)
        # status: go to position request
        # if self._gripper_status.gGTO == 1:
        #     count = 0
        #     while count < self._timeout:
        #         # status: gripper is stopped
        #         if self._gripper_status.gSTA != 0:
        #             return self._gripper_status.gPRA
        #         sleep(0.1)
        #         count += 1

    def get_position_a(self):
        return int(self._gripper_status.gPOA)
        sleep(0.5)
        # status: go to position request
        # if self._gripper_status.gGTO == 1:
        #     count = 0
        #     while count < self._timeout:
        #         # status: gripper is stopped
        #         if self._gripper_status.gSTA != 0:
        #             return self._gripper_status.gPOA
        #         sleep(0.1)
        #         count += 1

    def get_position_b(self):
        return int(self._gripper_status.gPOB)
        sleep(0.5)
        # status: go to position request
        # if self._gripper_status.gGTO == 1:
        #     count = 0
        #     while count < self._timeout:
        #         # status: gripper is stopped
        #         if self._gripper_status.gSTA != 0:
        #             return self._gripper_status.gPOB
        #         sleep(0.1)
        #         count += 1

    def get_position_c(self):
        return int(self._gripper_status.gPOC)
        sleep(0.5)
        # status: go to position request
        # if self._gripper_status.gGTO == 1:
        #     count = 0
        #     while count < self._timeout:
        #         # status: gripper is stopped
        #         if self._gripper_status.gSTA != 0:
        #             return self._gripper_status.gPOC
        #         sleep(0.1)
        #         count += 1

    def get_speed(self):
        return self._command.rSPA

    def get_torque(self):
        return self._command.rFRA

