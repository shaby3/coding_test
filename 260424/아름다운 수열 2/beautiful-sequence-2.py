from itertools import permutations

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.
# perms = list(map(list, permutations(B)))
perms = list(permutations(B))


ans = 0
for i in range(N - M + 1):
    
    if tuple(A[i:i+M]) in perms:
        ans += 1

    
print(ans)
