#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 12:38:04 2017

@author: apple
"""
import time,os
a=["L     ZZZZZZ N    N"]#感谢马奇云同学指出字符串和列表的区别
b=["L         Z  N   NN"]
c=["L        Z   N  N N"]
d=["L       Z    N N  N"]
e=["L      Z     NN   N"]
f=["LLLLL ZZZZZZ N    N"]

alist=[a,b,c,d,e,f]
i=0
while i<6 :
    print(alist[i][0])
    i=i+1
    time.sleep(1)
t=2
while t<15:
    os.system('cls')
    for j in (a,b,c,d,e,f):
        j.insert(0," ") 
    i=0
    while i<6 :
        for k in range(t):
            print(alist[i][k],end='')
        print("\r")#感谢马奇云同学指导理清此处各个循环的关系 
        i=i+1
    time.sleep(1)
    t=t+1
