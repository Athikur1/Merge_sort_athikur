x= [1,23,4,5,66,6,6,7,8,1]
z = []
for i in x:
    if i not in z:
        z.append(i)
print(z)