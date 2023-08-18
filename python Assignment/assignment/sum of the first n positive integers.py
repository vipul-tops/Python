# Write a python program to sum of the first n positive integers.

def sum_of_first_n_positive_integers(n):
    if n <= 0:
        return 0
    else:
        return (n * (n + 1)) // 2

# Taking input from the user
n = int(input("Enter a positive integer: "))

result = sum_of_first_n_positive_integers(n)
print("Sum of the first", n, "positive integers:", result)

print("-------------------------------")
n=int(int(input("Entre Number : ")))

if n<=0:
    print("Zero")

else:
    print("sum of Positive integers :",(n*(n+1))//2)
