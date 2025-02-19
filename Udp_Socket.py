import os
import socket
import rclpy
from rclpy.node import Node
from udp_msgs.msg import UdpPacket  
from builtin_interfaces.msg import Time 

class UdpForwarder(Node):
    def __init__(self):
        super().__init__('udp_forwarder')
        
        self.publisher = self.create_publisher(UdpPacket, '/etsi_its_conversion/udp/in', 10)
        self.get_logger().info("UDP forwarder node initialized.")

    def publish_message(self, data, src_ip, src_port):
     
        msg = UdpPacket()

      
        msg.header.stamp = self.get_clock().now().to_msg()  
        msg.header.frame_id = "CAM_Msg"  

      
        msg.address = src_ip
        msg.src_port = src_port

       
        msg.data = list(data)  

    
        self.publisher.publish(msg)
        self.get_logger().info(f"Published UdpPacket: {msg.data} from {src_ip}:{src_port}")

def main(args=None):
    rclpy.init(args=args)

    #UDP_IP = "192.192.192.120"  
    #UDP_PORT = 9002             
    UDP_IP = os.getenv('UDP_IP', '0.0.0.0')  # Default to 0.0.0.0 if not set
    UDP_PORT = int(os.getenv('UDP_PORT', '9002'))  # Default to 9002 if not set
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, UDP_PORT))

  
    udp_forwarder = UdpForwarder()
    udp_forwarder.get_logger().info(f"Listening for UDP packets on {UDP_IP}:{UDP_PORT}...")

    try:
        while rclpy.ok():
           
            data, addr = sock.recvfrom(1024)  
            src_ip, src_port = addr

         
            udp_forwarder.get_logger().info(f"Received message: {data.hex()} from {src_ip}:{src_port}")

         
            udp_forwarder.publish_message(data, src_ip, src_port)

            
            rclpy.spin_once(udp_forwarder, timeout_sec=0)  
    except KeyboardInterrupt:
        udp_forwarder.get_logger().info("Shutting down UDP forwarder node.")
    finally:
        
        sock.close()
        udp_forwarder.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()