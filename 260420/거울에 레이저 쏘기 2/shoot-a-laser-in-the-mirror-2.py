n = int(input())
grid = [list(input()) for _ in range(n)]
k = int(input())

# Please write your code here.
# K를 N으로 나눈 몫과 나머지를 기준으로 위치를 특정한다. 몫이 0인 경우 북, 몫이 1인 경우 동, 몫이 2인 경우 남, 몫이 3인 경우 서
# 북인 경우 (0, 나머지), 동인 경우(나머지, n-1), 남인 경우(n - 1, n - 나머지), 서인 경우(n - 나머지, 0)

# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

if k // n == 0: # 북인 경우
    sx, sy = 0, k % n - 1
    d = 2
elif k // n == 1: # 동인 경우
    sx, sy = k % n - 1, n - 1
    d = 3
elif k // n == 2: # 남인 경우
    sx, sy = n - 1, n - (k % n)
    d = 0
elif k // n == 3: # 서인 경우
    sx, sy = n - (k % n), 0
    d = 1

mapping_slash = {
    0: 1,
    1: 0,
    2: 3,
    3: 2,
}

mapping_reverse = {
    0: 3,
    3: 0,
    1: 2,
    2: 1,
}

# /의 경우에는 북 -> 동, 동 -> 북, 서 -> 남, 남 -> 서
# \의 경우에는 북 -> 서, 서 -> 북, 동 -> 남, 남 -> 동
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

cnt = 0
while in_range(sx, sy):
    if grid[sx][sy] == "/":
        d = mapping_slash[d]
    else:
        d = mapping_reverse[d]
    
    sx, sy = sx + dx[d], sy + dy[d]
    cnt += 1

print(cnt)


