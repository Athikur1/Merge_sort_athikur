def Fibonacci_nonrecursive(num):
    first_value = 0
    second_value = 1
    t_sum=0
    if num == 1:
        print(0)
    else:
        print(1)
        for i in range(num-2):
            t_sum = first_value + second_value
            print(t_sum)
            first_value = second_value
            second_value = t_sum

n = int(input("Enter the limit of fibo series"))
Fibonacci_nonrecursive(n)