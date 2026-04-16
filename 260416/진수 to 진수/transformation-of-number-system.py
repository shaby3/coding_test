a, b = map(int, input().split())
n = input()

# Please write your code here.
# a진수 -> 10진수 -> b진수

# 방법 1
# num_10 = int(n, a)
# 방법 2
num_list = list(map(int, n))

num_10 = 0
for x in num_list:
    num_10 = num_10 * a + x

ans = []
while num_10:
    ans.append(num_10 % b)
    num_10 //= b

for n in ans[::-1]:
    print(n, end = '')