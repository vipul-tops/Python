#counting of vowel and consonants
s=input("Enter String : ")
vowel=0
coun=0
sp=0
for i in s:
    if (i=='a'or i=='e' or i=='i' or i=='o' or i=='u'):
        vowel=vowel+1
    elif (i==' '):
        sp=sp+1
    else:
        coun=coun+1
print("Vowel : ",vowel)
print("Counsanants : ",coun)
print("Space : ",sp)
