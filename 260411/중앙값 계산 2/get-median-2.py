n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

sorted_arr = []

ans = []
for idx in range(len(arr)):
    sorted_arr.append(arr[idx])
    if idx % 2 == 0:
        sorted_arr.sort()
        ans.append(sorted_arr[len(sorted_arr) // 2])

print(" ".join(map(str, ans)))

    