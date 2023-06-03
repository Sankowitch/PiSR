#!/usr/bin/env python3
import rospy
from math import cos, sin
from sensor_msgs.msg import LaserScan
from visualization_msgs.msg import Marker
from geometry_msgs.msg import Point


class Laserscan:
    def laser_callback(self, data):
        now = rospy.Time.now()
        marker = Marker()
        marker.type = Marker.POINTS
        marker.color.a = 1
        marker.scale.x = .3
        marker.scale.y = .3
        
        marker.header.stamp = now
        marker.header.frame_id = 'laserscan'
        marker.header = data.header
       
        index=0
        for datarange in data.ranges:
            ang_x = data.angle_min + data.angle_increment * index
            ang_y = data.angle_min + data.angle_increment * index
            point=Point()
            point.x=datarange * cos(ang_x)
            point.y=datarange * sin(ang_y)
            marker.points.append(point)
            index=index+1
            
        self.mark.publish(marker)
        
        

    def __init__(self):
        rospy.Subscriber('/scan', LaserScan, self.laser_callback)
        self.mark = rospy.Publisher('/point_position', Marker, queue_size=1)
        
        


if __name__ == "__main__": 
    rospy.init_node('pyclass')
    try:
        ne = Laserscan() 
        rospy.spin()
    except rospy.ROSInterruptException: 
        pass
