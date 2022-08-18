# A python program to create an array from another array
from array import *
arr1=array('i',[10,20,30,40,50])
print("before copying array 1 to array 2")
for i in arr1:
    print(i)
print("After copying array1 to array2")
arr2=array(arr1.typecode,(a*2 for a in arr1))
for i in arr2:
    print(i)
