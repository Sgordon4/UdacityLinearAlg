import math

def add(vector1, vector2):
    vector1 = [vec1 + vec2 for vec1, vec2 in zip(vector1, vector2)]
    return vector1

def subtract(vector1, vector2):
    vector1 = [vec1 - vec2 for vec1, vec2 in zip(vector1, vector2)]
    return vector1

def scalar(scale, vector):
    vector = [vec * scale for vec in vector]
    return vector

def multiply(vector1, vector2):
    vector1 = [vec1 * vec2 for vec1, vec2 in zip(vector1, vector2)]
    return vector1

def divide(vector1, vector2):
    vector1 = [vec1 / vec2 for vec1, vec2 in zip(vector1, vector2)]
    return vector1
    
#-------------------------------------------------#
    
def magnitude(vector):
    mag = 0
    for vec in vector:
        mag += vec**2
    mag = math.sqrt(mag)
    return mag

def direction(vector):
    normalizer = 1/magnitude(vector)
    unitVector = scalar(normalizer, vector)
    return unitVector
    
#-------------------------------------------------#

if(False):
    data1 = [1, 2, 3]
    data2 = [3, 2, 1]
    print(add(data1, data2))
    print(subtract(data1, data2))
    print(scalar(4, data1))
    print(multiply(data1, data2))
    print()
    
    print(add([8.218, -9.341], [-1.129, 2.111]))
    print(subtract([7.119, 8.215], [-8.223, .878]))
    print(scalar(7.41, [1.671, -1.012, -.318]))
    
    #- - - - - - - - - - - - - - - - - - - - - - - - -#
    
    print("\nPt. 2")
    print(magnitude([-.221, 7.437]))
    print(magnitude([8.813, -1.331, -6.247]))
    print(direction([5.581, -2.136]))
    print(direction([1.996, 3.108, -4.554]))