def print_list(arr):
  for i in range(len(arr)):
    print(arr[i],end=" ")

    print()
#Driver code
n=int(input("Enter how many numbers:"))
n1=n
arr=[]
while n>0:
  arr.append(int(input("Enter a number:")))
  n=n-1
print("
