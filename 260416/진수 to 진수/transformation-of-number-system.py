a, b = map(int, input().split())
n = input()

# Please write your code here.
# a진수 -> 10진수 -> b진수

num_10 = int(n, a)

ans = []
while num_10:
    ans.append(num_10 % b)
    num_10 //= b

for n in ans[::-1]:
    print(n, end = '')