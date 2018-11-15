list =  [1,2,3,4,5,6,7,8,9,10]

def add_or_multiply(a,b,c):
    if c == True or a ==0 or b ==0:
        return a+b
    else:
        return a*b

for a in list :
   print( add_or_multiply(a,5,True))
