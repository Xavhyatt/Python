from functools import partial

def multiply(a,b):
    return a*b


double = partial(multiply,2)
triple = partial(multiply,3)

a=1
b=5

c= double(a)
d= triple(b)

print("double", a, "is", c)
print("triple", b, "is", d)