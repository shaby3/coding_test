# N, M = map(int, input().split())
# arr = [input() for _ in range(N)]

# # Please write your code here.

# def in_range(x, y):
#     return 0 <= x < N and 0 <= y < M

# def func():
#     ans = 0
#     for i in range(N):
#         for j in range(M):
#             char = arr[i][j]
#             if char == 'L': # char이 l일때만 검사하면 됨
#                 # 가로 체크
#                 for d in range(1, 3):
#                     nj = j + d
#                     if in_range(i, nj) and arr[i][nj] == 'E':
#                         pass
#                     else:
#                         break
#                 else:
#                     ans += 1

#                 for d in range(1, 3):
#                     nj = j - d
#                     if in_range(i, nj) and arr[i][nj] == 'E':
#                         pass
#                     else:
#                         break
#                 else:
#                     ans += 1

#                 # 세로 체크
#                 for d in range(1, 3):
#                     ni = i + d
#                     if in_range(ni, j) and arr[ni][j] == 'E':
#                         pass
#                     else:
#                         break
#                 else:
#                     ans += 1

#                 for d in range(1, 3):
#                     ni = i - d
#                     if in_range(ni, j) and arr[ni][j] == 'E':
#                         pass
#                     else:
#                         break
#                 else:
#                     ans += 1

#                 # 우측 대각선 체크
#                 for d in range(1, 3):
#                     ni = i + d
#                     nj = j + d
#                     if in_range(ni, nj) and arr[ni][nj] == 'E':
#                         pass
#                     else:
#                         break
#                 else:
#                     ans += 1

#                 # 우측 대각선 체크
#                 for d in range(1, 3):
#                     ni = i - d
#                     nj = j - d
#                     if in_range(ni, nj) and arr[ni][nj] == 'E':
#                         pass
#                     else:
#                         break
#                 else:
#                     ans += 1

#                 # 좌측 대각선 체크
#                 for d in range(1, 3):
#                     ni = i + d
#                     nj = j - d

#                     if in_range(ni, nj) and arr[ni][nj] == 'E':
#                         pass
#                     else:
#                         break
#                 else:
#                     ans += 1

#                 for d in range(1, 3):
#                     ni = i - d
#                     nj = j + d

#                     if in_range(ni, nj) and arr[ni][nj] == 'E':
#                         pass
#                     else:
#                         break
#                 else:
#                     ans += 1
#     return ans

# print(func())
                
# 변수 선언 및 입력
n, m = tuple(map(int, input().split()))
arr = [
    input()
    for _ in range(n)
]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m

dxs, dys = [1, 1, 1, -1, -1, -1, 0, 0], [-1, 0, 1, -1, 0, 1, -1, 1]

# 모든 좌표에서 다 확인해봅니다.
cnt = 0
for i in range(n):
	# 격자를 벗어나지 않을 범위로만 잡습니다.
	for j in range(m):
		
		if arr[i][j] != 'L':
			continue
		
		for dx, dy in zip(dxs, dys):
			curt = 1
			curx = i
			cury = j
			while True:
				nx = curx + dx
				ny = cury + dy
				if in_range(nx, ny) == False:
					break
				if arr[nx][ny] != 'E':
					break
				curt += 1
				curx = nx
				cury = ny
			
			if curt >= 3:
				cnt += 1

print(cnt)
