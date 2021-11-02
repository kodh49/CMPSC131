Alst = []

for a in input("Enter sequence A: ").split():
    Alst.append(int(a))

b = int(input("Enter number B: "))

print("The good numbers are:", end=" ")
for item in Alst:
    # Loop through to check if item is a power of given base b
    k = 1
    while b**k <= item:
        if b**k == item:
            print(item, end=" ")
        k += 1
