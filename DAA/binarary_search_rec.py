def binary_search_rec(arr,target,lower,upper):
  if lower <= upper:
    middle =(lower +upper)//2

    if (arr[middle] ==target):
      return middle
    if (arr [middle]>target):
      upper = middle -1
      return binary_search_rec(arr,target,lower,upper)
    if (arr[middle]<target):
      lower=middle +1
      return binary_search_rec(arr,target,lower,upper)
  return -1

arr =[]
arr_len=int(input("Enter the lenght of array:"))
print("Enter",arr_len,"members")
while arr_len >0:
  user_input =int(input("\r"))
  arr.append(user_input)
  arr_len-=1
res=binary_search_rec(arr,2,0,len(arr)-1)

print("Element is at index",res)
