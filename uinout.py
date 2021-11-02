# Determine whether a given number is a prime number
def prime(n):
    i = 2
    isPrime = True
    while i*i <= n:
        if n%i==0:
            isPrime = False
        else:
            isPrime = isPrime
        i += 1
    if isPrime:
        return n
    else:
        return 0

# Edit the text file with 'write' mode
charlie = open("cinout.txt", 'w')

charlie.write("The following are the first 100 prime numbers\n")

count = 0
i = 2
lst = []

while count < 20:
    number = prime(i)
    if number != 0:
        if count%10 == 0:
            lst.append("\n")
        lst.append(number)
        count += 1
    i += 1

for item in lst:
    charlie.write((str(item)+" "))

charlie.close()

print("write-mode done\n")

# Read from the text file with 'read' mode
kevin = open("cinout.txt", 'r')

s = kevin.readline()

while not s=='':
    print(s.rstrip())
    s = kevin.readline()

kevin.close()

print("read-mode done")
