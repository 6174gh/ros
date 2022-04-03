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

It will contain the following:
sensor_msgs/Range sensor_data
string maker_name
uint32 part_number

We can see something really interesting here: We use an already derived message, sensor_msgs/Range, and simply add a string and an integer to it. So we can create new message types using already existing derived message types! This idea of stacking is really useful in ROS, since you can easily re-use what already exists. So in the above example, the sensor_msgs/Range already contains everything we need from the range sensor itself, and we only add the maker name and the part number.
