# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 03:12:42 2020

@author: Dell
"""


from project_micro_2 import *
import numpy as np

L=0.000180

w=0.000007

J=13.1

max_disp, Thatmax = update_parameters(L, w, J)

# L1=[]
# Disp=[]
# w1=[]
# Disp1=[]

# for L in np.arange(0.000150, 0.000200, 0.000005):
#     L1=np.append(L1, L)
#     max_disp, Thatmax = update_parameters(L, 0.000010, 13.1)
#     Disp=np.append(Disp, max_disp)
#     print(L)
#     print(max_disp)
   

# for w in np.arange(0.000005, 0.000015, 0.000001):
#     w1=np.append(w1, w)
#     max_disp1, Thatmax1 = update_parameters(0.000180, w, 13.1)
#     Disp1=np.append(Disp1, max_disp1)
#     print(w)
#     print(max_disp1)  
   
# for iT in np.arange(293, 310, 3):   
#     for width in np.arange(0.000005, 0.000010, 0.0000005):
#         max_disp = update_parameters(0.000175, width, iT)
#         print(iT)
#         print(width)
#         print(max_disp)




# import matplotlib.pyplot as plt
# from matplotlib.ticker import AutoMinorLocator

# fig, ax1 = plt.subplots()


# ax1.plot(L1, Disp, color="r") # regular plot (red)
# ax1.set_xlabel('x')

# ax2 = ax1.twiny() # ax1 and ax2 share y-axis
# ax2.plot(w1, Disp1, color="b") # semilog plot (blue)
# ax2.set_xlabel('semilogx')

# plt.show()