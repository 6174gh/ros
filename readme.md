Robotic Operating System

# EdX Course

## Week 0

1. Uses noetic version of ROS
2. Uses Readonly Singularity conatiner
3. Source neotic only once

```
source /opt/ros/noetic/setup.bash
```

4. Source workspace evrytime you load the terminal

```
source <path_to_your_workspace>/devel/setup.bash
(Eg:)
source $HOME/hrwros_ws/devel/setup.bash
```

## Week 1

### ROS/Catkin Workspace

ROS workspace (catkin workspace) consists of different subspaces. A workspace is a folder to organize ROS project files. ROS uses catkin, which is a build tool to compile source files into binary files. Your code goes into the src workspace folder and catkin manages the other ones. A catkin ROS workspace contains three main spaces:

src space: contains source code, this will be your main work folder
devel space: contains setup files for the project ROS environment
Contains all binaries from src space
build space: contains the compiled binary files
install space: -

```bash
$ mkdir -p new_ros_ws/src
$ cd new_ros_ws
$ source opt/ros/noetic/setup.bash
$ catkin init
$ catkin build
```

### ROS Packages

ROS packages reside in the 'src' space. In ROS, software is organised in ROS packages. A ROS package typically contains the following things:

- CMakeList.txt
- package.xml (These two files indicate that the folder is a ROS package file)
- scripts/ (This folder contains all Python scripts.)
- src/ (This folder contains all C++ source files.)

```
# To create a new ROS package, use catkin:
(create source files of package)
$ cd <path_to_ros_ws>/src
$ catkin_create_pkg hrwros_week2 std_msgs

(or install binaries of packages)
$ rosdep install <package_name>
Install all ROS package dependencies in one command:
$ cd <path_to_ros_ws>/src
$ rosdep install --from-paths . --ignore-src -y
```

### Node

These are software processes that do 'stuff' (e.g. process data, command hardware, execute algorithms).

node can publish to a topic and read from a topic

'/' before node and topic names

```
rosnode list // List actively running Nodes
rqt_graph //Graphical representation of nodes and how they communicate
rosnode info <node_name> //node specific info
```

### Nodes - Publisher

A ROS node that generates information is called a publisher. A publisher sends information to nodes via topics. With robotics often these publishers are connected with sensors like cameras, encoders, etc.

### Nodes - Subscriber

A ROS node that receives information is called a subscriber. It's subscribed to information in a topic and uses topic callback functions to process the received information. With robotics, subscribers typically monitor system states such as triggering an alert when the robot reaches joint limits.

And the subscriber node "reads from" one or more ROS topics with each subscription processed via a respective callback function.



### Topic

Transport between nodes
information oragnized as data structure
information super highway

```
rostopic list //List all topics
rostopic info <topic_name> //List details of a topic
rostopic echo <topic_name> // COntinously print content to terminal string
```

```
roslaunch hrwros_week1 hrwros_welcome.launch
```

### ROS File System

ROS Workspace
ROS packages - Organize different functional modules

Devolop own application

### ROS Message Types

Nodes can process and share information through topics. The information they pass through these topics needs to be structured in some way, to make it actually usable. Such a structure is known as a data structure. In ROS, we can abstract these data structures as ROS message types. Common data structures in ROS are for example floats, integers, and strings.

In ROS, we can easily combine multiple data structures using derived message types. For example, to represent a position in 3D space we will need 3 floating point values: X, Y and Z. The derived message type will then be a struct of three floating point numbers: {float x, float y, float z}.

These (derived) message types are defined in message files. These message files are typically located in <ros_package_name>/msg, with the filename <NewMessageType>.msg. 

> Example: Ultrasound distance sensor.

We want to construct a new message type called SensorInformation. It should contain:

    A ROS message type for interfacing with distance sensors
    A string containing the manufacturer name
    An unsigned integer containing the sensor part number

Create the following file: $HOME/hrwros_ws/src/hrwros/hrwros_msgs/msg/SensorInformation.msg.


```text
# Example message file
sensor_msgs/Range sensor_data # placeholder for the ROS message type for interfacing with distance sensors
string maker_name             # placeholder for manufacturer name
uint32 part_number            # placeholder for part number of the sensor
```
We can see something really interesting here: We use an already derived message, sensor_msgs/Range, and simply add a string and an integer to it. So we can create new message types using already existing derived message types! This idea of stacking is really useful in ROS, since you can easily re-use what already exists. So in the above example, the sensor_msgs/Range already contains everything we need from the range sensor itself, and we only add the maker name and the part number.
First, navigate to the folder where ROS message types are defined:


```
$ roscd hrwros_msgs
$ cd msg
```
Then, create the messagefile:
$ touch SensorInformation.msg

You can see all created message types by typing
$ rosmsg show sensor_msgs/
and hitting the Tab key.

Since we will need the Range type, enter
$ rosmsg show sensor_msgs/Range
and you will see what the Range message type consists of.

In the following example, we will create our own message type.

    Create the file and contents as shown below:
        Detail the data types the message type will contain
        And then some comments detailing the data entries
    Make sure to add the name to the add_message_files section in the CMakeLists.txt file
    Finally, run the catkin build command

### Building First ROS Application

### Publishing node and subscriber with custom message type

### Nodes - Service

1. Request - Response Communication

```
rosservice list
rosservice call
```

'---' indicate demarkation
service server and service client

Block program flow
Useful in sequential behaviour

Services are defined in the same package as messages,

### Nodes - Action


We don't always want blocking execution. ROS Actions allow non-blocking execution. This way, multiple things can happen at the same time. They are a generalized request-response system (as for services): a client-server infrastructure. Actions are defined by three message types:

    A goal (request),
    The result (response),
    And feedback.

There are a few ROS commands to interact with actions:

Generate action messages manually: 
$ rosrun actionlib_msgs genaction.py <path_to_action_file>
Show the contents of an action message: 
$ rosmsg show <stack_name>_msgs/<ActionMessage>

ROS actions have a few functions available to process requests:

    The goalCallback function processes a goal request.
    Goal statuses: ACTIVE, SUCCEEDED, ABORTED.

Nomenclature:

    Action server: A ROS node that advertises an action, so that other nodes can request action goals to be processed.
    Action client: A ROS node that sends goal requests to the action server.

Code example

Here, we will show the general structure of an action file.

Requirement: Counter with a 1s delay between each increment.

Goal message: Number to count up to (uint32)
Result message: A status message (string)
Feedback message: The number of counts completed (uint32)
```
uint32 num_counts     # Goal field
---                   # Separator
string result_message # Result field
---                   # Separator
uint32 counts_elapsed # Feedback field
```


The action generator script displays 7 actions:

    Specified actions:

1) CounterWithDelayFeedback
2) CounterWithDelayGoal
3) CounterWithDelayResult

    Additional actions which are used internally by the actionlib package:

4) CounterWithDelayActionFeedback
5) CounterWithDelayActionGoal
6) CounterWithDelayAction
7) CounterWithDelayActionResult

CounterWithDelayAction.msg is an aggregation of the other action messages. This is the action type of our action client

The action client code is something that we as users develop to leverage the facilities of the actionlib ROS package. 

Sent goals are registered by the action server and the actionlib package. The package requires additional information which is CounterWithDelayAction.msg.

Goal contains:

    Timestamp and header info
    Unique goal identifier
    Goal message

Action Result contains:

    Timestamp and header info
    Different states the goal can be in

Feedback contains:

    Timestamp and header info
    Different states the goal can be in
    Feedback message

Action server topics

    Feedback topic is published by the action server an has action feedback message type
    Action server subscribers to the cancel topic and is of the GoalID type

Attention!

    Simple Action Server/Client.
    Non-blocking execution of ONE goal at a time.
    New goal to the same action server will pre-empt an active goal. Meaning that the active goal is completed first before a new goal will be processed.

