import cv2
import matplotlib.pyplot as plt
import numpy as np

def Sobel(img, require_grad=False):
    grad_x = cv2.Sobel(img,cv2.CV_64F,1,0)
    grad_y = cv2.Sobel(img,cv2.CV_64F,0,1)
    grad_mag = np.sqrt(np.square(grad_x)+np.square(grad_y)) # 计算梯度模长
    grad_dir = np.arctan2(grad_y,grad_x) # 计算梯度的角度
    if require_grad:
        return grad_x, grad_y, grad_mag, grad_dir
    else:
        return grad_mag, grad_dir

def visualization(img):
    mi,ma = np.min(img),np.max(img)
    new_img = np.array((img - mi)/ma * 255,dtype='uint8') # 将梯度值大小变化为图像灰度值输出
    cv2.imshow("gradient_magnitude",new_img)
    cv2.waitKey(0)
    # cv2.imwrite('./Sobel.jpg',new_img)

def NMS(arr,i,j,dir):
    maxi,maxj = arr.shape
    # 计算梯度方向对应的像素是否更大    
    if dir > 3*np.pi/8 or dir < -3*np.pi/8:
        dx,dy = [1,-1],[0,0]
    elif dir > np.pi/8:
        dx,dy = [1,-1],[1,-1]
    elif dir > -np.pi/8:
        dx,dy = [0,0],[1,-1]
    else:
        dx,dy = [1,-1],[-1,1]
    # 如果沿梯度方向有更大值则返回True，表示要去除
    for k in range(2):
        newx,newy = i+dx[k],j+dy[k]
        if newx > -1 and newx < maxi and newy > -1 and newy < maxj:
            if arr[newx,newy] > arr[i][j]:
                return True
    return False

def Canny(img, th1=50, th2=10): 
    img = cv2.GaussianBlur(img,(3,3),1) #高斯滤波减少噪音
    grad_mag, grad_dir = Sobel(img)
    mi,ma = np.min(grad_mag),np.max(grad_mag)
    # 将梯度直接拉成0-255的范围
    grad_mag = np.array((grad_mag - mi)/ma * 255,dtype='uint8')
    height,width = img.shape
    dx = [-1,-1,-1,0,0,1,1,1]
    dy = [1,0,-1,1,-1,1,0,-1]
    mask = np.zeros(img.shape)
    # 非极大抑制
    for i in range(height):
        for j in range(width):
            if grad_mag[i,j] < th2:
                grad_mag[i,j] = 0
                continue
            else:
                if NMS(grad_mag,i,j,grad_dir[i,j]):
                    grad_mag[i,j] = 0
                elif grad_mag[i,j] > th1:
                    mask[i,j] = grad_mag[i,j]

    # 边缘连接，要求3x3的范围内有确定的边缘点
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):  
            if grad_mag[i,j] > th2 and grad_mag[i,j] < th1:
                for k in range(8):
                    newx,newy = i+dx[k],j+dy[k]
                    if newx > -1 and newx < height and newy > -1 and newy < width:
                        if mask[newx,newy]:
                            mask[i,j] = grad_mag[i,j]
                            break
    return mask

def Histogram_average(img):
    # 手写实现灰度直方图均衡化
    height,width = img.shape
    # 用字典表示离散转换函数
    trans = {}
    arr = np.zeros(256)
    for i in range(height):
        for j in range(width):
            arr[img[i,j]] += 1
    arr /= height*width
    trans[0] = round(255*arr[0],0)
    # 统计分布函数并进行转换
    for i in range(1,256):
        arr[i] += arr[i-1]
        trans[i] = round(255*arr[i],0)

    new_img = np.zeros(img.shape,dtype='uint8')
    for i in range(height):
        for j in range(width):
                new_img[i,j] = trans[img[i,j]]
    return new_img

def Harris(img, th=None):
    # 手写Harris，阈值th会根据R的最大值调整
    img = cv2.GaussianBlur(img,(3,3),0.5)
    Ix,Iy,_, grad_dir = Sobel(img,require_grad=True)
    Ix2 = cv2.GaussianBlur(Ix**2,(3,3),1)
    Iy2 = cv2.GaussianBlur(Iy**2,(3,3),1)
    Ixy = cv2.GaussianBlur(Ix*Iy,(3,3),1)
    M = np.zeros((*img.shape,2,2))
    M[:,:,0,0] = Ix2
    M[:,:,0,1] = M[:,:,1,0] = Ixy
    M[:,:,1,1] = Iy2
    R = np.linalg.det(M) - 0.06*np.trace(M,axis1=-1,axis2=-2)
    th = np.max(R)*0.1
    mask = R > th
    print(np.mean(R),np.max(R))
    # NMS
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if mask[i,j] and NMS(R,i,j,grad_dir[i,j]):
                R[i,j] = 0
                mask[i,j] = False
    # 灰度转BGR并且将角点标为红色
    new_img = np.dstack((img,img,img))
    new_img[mask] = [0,0,255]
    return new_img
    

def CvHarris(img,block_size,sobel_size,k):
    # 调库使用的Harris
    res = cv2.cornerHarris(img, block_size, sobel_size,k)
    _,grad_dir = Sobel(img)
    th = 0.05*res.max()
    mask = res > th
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if mask[i,j] and NMS(res,i,j,grad_dir[i,j]):
                res[i,j] = 0
                mask[i,j] = False
    new_img = np.dstack((img,img,img))
    new_img[mask] = [0,0,255]
    return new_img

if __name__ == "__main__":
    img = cv2.imread('./img.jpg')
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # 转灰度
    # new_img = Canny(img)
    # visualization(new_img)
    # res = cv2.Canny(img,10,50)
    new_img = CvHarris(img,5,3,0.05)
    cv2.imshow('My_Harris',new_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
