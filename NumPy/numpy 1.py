import numpy as np

x = np.array([1,2,5,3,6,8])

print(x)
print(type(x))

print(x.ndim)  #check type of dimension of array


print("-"*30)
# 2 dimension array

ar2 = np.array([[1,2,3,4]])
print(ar2)
print(ar2.ndim)

arr2 = np.array([[1,2,3,4],[1,2,3,4]])
print(arr2)
print(arr2.ndim)


print("-"*30)
# 3 dimension array


ar3 = np.array([[[1,2,3,4]]])
print(ar3)
print(ar3.ndim)


arr3 = np.array([[[1,2,3,4],[1,2,3,4],[1,2,3,4]]])
print(arr3)
print(arr3.ndim)


print("-"*30)
# multi dimension array

arn = np.array([1,2,3,4], ndmin=5)  #ndmin - used for multiplay array dimension
print(arn)
print(arn.ndim)











