def too_hot(a,b):
    is_summer = b

    if a>=60 and a<=100 and is_summer:
        return True

    elif a>=60 and a<=90 and not is_summer:
        return True

    elif a<60:
        return False

    else:
        return True


print(too_hot(101,False))