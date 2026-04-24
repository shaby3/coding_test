from 

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.
perms = list(map(list, permutations(B)))

ans = 0
for i in range(N - M + 1):
    cur_val = A[i: i + M]
    if cur_val in perms:
        ans += 1
        break
print(ans)

