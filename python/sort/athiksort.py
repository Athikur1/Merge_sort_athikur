n = int(input('Enter how many numbers: '))

n1 = n

list1 =[]

while n>0:
    list1.append(int(input("enter s number: ")))
    n = n-1

print("Given array: ")
print(list1)



def bubble_sort(list1):  
    # Outer loop for traverse the entire list  
    for i in range(0,len(list1)-1):  
        for j in range(len(list1)-1):  
            if(list1[j]>list1[j+1]):   
                # here we are not using temp variable  
                list1[j],list1[j+1] = list1[j+1], list1[j]  
    return list1  


bubble_sort(list1)
print('sorted array in ascending oder: ')
print(list1)



