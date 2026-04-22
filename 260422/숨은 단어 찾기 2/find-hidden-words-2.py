N, M = map(int, input().split())
arr = [input() for _ in range(N)]

# Please write your code here.

def in_range(x, y):
    return 0 <= x < N and 0 <= y < M

def func():
    ans = 0
    for i in range(N):
        for j in range(M):
            char = arr[i][j]
            if char == 'L': # char이 l일때만 검사하면 됨
                # 가로 체크
                for d in range(1, 3):
                    nj = j + d
                    if in_range(i, nj) and arr[i][nj] == 'E':
                        pass
                    else:
                        break
                else:
                    ans += 1

                for d in range(1, 3):
                    nj = j - d
                    if in_range(i, nj) and arr[i][nj] == 'E':
                        pass
                    else:
                        break
                else:
                    ans += 1

                # 세로 체크
                for d in range(1, 3):
                    ni = i + d
                    if in_range(ni, j) and arr[ni][j] == 'E':
                        pass
                    else:
                        break
                else:
                    ans += 1

                for d in range(1, 3):
                    ni = i - d
                    if in_range(ni, j) and arr[ni][j] == 'E':
                        pass
                    else:
                        break
                else:
                    ans += 1

                # 우측 대각선 체크
                for d in range(1, 3):
                    ni = i + d
                    nj = j + d
                    if in_range(ni, nj) and arr[ni][nj] == 'E':
                        pass
                    else:
                        break
                else:
                    ans += 1

                # 우측 대각선 체크
                for d in range(1, 3):
                    ni = i - d
                    nj = j - d
                    if in_range(ni, nj) and arr[ni][nj] == 'E':
                        pass
                    else:
                        break
                else:
                    ans += 1

                # 좌측 대각선 체크
                for d in range(1, 3):
                    ni = i + d
                    nj = j - d

                    if in_range(ni, nj) and arr[ni][nj] == 'E':
                        pass
                    else:
                        break
                else:
                    ans += 1

                for d in range(1, 3):
                    ni = i - d
                    nj = j + d

                    if in_range(ni, nj) and arr[ni][nj] == 'E':
                        pass
                    else:
                        break
                else:
                    ans += 1
    return ans

print(func())
                
