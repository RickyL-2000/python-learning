def check(n):
    try:
        n = int(n)
        if not type(n) == int or not 0 < n <= 50:
            print("Invalid input!")
            return None
    except:
        print("Invalid input!")
        return None
    return n

def factorial(n):
    prod = 1
    for i in range(2, n+1):
        prod *= i
    return prod

while True:
    n = input("Please enter a positive integer ranged in (1, 50):")
    n = check(n)
    if n:
        print("The factorial is:", factorial(n))
        break
    else:
        continue
