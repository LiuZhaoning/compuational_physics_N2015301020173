#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 16:57:59 2017

@author: apple
"""

import matplotlib.pyplot as plt
import numpy as np
w_0=0
Theta_0=float(0.200000)
l=9.8
q=0.5
Omega_D=0.667
F_D=float(1.2)
dt=0.04
t=0
i=0
w=w_0
Theta=Theta_0
E=0.5*l**2*(w**2+9.8/l*Theta**2)
Theta_list=[Theta_0]
t_list=[t]
E_list=[E]
while i<1500:
    w=w-(9.8/l*np.sin(Theta)+q*w-F_D*np.sin(Omega_D*t))*dt
    Theta=Theta+w*dt
    if Theta>np.pi:
        Theta=Theta-np.pi*2
    if Theta<-np.pi:
        Theta=Theta+np.pi*2  
    E=0.5*l**2*(w**2+9.8/l*Theta**2)
    t=t+dt
    i +=1
    Theta_list.append(Theta)
    t_list.append(t)
    E_list.append(E)
plt.plot(t_list,Theta_list,label="$F_D=1.2$")
plt.ylabel('$\Theta/radians$')
plt.xlabel('time/s')
plt.title('$\Theta versus time$')
plt.grid(True)
plt.legend(loc='2')
plt.show()
plt.plot(t_list,E_list,label='$F_D=1.2$')
plt.ylabel('E/Joules')
plt.xlabel('time/s')
plt.title('E versus time')
plt.grid(True)
plt.legend(loc='2')
plt.show()
print(max(E_list))