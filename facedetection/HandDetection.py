import mediapipe as mp
import cv2,math
import mediapipe as mp

def is_straight(joints):
    angle = [math.atan2(joints[i+1][1] - joints[i][1], joints[i+1][0] - joints[i][0]) for i in range(3)]
    if abs(angle[0] - angle[1]) > math.pi/5 or abs(angle[2]-angle[1]) > math.pi/5:
        return False
    return True


def check_hand_info(hand_info):
    if hand_info[0]:
        straight_l = [is_straight(hand_info[0][4*i+1:4*i+5]) for i in range(5)]
        if straight_l == [False,True,True,False,False]:
            return 'yes'
        elif straight_l[1:] == [False,True,True,True]:
            return 'ok'
    if hand_info[1]:
        straight_r = [is_straight(hand_info[1][4*i+1:4*i+5]) for i in range(5)]
        if straight_r == [False,True,True,False,False]:
            return 'yes'
        elif straight_r[1:] == [False,True,True,True]:
            return 'ok'
    return 'else'


def get_hand_info(image):
    hands = mp.solutions.hands.Hands(static_image_mode=True, max_num_hands=2)
    h,w,_ = image.shape
    results = hands.process(image)
    if results.multi_hand_landmarks:
        hand_info = [[(pos.x*w,pos.y*h) for pos in handLms.landmark] for handLms in results.multi_hand_landmarks ]
        if len(hand_info) < 2:
            hand_info.append([])
    else:
        hand_info = [[],[]]
    hands.close()
    return hand_info


def draw(image):
    mp_drawing = mp.solutions.drawing_utils
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(static_image_mode=True,
                           max_num_hands=2)
    img = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    results = hands.process(img)
    img = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                img, hand_landmarks, mp_hands.HAND_CONNECTIONS)
    cv2.imshow('xjt',cv2.resize(img,(650,1000)))
    cv2.waitKey(0)
    cv2.destroyAllWindows()
def get_hand_gesture(image):
    return check_hand_info(get_hand_info(image))

if __name__ == '__main__':
    img = cv2.imread('./output/cch yes.jpg')
    draw(img)
    print(get_hand_gesture(cv2.cvtColor(img,cv2.COLOR_BGR2RGB)))

