# 개발자 수, 전염병 걸린 이후 K번의 악수만 전염병 옮김, P는 처음 전염병 걸린 개발자 번호, T는 총 악수 횟수
N, K, P, T = map(int, input().split())
handshakes = [tuple(map(int, input().split())) for _ in range(T)] # t, x, y
handshakes.sort()

# Please write your code here.
# N명의 개발자들
# 악수 횟수: T번
# x개발자와 y개발자가 악수를 나눈 시간: t초
# 전염병이 걸린 이후 K번의 악수 동안만 전염병을 옮기게 됨
# 그 이후에는 전염병에 걸려는 있지만 옮기지는 않음
# 전염된 사람끼리 만나도 전염시킨 것으로 간주해야 함.

# 정리를 하자면 총 T번의 악수가 진행되는데 감염될 경우 K번의 악수 동안만 전염병을 옮김
# 남은 전염 횟수를 나타내는 배열 1개

remain_cnt = [0] * (N + 1)
checked = [0] * (N + 1)

remain_cnt[P] = K
checked[P] = 1

for t, x, y in handshakes:
    # 만약 둘 다 감염이 된 상태면
    if remain_cnt[x] != 0 and remain_cnt[y] != 0:
        remain_cnt[x] -= 1
        remain_cnt[y] -= 1
    elif remain_cnt[x] != 0:
        remain_cnt[x] -= 1
        remain_cnt[y] = K
        checked[y] = 1
    elif remain_cnt[y] != 0:
        remain_cnt[x] = K
        remain_cnt[y] -= 1    # 만약 x만 감염된 상태면
        checked[x] = 1

for idx in range(1, N + 1):
    print(checked[idx], end = '')    