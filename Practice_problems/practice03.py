# Ask the user to enter a number n followed by n numbers.
# Thereafter, ask the user to enter another number m and then m indices.
# Sort the list while keeping the m indicated indices fixed.

"""
=== Sample io ===
Enter n: 10
10 9 8 7 6 5 4 3 2 1
Enter m: 2
Enter indices: 0 6
10 1 2 3 5 6 4 7 8 9
"""
# Indices 0 and 6 remained fixed,
# so the numbers at those position 10, 4 remained fixed
# the rest are sorted in ascending order

# uin
n = int(input("Enter n: "))
input_arr = input("").strip()
array = []
for entry in input_arr.split(' '):
    array.append(int(entry))
m = int(input("Enter m: "))
indices_arr = input("Enter indices: ").strip()
indices = []
for entry in indices_arr.split(' '):
    item = [int(entry), array[int(entry)]]
    indices.append(item)

for entry in indices:
    array.remove(entry[1])

# preprocess
i = 0
while i < len(array)-1:
    for j in range(0, len(array)-i-1):
        if array[j] > array[j+1]:
            exch = array[j+1]
            array[j+1] = array[j]
            array[j] = exch
    i += 1

# process
for index in indices:
    array.insert(index[0], index[1])

# sysout
print(array)
