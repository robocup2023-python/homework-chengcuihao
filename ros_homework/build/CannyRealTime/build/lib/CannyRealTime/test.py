import cv2,time

# 打开视频文件
cap = cv2.VideoCapture('resource/output.mp4')

# 检查视频是否成功打开
if not cap.isOpened():
    print("无法打开视频文件")
    exit()

# 读取并显示视频帧
while True:
    # 逐帧读取视频
    ret, frame = cap.read()
    time.sleep(0.05)
    # 如果视频读取完毕，退出循环
    if not ret:
        break

    # 在窗口中显示视频帧
    cv2.imshow('Video', frame)
    
    # 按下 'q' 键退出循环
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放视频对象和关闭窗口
cap.release()
cv2.destroyAllWindows()