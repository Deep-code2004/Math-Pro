def factorial(n):
    if (n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1)


n = int(input())
result = factorial(n)
print("The Factorial of ", n, "is", result)

# This program calculates the factorial of a given number using recursion.





