因为在wsl上装的ros2,但wsl2没法使用本机的摄像头,试了试用ffmpeg等用网络传输视频流但一直连接不上本机,所以只好出此下策用以录制好的视频来代替摄像头了,把代码中
```Python
self.capture = cv2.VideoCapture(video_path)
# 替换成
self.capture = cv2.VideoCapture(0)
```
即可得到摄像头的实时效果