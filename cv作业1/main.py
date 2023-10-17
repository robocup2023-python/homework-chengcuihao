import cv2
import numpy as np
from matplotlib import pyplot as plt

def Gaussian_distribution(x,y,sigma=1):
    return np.exp(-(x**2+y**2)/sigma**2)/(2*np.pi*sigma**2)



def Gauss_filter(n,sigma=1):
    gauss_filter = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            gauss_filter[i,j] = Gaussian_distribution(i-n//2,j-n//2,sigma=sigma)
    gauss_filter = gauss_filter / np.sum(gauss_filter)
    return gauss_filter

def Visualize_filter():
    fig = plt.figure() 
    for index,sigma in enumerate((0.5,1,3,5)): 
        plt.subplot(2,2,index+1)
        gf = Gauss_filter(9,sigma)
        ax = fig.add_subplot(2,2,index+1, projection='3d')
        X,Y = np.meshgrid(range(-4,5),range(-4,5))
        ax.contour3D(X,Y,gf,50,cmap='viridis')
        ax.set_xlabel('x')  
        ax.set_ylabel('y')
        ax.set_zlabel(f"sigma={sigma}")
    plt.tight_layout()
    plt.show()

def Convolution(img, filter, padding=None,show_padding=False):
    height,width = img.shape[0],img.shape[1]
    kernel_size = filter.shape[0]
    res = np.zeros(img.shape,dtype='uint8')
    pad_img = np.zeros((height+kernel_size-1,width+kernel_size-1,3),dtype='uint8')
    pad_num = kernel_size//2
    pad_img[pad_num:pad_img.shape[0]-pad_num,pad_num:pad_img.shape[1]-pad_num,:] = img
    if padding == 'reflect':
        pad_img[:pad_num,:,:] = pad_img[2*pad_num:pad_num:-1,:,:]
        pad_img[-pad_num:,:,:] = pad_img[-pad_num-1:-2*pad_num-1:-1,:,:]
        pad_img[:,:pad_num,:] = pad_img[:,2*pad_num:pad_num:-1,:]
        pad_img[:,-pad_num:,:] = pad_img[:,-pad_num-1:-2*pad_num-1:-1,:]
    elif padding == 'warp':
        pad_img[:pad_num,:,:] = pad_img[-2*pad_num:-pad_num,:,:]
        pad_img[-pad_num:,:,:] = pad_img[pad_num:2*pad_num,:,:]
        pad_img[:,:pad_num,:] = pad_img[:,-2*pad_num:-pad_num,:]
        pad_img[:,-pad_num:,:] = pad_img[:,pad_num:2*pad_num,:]
    if show_padding:
        if not padding:
            padding = 'zero'
        cv2.imshow(padding,pad_img)
    for i in range(height):
        for j in range(width):
            for k in range(3):
                res[i,j,k] = np.sum(pad_img[i:i+kernel_size,j:j+kernel_size,k]* filter)
    return res

def Compare_with_different_filter(img):
    f1 = Gauss_filter(31,1)
    f2 = Gauss_filter(3,3)
    f3 = Gauss_filter(31,1)
    cv2.imshow('3x3, sigma=1', Convolution(img,f1,padding='warp'))
    cv2.imshow('3x3, sigma=3', Convolution(img,f2))
    cv2.imshow('9x9, sigma=1', Convolution(img,f3))
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def show_padding(img):
    f1 = Gauss_filter(31,1)
    Convolution(img,f1,show_padding=True)
    Convolution(img,f1,padding='warp',show_padding=True)
    Convolution(img,f1,padding='reflect',show_padding=True)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    img = cv2.imread('./img.jpg')
    Visualize_filter()
    Compare_with_different_filter(img)
    show_padding(img)

