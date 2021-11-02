def find_prime(n):
    i = 2
    isPrime = True
    while i*i<=n:
        if n%i==0:
            isPrime = False
        else:
            isPrime = isPrime
        i += 1
    if isPrime:
        print("YES")
    else:
        print("NO")


number = int(input("Input a number: "))
find_prime(number)
