n = int(input())
a, b, c = [], [], []
for _ in range(n):
    num, cnt1, cnt2 = map(int, input().split())
    a.append(num)
    b.append(cnt1)
    c.append(cnt2)

# Please write your code here.

# 111 - 999 까지의 숫자들 중에서 조건을 만족하는 경우만 남겨두고 나머지는
# 모두 제외시키면 된다

def get_cnt(cur_num, target_num):
    cur_num = list(map(str, cur_num))
    target_num = list(map(str, str(target_num)))
    
    cnt1 = 0
    cnt2 = 0
    for cn, tn in zip(cur_num, target_num):
        if cn == tn:
            cnt1 += 1
        elif cn in target_num:
            cnt2 += 1

    return cnt1, cnt2

ans = 0
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            if i != j and j != k and i != k:
                cnt = 0
                for target_num, cnt1, cnt2 in zip(a, b, c):
                    cnt_1, cnt_2 = get_cnt([i, j, k], target_num)
                    cur_num = i * 100 + j * 10 + k
                    if cnt_1 == cnt1 and cnt_2 == cnt2:
                        cnt += 1
                if cnt == n:
                    ans += 1
                    # print(i, j, k)
print(ans)