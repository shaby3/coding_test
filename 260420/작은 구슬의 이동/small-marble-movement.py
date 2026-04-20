n, t = map(int, input().split()) # n행 n열, t초
r, c, d = input().split() # 초기 구슬 위치: r행 c열, d는 방향을 의미함
r, c = int(r) - 1, int(c) - 1

# Please write your code here.
# 초기 위치에서 정해진 방향으로 t초만큼 이동

# 0초 ~ 7초
# 8초 ~ 15초

t = t % (2*n) # 벽에 반사되는 경우를 고려하여 t를 왕복 시간 2*n으로 나누어준 나머지로 설정

mapper = {
    "U": 0,
    "D": 3,
    "L": 1,
    "R": 2
}

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

d = mapper[d]

def in_range(x, y):
    if 0 <= x < n and 0 <= y < n:
        return True
    return False

for idx in range(t):
    nr, nc = r + dx[d], c + dy[d]
    if not in_range(nr, nc):
        d = 3 - d
    else:
        r, c = nr, nc

print(r + 1, c + 1)