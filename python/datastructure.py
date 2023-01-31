def array_function():
    arr_len=int(input("Enter the length of the array"))
    array=[0 for i in range(arr_len)]
    for j in range(arr_len):
        array[j]=int(input("enter the array element"))
    print("The given array",array)

def list_function():
    lis_len=int(input("Ente the length of list:"))
    alist=[]
    for j in range(lis_len):
        alist.append(eval(input("Enter the list element:")))
    print("The given list",alist)

def tuple_function():
    tuple_len=int(input("Enter the tuple of length:"))
    atuple=()
    for i in range(tuple_len):
        a =tuple(int((input("Enter the tuple element:"))))
        atuple = atuple+a
    print("The given tuple",atuple)

def dic_function():
    dic_len=int(input("Enter the tuple of list:"))
    adic=[]
    for i in range(dic_len):
        key=eval(input("Enter the key:"))
        value=eval(input("Enter the value:"))
        adic[key]=value
    print("The given Dictionary:",adic)


print("Select your choice of data Structure \n 1.Array \n 2.list \n 3.tuple\n 4.Dictionary\n 5.set")
 
choice=int(input("Enter your Choice:"))

if (choice==1):
    print("Array Data structure:")
    array_function()

elif(choice==2):
    print("List Data Structure:")
    list_function()
elif(choice==3):
    print("Tuple Data Structure:")
    tuple_function()

elif(choice==4):
    print("Dictionary Data Structure:")
    dic_function()

elif(choice==5):
    print("Set Data Structure:")
    list_function()
else:
    print("Invalid choice")