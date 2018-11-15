def factorial(n):
    if n == 1:
        return 1
    else:
      return n * factorial(n-1)


print(factorial(5))

def add_or_multiply(a,b,c,n):
    if n == 0:
        return 1
    if c == True or a ==0 or b ==0:
        print(a+b)
        return add_or_multiply((a+b),b,c,(n-1))
    else:
        print(a*b)
        return add_or_multiply((a*b),b,c,(n-1))




print(add_or_multiply(1,2,True,10))