# Ask the user for a number
# and output that many primes in the following pattern
# (increasing number of primes per line)
"""
=== Sample io ===
Enter n: 10

22
3 5
7 11 13
17 19 23 29
"""

# uin
n = int(input("Enter n: "))

# pre-process
def prime(n):
    i = 2
    isPrime = True
    while i*i<=n:
        if n%i == 0:
            isPrime = False
        else:
            isPrime = isPrime
        i += 1
    return isPrime

primelst = []

# process
def find_line(n):
    elementlist = []
    i = 1
    sigma = 0
    while sigma+i <= n:
        sigma += i
        i += 1
        if sigma+i > n:
            elementlist.append(i-1+(n-sigma))
        else:
            elementlist.append(i-1)
    return elementlist

# sysout
repeat = find_line(n)
i = 2
primecount = 0
while primecount<n:
    if prime(i):
        primelst.append(i)
        primecount += 1
    i += 1

for iterate in repeat:
    for i in range(iterate):
        print(primelst.pop(0), end=' ')
    print('')