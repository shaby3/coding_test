a = list(map(int, input()))

# Please write your code here.
ans = 0
for idx in range(len(a)):
    a[idx] = 1 - a[idx]
    
    ans = max(ans, int(''.join(map(str,a)), 2))

    a[idx] = 1 - a[idx]

print(ans)
