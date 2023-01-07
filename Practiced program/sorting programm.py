x= [9,23,4,5,66,6,7,8]
z = []
minimum = x[0]

i = len(x)-1
while i >=0 :
    if minimum > x[i]:
        x.insert(i, minimum)
        x.insert(0, i)
        minimum = i
    i -=1
print(x)

for i in x:
    if i not in z:
        z.append(i)
print(z)
        