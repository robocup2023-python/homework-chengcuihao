import insightface
import cv2,os
import numpy as np
from insightface.app import FaceAnalysis
from concurrent.futures import ThreadPoolExecutor, as_completed


def  get_feature_label(paths,detector):
    features = np.zeros((len(paths),512))
    name_list = ['']*len(paths)
    thread_list = []
    with ThreadPoolExecutor(max_workers=5) as t:
        for path in paths:
            thread_list.append(t.submit(_get_feature_label,path,detector))
        for index,future in enumerate(as_completed(thread_list)):
            features[index],name_list[index] = future.result()
    return features, name_list

def _get_feature_label(path,detector):
    name = os.path.basename(path)[:-4]
    feature = get_face_feats(cv2.imread(path),detector)
    return feature, name


def get_face_feats(img,detector):
    faces = detector.get(img)
    return np.array([face.normed_embedding for face in faces], dtype=np.float32)

def draw(img):
    app = FaceAnalysis()
    app.prepare(ctx_id=-1, det_size=(640, 640),det_thresh=0.5)
    faces = app.get(img)
    rimg = app.draw_on(img, faces)
    cv2.imshow('check',cv2.resize(rimg,(1320,960)))
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    img = cv2.imread('./imgs/group2.jpg')
    draw(img)
