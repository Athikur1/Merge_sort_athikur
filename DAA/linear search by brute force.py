def search(arr,value):
  for i in range(len(arr)):
    if arr[i] == value:
      print("Element found at index",i)
      return i
  print("Element not found")
  return -1
arr=[2,5,6,3,8,9,4,1,7]
search(arr,6)
  
  
    
