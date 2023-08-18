# Write a Python program to count occurrences of a substring in a string

main_string = input("Enter the main string: ")
substring = input("Enter the substring to count: ")

count = 0
start = 0

# Counting occurrences of substring
while start < len(main_string):
    pos = main_string.find(substring, start)
    if pos != -1:
        count += 1
        start = pos + 1
    else:
        break

# Displaying the count of occurrences
print(f"The substring '{substring}' appears {count} times in the main string.")
