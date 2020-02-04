# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 09:43:02 2019

@author: andy3
"""

import numpy as np
import matplotlib.pyplot as plt

N = 5
ind = np.arange(N)  # the x locations for the groups
width = 0.1       # the width of the bars

fig = plt.figure(figsize=(20, 10))
ax = fig.add_subplot(111)

Mode_1 = [0.0620, 0.0613, 0.0624,0.0614,0.0612]
rects1 = ax.bar (ind-width*1.5, Mode_1 , width, color='r')

Mode_2 = [0.0627,0.0614,0.0612,0.0616,0.0615]
rects2 = ax.bar(ind-width*0.5, Mode_2, width, color='g')

Mode_3= [0.0610,0.06149,0.0615,0.0615,0.0614]
rects3 = ax.bar(ind+width*0.5, Mode_3, width, color='b')

Mode_4 = [0.0617,0.0611,0.0613,0.0618,0.0630]
rects4 = ax.bar(ind+width*1.5, Mode_4, width, color='brown')
ax.set_xscale('linear',linewidth=0.001)

ax.set_ylabel('Validation_mean_square_error')
ax.set_xlabel('The_number_of_NN_unions')
ax.set_xticks(ind+width)
ax.set_xticklabels( ('50union', '100union', '150union','200union','250union') )
ax.legend(  (rects1[0], rects2[0], rects3[0], rects4[0]),('1_hidden_layer', '2_hidden_layer', '3_hidden_layer','4_hidden_layer'))


plt.title('Compare the relationship between Validation_mean_square_error and Model_structure')
plt.show()
