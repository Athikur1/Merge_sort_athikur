def ip():
    arr = []
    a = int(input("enter how many numbers:"))
    while len(arr) <a:
        n = input("Enter values: ")
        arr.append(n)
    print(arr)
    mergesort(arr)
    print("Sorted array is: ")
    printlist(arr)
    
    
    
def mergesort(arr):
    if len(arr) >1:
        mid = len(arr) //2
        L = arr[:mid]
        R =arr[mid:]
        
        mergesort(L)
        mergesort(R)
        merge(arr,L,R)
    
def merge(arr,L,R):
    i =j= k= 0
    while i<len(L) and j< len(R):
        if L[i]< R[j]:
            arr[k] = L[i]
            i+=1
        else:
            arr[k] = R[j]
            j+=1
        k+=1
    while i<len(L):
        arr[k] =L[i]
        i+=1
        k+=1
    while j< len(R):
        arr[k]= R[j]
        j+=1
        k+=1     

    
def printlist(arr):
    for i in range(len(arr)):
        print(arr[i], end =' ')
    print()




            