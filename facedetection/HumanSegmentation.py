import cv2,torch,copy
import numpy as np
from FaceDetection import *
from HandDetection import get_hand_gesture
from concurrent.futures import ThreadPoolExecutor, as_completed


def human_segmentation(model, image, feature, label, face_dect, persons=3, margin=5):
    """
    先用yolo框出人,然后立即进行FaceDetection,并与数据集进行比较,查出每个人脸对应是谁,同时进行HandDetection
    ,再写入信息
    model: yolo的实例
    image: 待检测图片
    feature: 预先存储人脸特征
    label:对应feature的人名
    face_dect: insightface的实例
    """
    result = model(image)
    image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    human_pos = np.array(result.xyxy[0].cpu())[:persons]
    name_list = [''] * len(human_pos)
    gesture_list = [''] * len(human_pos)
    thread_list = []
    with ThreadPoolExecutor(max_workers=persons) as t:
        for index,items in enumerate(human_pos):
            thread_list.append(
                t.submit(_human_segmentation, image, feature, label, items, index, face_dect, margin))
        for future in as_completed(thread_list):
            name,gesture,index = future.result()
            name_list[index], gesture_list[index] = name,gesture
    image = cv2.cvtColor(image,cv2.COLOR_RGB2BGR)
    for index, (x1, y1, x2, y2, conf, cls) in enumerate(human_pos):
        if name_list[index] == 'others':
            continue
        cv2.rectangle(image, (int(x1 - margin), int(y1 - margin)), (int(x2 + margin), int(y2 + margin)), (255, 0, 0), 4)
        cv2.putText(image, f'{name_list[index]},{gesture_list[index]}', (int(x1 - margin), int(y1 - margin) - 2),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 2)
    cv2.imwrite('./output/ultimate.jpg', image)


def _human_segmentation(image, feature, label, human_pos,index, face_dect, margin=5):
    subimg = image[int(max(0,human_pos[1] - margin)):int(human_pos[3] + margin), \
             int(max(0,human_pos[0] - margin)):int(human_pos[2] + margin), :]
    feat = get_face_feats(subimg, face_dect)
    if len(feat) == 0:
        return 'others', '',index
    sims = np.dot(feat, feature.T)
    print(sims)
    if np.max(sims) < 0.4:
        return 'others', '',index
    name = label[np.argmax(sims)]
    # 同时去检测手势
    gesture = get_hand_gesture(subimg)
    cv2.imwrite(f'./output/{name} {gesture}.jpg', cv2.cvtColor(subimg,cv2.COLOR_RGB2BGR))
    return name, gesture,index

if __name__ == '__main__':
    yolo_model = torch.hub.load('../yolov5/yolov5', 'custom','../yolov5/yolov5/weights/yolov5s.pt',source='local')
    if torch.cuda.is_available():
        yolo_model.to('cuda')
    yolo_model.classes=[0]
    image = cv2.imread('./imgs/group2.jpg')
    result = yolo_model(image)
    margin=5
    human_pos = np.array(result.xyxy[0].cpu())[:5]
    for index, (x1, y1, x2, y2, conf, cls) in enumerate(human_pos):
        cv2.rectangle(image, (int(x1 - margin), int(y1 - margin)), (int(x2 + margin), int(y2 + margin)), (255, 0, 0), 4)
        cv2.putText(image, '%.3f'%conf, (int(x1 - margin), int(y1 - margin) - 2),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 2)
    cv2.imshow('222', cv2.resize(image,(1320,960)))
    cv2.waitKey(0)
    cv2.destroyAllWindows()