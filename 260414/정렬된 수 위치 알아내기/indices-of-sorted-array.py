n = int(input())
sequence = list(map(int, input().split()))

# Please write your code here.
# index 값을 sequence[i]를 기준으로 정렬하면 오름차순으로 정렬했을 때의 index 리스트가 생성된다..
sorted_idx = sorted(range(n), key = lambda i: sequence[i])

rank = [0] * n
for i, idx in enumerate(sorted_idx):
    rank[idx] = i + 1

print(*rank)