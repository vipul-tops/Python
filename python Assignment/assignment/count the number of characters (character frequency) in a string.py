''' Write a Python program to count the number of characters (character 
frequency) in a string '''


st = input("Enter a string: ")

char_freq = {}

for char in st:
    if char in char_freq:
        char_freq[char] += 1
    else:
        char_freq[char] = 1


print("Character Frequency:")
for char, count in char_freq.items():
    print(f"'{char}': {count}")

