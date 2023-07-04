def fibonacci(n):
    a = 1
    b = 0
    for i in range(n):
        a, b = b, a + b
    return b
 
print(fibonacci(35))