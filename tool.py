#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import cv2
import numpy as np
import os

def save_img(img,path,i):
    address = os.path.join(path,str(i)) + '.jpg'
    # print(address)
    cv2.imwrite(address,img)

def cut_frame(vpath,spath,frameFrequency=2):
    """
    视频抽帧保存图片
    :param vpath:视频路径
    :param spath: 保存路径
    :param frameFrequency:帧间隔
    :return:
    """
    camera = cv2.VideoCapture(vpath)
    times = 0
    current = 1
    while True:
        times += 1
        res, image = camera.read()
        if not res:
            # print('not res , not image')
            break
        if times % frameFrequency == 0:
            save_img(image,spath,current)
            current += 1
            # cv2.imwrite(outPutDirName + str(times) + '.jpg', image)
            # print(outPutDirName + str(times) + '.jpg')

if __name__ == '__main__':
    # save_img(0,'asd',2)
    # cut_frame(r'H:\SFMData\corridor\video.mp4',r'H:\SFMData\corridor\images')
    # cut_frame(r'H:\SFMData\toilet\video.mp4', r'H:\SFMData\toilet\images')
    cut_frame(r'H:\SFMData\bathroom\video.mp4', r'H:\SFMData\bathroom\images',3)