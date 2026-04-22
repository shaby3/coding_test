n = int(input())
a = [int(input()) for _ in range(n)]

# Please write your code here.
# 시작 위치에 따른 거리의 합을 모두 구해서 그 중 최소를 선택
# 따라서 완전 탐색

# 출발 위치 2를 시작 위치로 잡으면 3은 거리가 1 단 1은 거리가 4 n이 5 기준
# e - s 가 만약 마이너스라면 n을 더해주면 된다.

ans = 1003 * 100

for s in range(n):
    dist = 0
    for e in range(n):
        d = e - s
        if d < 0:
            d = n + d
        dist += a[e] * d
    ans = min(ans, dist)
print(ans)