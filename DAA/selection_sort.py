# arr = [2,5,6,3,8,9,4,1,7]
# arr =[5,7,4]



arr = []
arr_len = int(input("Enter length of aray: "))
print("Enter", arr_len, "numbers")

while arr_len > 0:
    user_input = int(input("\r"))
    arr.append(user_input)
    arr_len -= 1



def selec_sort(arr):
    for i in range(0, len(arr)):
        for j in range(i+1 , len(arr)):
            if(arr[i] > arr[j]):
                arr[i], arr[j] = arr[j], arr[i]
    return arr


print("Original Array", arr)
print("Sorted array", selec_sort(arr))
