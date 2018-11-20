def unique_sum(a,b,c):
    if a!=b and a!=c and b!=c:
        return a + b + c

    elif a==b and b==c:
        return 0

    elif a==b:
        return c

    elif a==c:
        return b

    elif b==c:
        return a


print(unique_sum(1,4,4))