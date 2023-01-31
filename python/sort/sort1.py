def bubble_sort(list1):  
    # Outer loop for traverse the entire list  
    for i in range(0,len(list1)-1):  
        for j in range(len(list1)-1):  
            if(list1[j]>list1[j+1]):   
                # here we are not using temp variable  
                list1[j],list1[j+1] = list1[j+1], list1[j]  
    return list1  
  
list1 = [5, 3, 8, 6, 7, 2]  
print("The unsorted list is: ", list1)  
# Calling the bubble sort function  
print("The sorted list is: ", bubble_sort(list1))  



n = int(input('Enter how many numbers: '))

n1 = n

a =[]

while n>0:
    a.append(int(input("enter s number: ")))
    n = n-1

print("Given array: ")
print(a)

selectionSort(a,n1)
print('sorted array in ascending oder: ')
print(a)