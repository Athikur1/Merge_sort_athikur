def insertionSort(array):
    for i in range(1,len(array)):
        key=array[i]
        j=i-1
        while j>=0 and key<array[j]:
            array[j+1]=array[j]
            j=j-1
        array[j+1]=key
        

array = [] 
n = int(input("enter how many numbers:"))
while n>0:
    array.append(int(input("Enter value: ")))
    n=n-1
print(array)


insertionSort(array)  
print("sorted array in ascending order: ")
print(array)


