import numpy as np
import timeit

arr = np.array([1,2,3,4,6])

print(arr)


print("_ _"*20)

# check version of numpy
print(np.__version__)


ar = np.array([15,34,96,3,15,20])

print(ar)
print(np.__version__)
print(type(ar))


print("_ _"*20)

# check executive time with using timeit library
 
n="5+5"
print(timeit.timeit(n))

stmt = "[i**4 for i in range(1, 5)]"
time_taken = timeit.timeit(stmt, number=1000000)
print(f"Time taken: {time_taken:.2f} seconds")


print("_ _"*20)

# convert list into array

x = [15,6,9,30,78,3]

y = np.array(x)

print(y)
































