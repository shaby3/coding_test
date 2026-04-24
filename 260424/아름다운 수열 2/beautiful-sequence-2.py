from collections import Counter

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.
counter_b = Counter(B)

ans = 0
for i in range(N - M + 1):
    
    if Counter(A[i: i+ M]) == counter_b:
        ans += 1
print(ans)

