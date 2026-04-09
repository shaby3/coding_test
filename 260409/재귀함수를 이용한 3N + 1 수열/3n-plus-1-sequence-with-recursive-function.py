n = int(input())

# Please write your code here.
def func(n, cnt):
    if n == 1:
        return cnt

    if n % 2 == 0:
        return func(n // 2, cnt + 1)
    else:
        return func(n * 3 + 1, cnt + 1)

print(func(n, 0))
