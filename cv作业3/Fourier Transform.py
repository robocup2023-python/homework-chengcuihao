import cv2
import matplotlib.pyplot as plt
import numpy as np


def uniform(img):
    ma,mi = np.max(img),np.min(img)
    res = np.array((img-mi)/(ma-mi)*256,dtype='uint8')
    return res

def FFT(img):
    img_cpx = np.fft.fft2(img)
    img_shift = np.fft.fftshift(img_cpx) # 中心化
    img_phase = np.angle(img_shift) # 相位图
    img_freq = np.abs(img_shift) # 频谱
    log_img_freq = np.log(img_freq)  
    return img_shift,img_freq,img_phase

def low_pass_filter(img, r=30):
    img_shift,_,_ = FFT(img)
    mask = np.zeros_like(img)
    center = (mask.shape[0]//2, mask.shape[1]//2)
    cv2.circle(mask, center, radius=r, color=1,thickness=-1)
    # mask[mask == 0] = 2 # 取反得高通道
    # mask -= 1
    img_shift *= mask
    img_reshift = np.fft.ifft2(np.fft.ifftshift(img_shift))
    # cv2.imshow('low_freq_filter',uniform(img_reshift.real))
    # cv2.imwrite('./high_pass_filter.jpg',uniform(img_reshift.real))


if __name__ == "__main__":
    img = cv2.imread('./img.jpg')
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # 转灰度
    cv2.imshow('origin',img)
    low_pass_filter(img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
