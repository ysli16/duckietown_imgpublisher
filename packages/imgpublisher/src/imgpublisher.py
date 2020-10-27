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
        # construct publisher
        self.pub = rospy.Publisher('colordetector/image/compressed', CompressedImage, queue_size=10)

    def run(self,cap,bridge):
        # publish message every 1 second
        rate = rospy.Rate(5) # 1Hz
        while not rospy.is_shutdown():
            ret, frame = cap.read()
            img_msg=bridge.cv2_to_compressed_imgmsg(frame)
            rospy.loginfo("Get an image...")
            self.pub.publish(img_msg)
            rate.sleep()

if __name__ == '__main__':
    # create the node
    node = ImagePublisher(node_name='imgpublisher')
    #extract image
    cap = cv2.VideoCapture(2)
    bridge = CvBridge()
    # run node
    node.run(cap=cap,bridge=bridge)
    # keep spinning
    rospy.spin()
