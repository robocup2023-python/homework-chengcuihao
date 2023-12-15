import cv2,os
import rclpy
from rclpy.node import Node
from image_msg.msg import CameraImage


class CameraPublisher(Node):

    def __init__(self):
        super().__init__('camera')
        self.publisher_ = self.create_publisher(CameraImage,'CameraImage',10,)
        self.fps = 30
        self.timer = self.create_timer(1/self.fps,self.publish_image)
        location = os.path.abspath(__file__).split('/')
        video_path = '/'.join(location[:-7]) + '/src/CannyRealTime/resource/output.mp4'
        self.capture = cv2.VideoCapture(video_path)
        print(video_path)
        if not self.capture.isOpened():
            print('无法打开视频')
        self.i = 0 

    def publish_image(self):
        ret,frame = self.capture.read()
        if not ret:
            self.get_logger().info("Vedio has been played")
            return
        msg = CameraImage()
        msg.data = frame.reshape(-1).tolist()
        msg.fps = self.fps
        msg.height,msg.width,msg.channel = frame.shape
        self.publisher_.publish(msg)
        self.i += 1
        self.get_logger().info('Publishing Image: %d'%(self.i))

    def destroy_node(self):
        self.capture.release()
        cv2.destroyAllWindows()
        super().destroy_node()

def main(args=None):
    rclpy.init(args=args)
    camera = CameraPublisher()
    rclpy.spin(camera)
    camera.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

