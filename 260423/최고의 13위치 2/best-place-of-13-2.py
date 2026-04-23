n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
new_arr = [[0] * (n - 2) for _ in range(n)]

for i in range(n):
    for j in range(n - 2):
        new_arr[i][j] = sum(arr[i][j:j+3])

# for row in arr:
#     print(row)

# for row in new_arr:
#     print(row)
        
ans = 0
for cur_i in range(len(new_arr)):
    for cur_j in range(len(new_arr[0])):
        for next_i in range(cur_i, len(new_arr)):
            for next_j in range(len(new_arr[0])):
                if next_i == cur_i and cur_j + 2 >= next_j:
                    continue
                ans = max(ans, new_arr[cur_i][cur_j] + new_arr[next_i][next_j])
print(ans)