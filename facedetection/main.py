from FaceDetection import get_feature_label
from HumanSegmentation import human_segmentation
from insightface.app import FaceAnalysis
import time, torch, cv2
from concurrent.futures import ThreadPoolExecutor

def load_yolo():
    yolo_model = torch.hub.load('../yolov5/yolov5', 'custom','../yolov5/yolov5/weights/yolov5s.pt',source='local')
    if torch.cuda.is_available():
        yolo_model.to('cuda')
    yolo_model.classes=[0]
    return yolo_model

def params_init(files,target_file):
    # hands在进行多线程时process函数内部有些临时变量可能会变化,导致手势出来同一结果,因此不能只创建一个实例了
    app = FaceAnalysis()
    app.prepare(ctx_id=-1, det_size=(640, 640),det_thresh=0.5)
    feature, label = get_feature_label(files, app)
    return app,feature, label, cv2.imread(target_file)

if __name__ == '__main__':
    st = time.time()
    files = ['./imgs/cch.jpg', './imgs/xjt.jpg', './imgs/wjb.jpg']
    target_file = './imgs/group2.jpg'
    executor = ThreadPoolExecutor()
    future1 = executor.submit(load_yolo)
    future2 = executor.submit(params_init,files,target_file)
    app,feature,label,target_img = future2.result()
    yolo_model = future1.result()
    human_segmentation(yolo_model,target_img,feature,label,app,5)
    print('Done!, time cost: %.3f'%(time.time()-st))

