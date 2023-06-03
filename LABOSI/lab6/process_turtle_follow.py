#!/usr/bin/env python3
import rosbag
import sys
import math
import rospy

def calculateDistance(bag):
    dis=0
    is_first=0
    for(topic, msg, t) in bag.read_messages(topics=['/turtle1/pose']):
       if (is_first==0): 
           stari_x=msg.x
           stari_y=msg.y
           is_first=1
       dis=dis + math.sqrt(pow((msg.x - stari_x), 2) + pow((msg.y - stari_y), 2))
       stari_x=msg.x
       stari_y=msg.y
   
    return dis
    
def getDuration(bag):
    is_first=0
    for (topic, msg, t) in bag.read_messages(topics=['/turtle1/pose']):
        if (is_first==0):
            is_first=1
            first_time=t
        last_time=t
    return (last_time - first_time).to_sec()
    
def writeToAnotherBag(bag, resolution_x, resolution_y):
    counter=0
    bag2=rosbag.Bag('processed_follow.bag', 'w')
    
    for (topic, msg, t) in bag.read_messages():
        if (topic == '/turtle1/pose'):
            counter=counter+1
            topic=' /follower/pose'
            bag2.write(topic, msg, t)
        if (topic == '/mouse_position'):
            counter=counter+1
            topic='/mouse_positions_on_grandparents_computer'
            #changing the resolution
            msg.x = round(msg.x/ resolution_x * 800) 
            msg.y = round(msg.y/ resolution_y* 600) 
            bag2.write(topic, msg, t)
    return counter
    

if __name__ =='__main__':
    bagFile=sys.argv[1]
    bag = rosbag.Bag(bagFile)
    resolution_width=1842
    resolution_height=1000
    
    distance=calculateDistance(bag)        #calculating distance
    full_duration=getDuration(bag)         #calculating duration
    avg_velocity= distance/full_duration   #calculating avg velocity
    numOfMsgs=writeToAnotherBag(bag, resolution_width, resolution_height)
    
    print('Processing input bagfile: {}\nFollower turtle'.format(bagFile))
    print('    Covered distance: {:.2f} m'.format(distance))
    print('    Average velocity: {:.2f} m/s'.format(avg_velocity))
    print('Follow session duration: {:.2f} s'.format(full_duration))
    print('Wrote {} messages to processed_follow.bag'.format(numOfMsgs))
