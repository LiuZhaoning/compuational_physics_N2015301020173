#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 19:03:38 2017

@author: apple
"""
import numpy as np
import matplotlib.pyplot as plt
Na0=input("please input Na0:")
Nb0=input("please input Nb0:")
Ta=input("please input Ta:")
Tb=input("please input Tb:")
Nat=Na0/100
Nbt=Nb0/100
Na=Na0
Nb=Nb0
dt=0.1
t=0
Na_list=[Na]
Nb_list=[Nb]
Na_ana=[Na0]
Nb_ana=[Nb0]
T=[0]
while Na>Nat or Nb>Nbt :
    Nb=Nb+(Na/Ta-Nb/Tb)*dt
    Na=Na-Na/Ta*dt
    t=t+dt
    Na_ana.append(Na0*np.exp(-t/Ta))
    if Ta<>Tb:
        Nb_ana.append((Nb0-Na0*Tb/(Ta-Tb))*np.exp(-t/Tb)+Tb*Na0/(Ta-Tb)*np.exp(-t/Ta))
    else:
         Nb_ana.append(Na0/Ta*t*np.exp(-t/Tb)+Nb0*np.exp(-t/Tb))
    Na_list.append(Na)
    Nb_list.append(Nb)
    T.append(t)  
plt.plot(T,Na_list)
plt.plot(T,Nb_list)
plt.plot(T,Na_ana)
plt.plot(T,Nb_ana)

