OFFSET = 100
MAX_R = 200

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x, y = zip(*points)
x, y = list(x), list(y)

# Please write your code here.
# 가로세로 길이가 8인 즉 넓이가 64인 색종이 N장 주어짐.
# 좌측하단의 꼭지점이 주어졌을 때, 모든 색종이가 ㅜㅌ여진 이후의 총 넓이를 구하는 프로그램을 작성
# 모든 색종이는 -100, -100을 좌측 상단 100, 100을 우측 하단으로 -> 이는 우측 하단이 99, 99 까지 있음을 의미함

mat = [[0] * MAX_R for _ in range(MAX_R)]

for i, j in zip(x, y):
    for ci in range(i, i + 8):
        for cj in range(j, j + 8):
            mat[ci][cj] = 1

ans = 0
for i in range(MAX_R):
    for j in range(MAX_R):
        if mat[i][j] == 1:
            ans += 1

print(ans)