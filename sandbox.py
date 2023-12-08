import numpy as np
import math as m

'''
#Sandbox to play around with code

'''
'''
word = "*aceca*"
arr = [1,2,5]
arr.count(1)
#print(arr)
print(word.count('*'))

print(1%2)

#print(bin(1).count("1"))

for i in ran:
    print(i)

a =[2,4,7,3]
b =[5,2,1,6]
left = [0]
right = [0,4,2,53,4]
#print(np.subtract(a,b))
#print(left, right)

#a.append((2,3))
#print(a[-1:0:-1])
#right.insert(len(right),23)
#print(right)
#right.reverse()
#print(right[2] + 2)
right.insert(len(right),2)
right.remove(4)
print(right)
#print(a[:0:-1])

flip = ""
nums = [1,2,3,4]
print(sum(nums[0:0],nums[0]))
print(len(nums[0:1]))

num = 17
print(round((num**0.5)))
print(0 if num == 18 else -1)
flip = "yes"
print(flip.index("e"))

print(m.ceil(1/2))
'''


#print(s + 'a')
#print(s,q)
nums = [1,2,3,4,5,6]
arr = []
count =0
o = nums.index(max(nums))
#print(o,type(o))
#print(1//3)
def missingNumber(nums) -> int:
        arr = tuple(set(range(0,len(nums)+1)) - set(nums))[0]
missingNumber(nums=nums)

k=3
nums = [1,2,3]

for i in nums:
    if k-i in nums:
          count+=1
          nums.pop(k-i)
print(count)