
import numpy as np

# Array fills with zero (0)

print("Array Filled with Zeros (0)")
ar_zero = np.zeros(4)
ar_zero1 = np.zeros((3,4))

print(ar_zero)
print()
print(ar_zero1)

print("-"*30)
# Array filled with Ones (1)

print("Array filled with Ones (1)")
ar_one = np.ones(4)
ar_one1 = np.ones((3,4))

print(ar_one)
print()
print(ar_one1)


print("-"*30)

# Array Filled with Empty
print("Array Filled with Empty")
ar_em = np.empty(4)

print(ar_em)


print("-"*30)
# Array filled with range

print("Array Filled With Range")
ar_range = np.arange(6)

print(ar_range)


print("-"*30)

# Array Diagonal

print("Array Diagonal")
ar_dia = np.eye(3)

print(ar_dia)

ar_dia1 = np.eye(3,5)

print(ar_dia1)

print("-"*30)
# Array linspace

print("Array Linspace")
ar_lin = np.linspace(0,20,num=5)

print(ar_lin)















