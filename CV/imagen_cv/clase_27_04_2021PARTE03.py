# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 09:58:25 2021

@author: INTEL
"""

import matplotlib.pyplot as plt
import  numpy as np

x = [1, 2, 3, 4, 5, 6, 7]
sizes = [100, 150, 200, 250, 300, 350, 400]


a=["red","yellow","orange","blue","purple","green","black"]

plt.scatter(x = x, y = x, s = sizes, c = a, alpha = 0.5 )
plt.title("Diferentes tamaños")
plt.show()