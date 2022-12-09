def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a//b

# print(__name__)

if __name__ == "__main__":                    #if i am runnnign this then this will be true . instead if i import it will simply use as module

    print("Hello")
    a = int(input())
    b = int(input())
    print(add(a,b))
