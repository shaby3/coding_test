n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]

# Please write your code here.
str.sort()

start = -1
for i in range(len(str)):
    if str[i].startswith(t):
        if start == -1:
            start = 1
        else:
            start += 1
    
    if start == k:
        print(str[i])
        break
