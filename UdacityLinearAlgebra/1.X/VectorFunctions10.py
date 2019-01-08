# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 21:56:29 2018

@author: Sean Gordon
"""

import VectorFunctions4

def checkParallel(vector1, vector2):
    # Using divide fuction
    vector1 = VectorFunctions4.divide(vector1, vector2)
    #vector1 = [vec1 / vec2 for vec1, vec2 in zip(vector1, vector2)]
    for i in range(len(vector1)-2):
        if vector1[i] != vector1[i+1]:
            return False
        
    return True

def checkOrthoganal(vector1, vector2):
    # Using multiply fuction
    vector1 = VectorFunctions4.multiply(vector1, vector2)
    #vector1 = [vec1 * vec2 for vec1, vec2 in zip(vector1, vector2)]
    for vec in vector1:
        if vec != 0:
            return False
        
    return True


#-------------------------------------------------#

if(False):
    parallel1 = [1, 2, 3]
    parallel2 = [2, 4, 6]
    
    ortho1 = [7, 23, 5]
    ortho2 = [0, 0, 0]
    
    print(checkParallel(parallel1, parallel2))
    print(checkParallel(parallel1, ortho1))
    
    print(checkOrthoganal(ortho1, ortho2))
    print(checkOrthoganal(ortho1, parallel2))
