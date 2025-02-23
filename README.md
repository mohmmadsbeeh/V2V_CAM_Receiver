# 🚗 V2V CAM Receiver

This repository contains a Dockerized ROS 2 node for testing the [Autoware V2V CAM Publisher Node](https://github.com/mohmmadsbeeh/autoware_v2v_cam_publisher_node/). It integrates the ETSI ITS Messages conversion node from the [ika-rwth-aachen/etsi_its_messages](https://github.com/ika-rwth-aachen/etsi_its_messages/tree/main) repository and includes a UDP socket for receiving and forwarding CAM (Cooperative Awareness Message) data.

## 📌 Overview

The purpose of this repository is to provide a testing environment(Receiver Side) for the Autoware V2V CAM Publisher Node. It includes:
- A **UDP socket** for receiving CAM messages.
- The **ETSI ITS Messages conversion node** to process and forward the received messages.
- A Dockerized setup for easy deployment and testing.

For more details about the ETSI ITS Messages conversion node, visit the [ika-rwth-aachen/etsi_its_messages](https://github.com/ika-rwth-aachen/etsi_its_messages/tree/main) repository.

---

## 🏗️ Prerequisites

Ensure you have the following installed:

- 🐳 **Docker** → [Install Docker](https://docs.docker.com/get-docker/)  
- 🦭 **ROS 2 Humble** → [Install ROS 2](https://docs.ros.org/en/humble/)  

---

## Usage

### 🔹 1️⃣ Build the Docker Image

To build the Docker image, run the following command:

```bash
docker build -t V2V_CAM_Receiver .
```

## 🚀 Run the Docker Container

### 📡 **Option 1: Use Host Network (Recommended for Testing)**  
To run the container with the **host's network stack** (useful for testing with the same IP address):

```bash
docker run -it --rm --network host V2V_CAM_Receiver
```
### ⚙️ Option 2: Custom IP and Port

```bash
docker run -it --rm -e UDP_IP=192.192.192.120 -e UDP_PORT=9002 V2V_CAM_Receiver
```
> 📝 **Note:** Replace `192.192.192.120` and `9002` with your desired IP address and port.

---
## 📂 Repository Structure

- 📄 **`Dockerfile`** → Contains the Docker configuration for building the image.  
- 📝 **`Udp_Socket.py`** → Python script for receiving UDP packets and forwarding them as ROS 2 messages.  
- 📑 **`params.yml`** → Configuration file for the ETSI ITS Messages conversion node.  

---
## 🙌 Acknowledgments
 
- 🔗 [ika-rwth-aachen/etsi_its_messages](https://github.com/ika-rwth-aachen/etsi_its_messages/tree/main)  

---
