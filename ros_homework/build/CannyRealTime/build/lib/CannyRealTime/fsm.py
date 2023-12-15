import cv2
import numpy as np
import rclpy
from rclpy.node import Node
from image_msg.msg import CameraImage


class CameraSubscriber(Node):

    def __init__(self):
        super().__init__('fsm')
        self.subscription = self.create_subscription(
            CameraImage(),
            'CameraImage',
            self.canny_callback,
            10
        )
        
    def canny_callback(self, msg):
        data = np.array(msg.data,dtype='uint8')
        data = data.reshape(msg.height,msg.width,msg.channel)
        print(data.shape)
        img = cv2.cvtColor(data,cv2.COLOR_BGR2GRAY)
        img = cv2.Canny(img, 75, 150)
        cv2.imshow('canny',img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            return
    
    def destroy_node(self):
        cv2.destroyAllWindows()
        super().destroy_node()


def main(args=None):
    rclpy.init(args=args)
    fsm = CameraSubscriber()
    rclpy.spin(fsm)
    fsm.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()    
