a, b, c = map(int, input().split())

# Please write your code here.
# 하루는 총 몇분이지? 24시간 * 60분
min_per_day = 24 * 60

# 일 수 기준으로 소요 분 계산
day_time = min_per_day * (a - 11)

# 시, 분을 활용한 소요 분 계산
min_time = (b * 60 + c) - (11 * 60 + 11)

ans_time = max(-1, day_time + min_time)

print(ans_time)