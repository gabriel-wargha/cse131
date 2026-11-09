
# def factorial_loop(n):
#    factorial = 1
#    for i in range(n):
#        factorial += n *factorial_loop(n-i)
       
#        if factorial != 1:
#         return factorial


def factorial_loop(n):
    factorial = 1
    for i in range(0, n):
        factorial *= i +  1
    
    return factorial


def factorial_recursion(n):
    if n == 1:
        return 1
    
    else:
        return n * factorial_recursion(n-1)
   
if __name__ == "__main__":
    
       print(factorial_loop(5))
       print(factorial_recursion(10))