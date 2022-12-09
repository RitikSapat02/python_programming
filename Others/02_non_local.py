x = "fantastic"        #global
def outer():
    x = "local"             #local
    def inner():
        nonlocal x         #refers to parent local instead of global
        x="non-local"
        print("inner: ",x)
    inner()
    print("outer: ",x)

outer()