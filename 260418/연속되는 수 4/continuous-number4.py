n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
cnt = 1
ans = 1
for i in range(n - 1):
    # 만약 현재 값 보다 다음 값이 크면 cnt += 1, ans = max(ans, cnt)
    if arr[i] < arr[i + 1]:
        cnt += 1
        ans = max(ans, cnt)
    # 만약 현재 값 보다 다음 값이 작으면 cnt = 1
    else:
        cnt = 1

print(ans)