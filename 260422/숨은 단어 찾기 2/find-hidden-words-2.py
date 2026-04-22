N, M = map(int, input().split())
arr = [input() for _ in range(N)]

# Please write your code here.

def in_range(x, y):
    return 0 <= x < N and 0 <= y < M

def func():
    dxs = [0, -1, -1, -1, 0, 1, 1, 1]
    dys = [-1, -1, 0, 1, 1, 1, 0, -1]
    ans = 0
    for i in range(N):
        for j in range(M):
            num = arr[i][j]
            
            if num != 'L':
                continue
            
            # 다른 문자가 나올 때 까지 개수를 세고 다른 문자
            # 가 나왔다면 그 순간의 개수를 체크해서 3개면 ans +=1
            for dx, dy in zip(dxs, dys):
                curx = i
                cury = j
                cnt = 1

                while True:
                    nx = curx + dx
                    ny = cury + dy
                    if not in_range(nx, ny):
                        break
                    if arr[nx][ny] != 'E':
                        break
                    curx = nx
                    cury = ny
                    cnt += 1
                
                if cnt == 3:
                    ans += 1
    return ans

print(func())


            
