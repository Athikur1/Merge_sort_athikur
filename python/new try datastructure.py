def list1():
    list1=[]
    n = int(input("enter how may value: "))
    while(n > len(list1)):
        nv = input("enter values: ")
        list1.append(nv)
    print(list1)

def set1():
    set1=set()
    n = int(input("enter how may value: "))
    while(n > len(set1)):
        nv = input("enter values: ")
        set1.append(nv)
    print(set1)
    
def dict1():
    dict={}
    print("Dict working")

def tuple1():
    tuple1=()
    print("tuple working")
    
def c():
    df = int(input("Select data storage type:\nList(1)\nSet(2)\nDict(3)\nTuple(4): "))
    if df == 1:
        list1()
    elif df == 2:
        set1()
    elif df == 3:
        dict1()
    elif df == 4:
        tuple1()
    else:
        print("Give valid detail ")





