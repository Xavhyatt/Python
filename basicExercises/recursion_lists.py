list =  []

for a in range(0,20,2) :
    list.append(a)


print(list)

for n,b in enumerate(list):
    list[n] = b*10

print(list)