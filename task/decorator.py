def my_decorator(func):
    def wrapper():
        num= int(func())
        return num*2
    return wrapper

@my_decorator
def number():
    return "123"

print(number())
