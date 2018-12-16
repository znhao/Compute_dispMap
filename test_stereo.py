# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 21:56:09 2018

@author: dell
"""

import stereo
from PIL import Image
from numpy import *
im_l = array(Image.open('t1.jpg'),'f')
im_r = array(Image.open('t2.jpg'),'f')

#开始偏移，设置步长
steps = 2
start = 0

#ncc的宽度(滑动窗口的宽度)
wid = 9

res = stereo.plane_Sweep_ncc(im_l,im_r,start,steps,wid)

import scipy.misc
scipy.misc.imsave('depth.png',res)