binary = input()

# Please write your code here.

binary = list(map(int, binary))

num = 0
for x in binary:
    num = num * 2 + x

print(num)