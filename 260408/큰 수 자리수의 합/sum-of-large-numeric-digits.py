a, b, c = map(int, input().split())

# Please write your code here.
num = a * b * c

def func(num):
    if num == 0:
        return 0

    return num % 10 + func(num // 10)

print(func(num))