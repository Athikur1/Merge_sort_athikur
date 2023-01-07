def lst ():
    x = []
    a = int(input("enter how many numbers:"))
    
    while len(x) <a:
        n = input("Enter values: ")
        x.append(n)
    print(x)


 
def st():
    s = set()
    print("Remember: Values can't be repeated.")
    b = int(input("enter how many numbers:"))
    
    while len(s) <b:
        s1 = input("Enter values: ")
        s.add(s1)
    print(s)
    
def dt():
    di = {}
    
    print("Remember: Values should have reference variable.")
    d = int(input("enter how many numbers:"))
    
    while len(di) <d:
        d1 = input("Enter reference values: ")
        d2 = input("Enter values: ")
        di[d1] = d2 
    print(di)

def tp():
    tu = ()
    print("Remember: Carefull once created Values can't be changed.")
    t = int(input("enter how many numbers:"))
    while len(tu) <t:
        t1 = input("Enter values: ")
        tu += tuple(t1)
    print(tu)


