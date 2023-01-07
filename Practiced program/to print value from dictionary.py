dict = {'1':'one','2':'two','3':'three'}


a = input('Enter number ')

z = ''
for i in a:
    z += dict.get(i, '?') + ' '
print(z)

    


 

