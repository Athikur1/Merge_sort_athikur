# STEP 1:
def mergeSort(array):
    if len(array) > 1:

        r = len(array)//2
        L = array[:r]
        M = array[r:]
        print('L_value: ' + str(L))
        print('M_value: ' + str(M))
        print('\n')

        mergeSort(L)
        mergeSort(M)

        i = j = k = 0

        
    # STEP 2: 
        print('In Step two ')
        print(len(L))
        while i < len(L) and j < len(M):
            print('Inside loop ')
            print('So the value of L: ' + str(L[i]))
            print('So the value of M: ' + str(M[i]))
            if L[i] < M[j]:
                array[k] = L[i]
                print(array[k])
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1
            
        while i < len(L):
            print('In first while')
            array[k] = L[i]
            print(array[k])
            i += 1
            k += 1

        while j < len(M):
            print('In second while')
            array[k] = M[j]
            print(array)
            j += 1
            k += 1


# Print the array
def printList(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()


# Driver program
if __name__ == '__main__':
    array = [6, 5, 12, 10, 9, 1]

    mergeSort(array)

    print("Sorted array is: ")
    printList(array)

