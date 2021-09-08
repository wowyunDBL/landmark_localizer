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
$ bash ./demo.sh
```
