N, B = map(int, input().split())

# Please write your code here.
ans = []

while N:
    ans.append(N % B)
    N = N // B

for x in ans[::-1]:
    print(x, end = '')