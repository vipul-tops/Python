#lambda function
#Anonymous function

#task=1
def double(x):
    return x*2
print(double(10))

double= lambda x: x*2
print(double(8))

print("--------")
#task=2
avg= lambda x,y: (x+y)/2
print(avg(7,9))

print("--------")
#task=3
l= lambda name: print("Hello ,",name)
l("Vipul")

print("--------")
#task=4
x= lambda a,b,c: a+b+c
print(x(5,6,2))

print("--------")
#task=5
l=[1,2,4,5,7,9,11]
l= map(lambda x: x*x,l)

for num in l:
    print(num,end=" ")
