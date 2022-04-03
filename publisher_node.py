## Node to publish a string topic.
import rospy # Ros specific python modules
from std_msgs.msg import String

def simplePublisher():
    simple_publisher = rospy.Publisher('topic_1', String, queue_size = 10) # Define ros object
    rospy.init_node('node_1', anonymous = False) #data only good if associated with a node
    rate = rospy.Rate(1) #Frequency of publishing
    
    # The string to be published on the topic.
    topic1_content = "my first ROS topic"
    
    while not rospy.is_shutdown():
    	simple_publisher.publish(topic1_content)
        rate.sleep() #Published at specified frequency

#Driver Code   
if __name__== '__main__':
    try:
        simplePublisher()
    except rospy.ROSInterruptException:
        pass