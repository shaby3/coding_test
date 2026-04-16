n = int(input())

# Please write your code here.

ans = []
while n:
    ans.append(n % 2)
    n //= 2

if not ans:
    print(0)

for num in ans[::-1]:
    print(num, end = '')
