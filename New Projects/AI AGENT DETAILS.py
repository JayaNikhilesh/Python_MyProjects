'''n = int(input("Enter number of elements: "))
b = []
for y in range(n):
    b.append(int(input()))
m = 0
temp// = b[0]
for item in range(n):
    if b[item] >= temp:
        m += 1
print(m)'''



'''
n = int(input("Enter number of elements: "))

b = n / 7

x = int(b + 1)
print(x) 

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
for i in sorted(arr):
    print(i, end= ' ') 
'''

'''n=input("enter a name:")
length=len(n)
if length<5:
    print("weak")
else:
    print("strong")'''

'''age=int(input("enter your age:"))
if age<18:
    print("child ticket")
else:
    print("adult ticket")'''


'''n=input("enter a name:")
length=len(n)
if(length%2==0):
    print("even")
else:
    print("odd")'''

'''
matrix = [[0,1,0],[1,1,0],[0,0,1]]
row_counts = []
for row in matrix:
    row_counts.append(sum(row))
print("Row with max 1s:", row_counts.index(max(row_counts)))'''
'''
# Choose number of soldiers and skill range
n = int(input("Enter number of soldiers: "))
r = int(input("Enter maximum skill number: "))

# DP table: dp[pos][skill] = number of ways
dp = [[0] * (r+1) for _ in range(n)]

# First soldier must be skill 1
dp[0][1] = 1

# Fill positions
for pos in range(1, n):
    for skill in range(1, r+1):
        if dp[pos-1][skill] > 0:
            for next_skill in range(1, r+1):
                if next_skill != skill:  # no two same adjacent
                    dp[pos][next_skill] += dp[pos-1][skill]

# Last soldier must be skill r
print("Number of valid arrangements:", dp[n-1][r])
'''

'''
def merge(a,b):
    i=j=0; res=[]
    while i<len(a) and j<len(b):
        if a[i]<b[j]:
            res.append(a[i]); i+=1
        else:
            res.append(b[j]); j+=1
    res.extend(a[i:]); res.extend(b[j:])
    return res

a = [3, 4, 5, 8]
b = [2, 5, 7, 9]

n = merge(a, b)
print(n)
'''

c = (x for x in range(5))
print(c)