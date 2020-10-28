#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 21:50:04 2020

@author: yueshan
"""
#import os
import rospy
from duckietown.dtros import DTROS, NodeType
from sensor_msgs.msg import CompressedImage
import cv2
from cv_bridge import CvBridge

class ImagePublisher(DTROS):

    def __init__(self, node_name):
        # initialize the DTROS parent class
        super(ImagePublisher, self).__init__(node_name=node_name, node_type=NodeType.GENERIC)
        #extract image
        self.cap = cv2.VideoCapture(2)
        self.bridge = CvBridge()
        # construct publisher
        self.pub = rospy.Publisher('colordetector/image/compressed', CompressedImage, queue_size=1)

    def run(self):
        # publish message every 1 second
        rate = rospy.Rate(5) # 1Hz
        while not rospy.is_shutdown():
            ret, frame = self.cap.read()
            img_msg=self.bridge.cv2_to_compressed_imgmsg(frame)
            img_msg.header.stamp=rospy.Time.now()
            rospy.loginfo("Get an image...")
            self.pub.publish(img_msg)
            rospy.loginfo("Published to topic colordetector/image/compressed")
            rate.sleep()

if __name__ == '__main__':
    # create the node
    node = ImagePublisher(node_name='imgpublisher')

    # run node
    node.run()
    # keep spinning
    rospy.spin()
