# Ask the user for a number and output the following pattern
"""
=== Sample ===
Enter n: 7
   X
  XOX
 XOXOX
XOXOXOX
 XOXOX
  XOX
   X
"""

# uin
n = int(input("Enter n: "))

# process
def pattern(n):
    pat = ''
    i = 1
    while i<=n:
        if (i%2!=0):
            pat += 'X'
        else:
            pat += 'O'
        i += 1
    return pat

# sysout
# Iterate through all odd numbers
i = 1
mid = int((n+1)/2)
while i <= mid:
    print((mid-i)*" "+pattern(2*i-1))
    i += 1
i -= 2
while i>=1:
    print((mid-i)*" "+pattern(2*i-1))
    i -= 1