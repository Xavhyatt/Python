def add_or_multiply(a,b,c):
    if c == True:
        return a+b
    else:
        return a*b


a = 10
b = 20
c = False

print(add_or_multiply(a,b,c))
