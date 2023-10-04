
import numpy as np

# check data type of numpy array

var = np.array([1,2,3,4,5,10])

print(var)
print("Data Type : ",var.dtype)


print("-"*30)

var = np.array([1.1,1.2,1.4,1.6])

print(var)
print("Data Type : ",var.dtype)


print("-"*30)

var = np.array(["a","b","c","d"])

print(var)
print("Data Type : ",var.dtype)


print("-"*30)

var = np.array(["a","b","c","d",1,2,3,4])

print(var)
print("Data Type : ",var.dtype)


print("-"*30)
# change data type of array

x = np.array([1,2,3,4],dtype = np.int8)

print(x)
print("data type : ",x.dtype)



print("-"*30)

# change int to float

x1 = np.array([1,2,3,4], dtype = "f")

print(x1)
print("data type  : ",x1.dtype)



print("-"*30)

# change data type

x2 = np.array([1,2,3,4])

new = np.float32(x2)

print(x2)
print("Data type : ",x2.dtype)

print(new)
print("Data type : ",new.dtype)


print("-"*30)

# change data type

x2 = np.array([1,2,3,4])

new = np.float32(x2)

new_one = np.int_(new)

print(x2)
print("Data type : ",x2.dtype)

print(new)
print("Data type : ",new.dtype)

print(new_one)
print("Data type : ",new_one.dtype)















