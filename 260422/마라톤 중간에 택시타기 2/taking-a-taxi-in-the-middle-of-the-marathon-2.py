n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Please write your code here.
'''
체크포인트가 총 n개이고 그 중 2개는 건너뛰는 경우에서 제외한다고
했으니 총 n - 2 번을 완전탐색하면된다.

건너뛸 idx를 1에서 n - 2 중에 하나를 고르면 된다.

idx를 골랐으면 처음부터 prev_coord와 cur_coord의 좌표 간의
거리를 계산해서 ans에 추가하면 된다.
이 때 건너뛰는 경우만 신경을 써주면 되는데 
'''
ans = 100 * 2000
for skip_idx in range(1, n - 1):
    prev_idx = 0
    total_distance = 0
    for cur_idx in range(1, n):
        if cur_idx == skip_idx:
            continue
        total_distance += abs(x[cur_idx] - x[prev_idx]) + abs(y[cur_idx] - y[prev_idx])
        prev_idx = cur_idx
    ans = min(total_distance, ans)

print(ans)