
FROM ros:humble

ENV ROS_DOMAIN_ID=123


RUN apt-get update && \
    apt-get install -y \
    python3-pip \
    ros-humble-etsi-its-messages \
    ros-humble-etsi-its-rviz-plugins \
    && rm -rf /var/lib/apt/lists/*


WORKDIR /src


COPY Udp_Socket.py /src/Udp_Socket.py


COPY params.yml /opt/ros/humble/share/etsi_its_conversion/config/params.yml


CMD ["bash", "-c", "source /opt/ros/humble/setup.bash && \
     python3 Udp_Socket.py & \
     ros2 launch etsi_its_conversion converter.launch.py"]