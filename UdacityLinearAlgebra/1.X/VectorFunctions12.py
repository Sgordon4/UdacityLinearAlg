# -*- coding: utf-8 -*-
"""
Created on Sat Dec 29 14:02:01 2018

@author: Sean Gordon
"""


#-------Prints all importable modules from current path-------
#import pkgutil
#search_path = '.' # set to None to see all modules importable from sys.path
#all_modules = [x[1] for x in pkgutil.iter_modules(path=search_path)]
#print(all_modules)

import VectorFunctions4
import VectorFunctions10


def projection(vector1, vector2):
    # Projection of v1 onto v2 is
    # v1 dot v2     
    #   |v2|       *  v2
    dotted = VectorFunctions4.multiply(vector1, vector2)
    magnitude = 0
    for vec in vector2:
        magnitude += vec**2
    
    dot = 0
    for vec in dotted:
        dot += vec
        
    scalar = dot / magnitude
    
    projection = [scalar * vec2 for vec2 in vector2]
    return projection

def perpendicular(vector1, vector2):
    parallel = projection(vector1, vector2)
    
    perp = VectorFunctions4.subtract(vector1, parallel)
    return perp


data1 = [2, 1, 4]
data2 = [1, -2, 1]
print("Testing ----------")
print(projection(data1, data2))
print(perpendicular(data1, data2))
print("------------------")

data3 = [3.039, 1.879]
data4 = [0.825, 2.036]
print(projection(data3, data4))
print("------------------")

data5 = [-9.880, -3.264, -8.159]
data6 = [-2.155, -9.353, -9.473]
print(perpendicular(data5, data6))
print("------------------")

data7 = [3.009, -6.172, 3.692, -2.510]
data8 = [6.404, -9.144, 2.759, 8.718]
print(projection(data7, data8))
print(perpendicular(data7, data8))