# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 22:27:53 2019

@author: Sean Gordon
"""
import sys
import VectorFunctions4
import VectorFunctions10
import VectorFunctions12

def crossProduct(vector1, vector2):
    cross = [
    vector1[0]*vector2[1] - vector1[1]*vector2[0],
    vector1[1]*vector2[2] - vector1[2]*vector2[1],
    vector1[2]*vector2[0] - vector1[0]*vector2[2],
    ]

    return cross

def parallelogramArea(vector1, vector2):
    cross = crossProduct(vector1, vector2)
    area = VectorFunctions4.magnitude(cross)

    return area

def areaOfTriangle(vector1, vector2):
    area = parallelogramArea(vector1, vector2)
    return area/2



#-------------------------------------------------#

data1 = [8.462, 7.893, -8.187]
data2 = [6.984, -5.975, 4.778]
print crossProduct(data1, data2)

data3 = [-8.987, -9.838, 5.031]
data4 = [-4.268, -1.861, -8.866]
print parallelogramArea(data3, data4)

data5 = [1.500, 9.547, 3.691]
data6 = [-6.007, 0.124, 5.772]
print areaOfTriangle(data5, data6)
