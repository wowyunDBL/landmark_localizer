# landmark_localizer

## Network Configuration
1. open terminal and type
```sh
$ echo "export ROS_MASTER_URI=http://192.168.0.101:11311" >> ~/.bashrc
$ echo "export ROS_HOSTNAME=192.168.0.103" >> ~/.bashrc
```
.0.101 is IP for host  
.0.103 is IP for slaver

2. Source the bashrc with below command.
```sh
$ source ~/.bashrc
```

3. return rosmsg by modifing this
```sh
$ sudo echo "192.168.0.101 ${ROS_MASTER_NAME}" >> /etc/hosts
```

## Seup Software
```sh
$ pip install -r requirements.txt
$ sudo apt install python-pip
```

## Execution
```sh
$ bash ./demo.sh
```

## rosbag filter (for those who don't need RGBD image)
rosbag filter ChiaY_outerHalf_2021-08-17-17-17-10.bag lighter_ChiaY_outerHalf_2021-08-17-17-17-10.bag "topic=='/imu_filter/rpy/filtered' or topic=='/outdoor_waypoint_nav/odometry/filtered_map' or topic=='/outdoor_waypoint_nav/odometry/filtered' or topic=='/tf'"


## working tree
├── CMakeLists.txt
├── demo.sh
├── include
│   └── landmark_localizer
├── install_librealsense.sh
├── package.xml
├── README.md
├── release-notes.md
├── requirements.txt
├── scripts
│   ├── cb_pose.py
│   └── cb_topic2npy.py # file_naming: timestampSecs%1000+timestampNSecs/1e6
└── src

