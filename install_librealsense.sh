#!/bin/bash
# Installs the Intel Realsense library librealsense on a Jetson Nano Development Kit
# The installation is from a RealSense Debian repository
# Copyright (c) 2016-19 Jetsonhacks 
# MIT License
# https://github.com/IntelRealSense/librealsense/blob/master/doc/installation_jetson.md

# referenced_site_yun: https://github.com/IntelRealSense/realsense-ros

# Register the server's public key:
sudo apt-key adv --keyserver keys.gnupg.net --recv-key F6E65AC044F831AC80A06380C8B3A55A6F3EFCDE || sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-key F6E65AC044F831AC80A06380C8B3A55A6F3EFCDE


# Ubuntu 18 is bionic
# sudo add-apt-repository "deb http://realsense-hw-public.s3.amazonaws.com/Debian/apt-repo bionic main" -u
sudo add-apt-repository "deb https://librealsense.intel.com/Debian/apt-repo $(lsb_release -cs) main" -u

# sudo apt-get install apt-utils -y
sudo apt-get install librealsense2-utils librealsense2-dkms librealsense2-dev -y

# uninstall >>> dpkg -l | grep "realsense" | cut -d " " -f 3 | xargs sudo dpkg --purge

# --- just install packages --- >>> sudo apt-get install ros-$ROS_DISTRO-realsense2-camera


