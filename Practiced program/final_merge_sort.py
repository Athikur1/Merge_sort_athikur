def ip():
    arr = []
    n = int(input("enter how many numbers:"))
    while n>0:
        arr.append(int(input("Enter value: ")))
        n=n-1
    print(arr)
    divide(arr)
    print("Sorted array is: ")
    printlist(arr)
    
    
    
def divide(arr):
    if len(arr) >1:
        mid = len(arr) //2
        L = arr[:mid]
        R =arr[mid:]
        
        divide(L)
        divide(R)
        merge_sort(arr,L,R)

def merge_sort(arr,L,R):
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
