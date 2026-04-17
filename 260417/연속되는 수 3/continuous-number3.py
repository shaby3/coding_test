N = int(input())
arr = [int(input()) for _ in range(N)]

# Please write your code here.
cnt = 1
ans = 1
for i in range(N - 1):
    # 만약 arr[i]와 arr[i + 1]의 부호가 같으면 cnt += 1, max값 갱신
    if arr[i] // abs(arr[i]) == arr[i + 1] // abs(arr[i + 1]):
        cnt += 1
        ans = max(ans, cnt)
    else:
        cnt = 1
print(ans)
    # 만약 부호가 반대라면, cnt = 1