def multiples(a,b):
    c=[]
    for i in range(b):
        c.append(a*(i+1))
    return c


r1,r2,r3,r4=multiples(3,4)
print(r1,r2,r3,r4)
r1,r2,r3,r4,r5=multiples(2,5)
print(r1,r2,r3,r4,r5)

