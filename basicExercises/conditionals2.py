def add_or_multiply(a,b,c):
    if c == True or a ==0 or b ==0:
        return a+b
    else:
        return a*b


a = 0
b = 5
c = True

print(add_or_multiply(a,b,c))
