def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i

    return result

for i in range (0,10):
    print(i, (factorial(i)))
