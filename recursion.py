#Example of recursion in python


#factorial

def factorial_iterative(n):
    fac = 1
    for i in range(n):
        fac = fac *(i+1)
    return fac

val = factorial_iterative(5)
print(val)


def factorial_recursive(n):
    if n==1:
        return 1
    else:
        return n * factorial_recursive(n-1)

val1 = factorial_iterative(5)
print(val1)




#fibonacci series
x = int(input("Enter your num: "))
def fibonacci(n):
    a= 0
    b = 1
    print(a)
    print(b)

    for i in range(2,n):
        c= a+b
        a=b
        b=c
        print(c)

fibonacci(x)
