import numpy as np
def leftRigthDifference(nums):

    left  = [0]
    right = [0]
    arr = []

    lastEle = 0
    LastEle = 0

    for i,j in zip(nums[:-1:],nums[-1:0:-1]):

        left.append(i + lastEle)
        right.insert(0,j + LastEle)
        
        lastEle += i
        LastEle += j



    print(arr)

leftRigthDifference([10,4,8,3])