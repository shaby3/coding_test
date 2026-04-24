N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.
ans = 0
for i in range(N - M + 1):
    if set(A[i:i+M]) == set(B):
        ans += 1
print(ans)
