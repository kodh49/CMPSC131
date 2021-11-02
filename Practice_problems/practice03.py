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
    indices.append(int(entry))
    array.remove(int(entry))

# Check status
# print(array)
# print(indices)

"""
[1,4,3,2] ->
[1,4,3,2] ->
[1,3,4,2] ->
[1,3,2,4] ->
[1,3,2,4] ->
[1,2,3,4] ->
[1,2,3,4] ->
[1,2,3,4]
"""

# preprocess
def switch(arr, i, j):
    if arr[i] > arr[j]:
        exch = arr[i]
        arr[i] = arr[j]
        arr[j] = exch
    return arr


# process
i = 0
while i<len(array)-1:
    
    # Decide whether to switch the position with given index
    array = switch(array, i, i+1)
    
    i += 1



# sysout
