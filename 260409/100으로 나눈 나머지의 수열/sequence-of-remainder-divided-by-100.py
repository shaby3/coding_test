N = int(input())

# Please write your code here.


def func(pre2, pre1, n):
    pre2, pre1 = pre1, (pre2 * pre1) % 100
    if n == N:
        return pre1
    return func(pre2, pre1, n + 1)

print(func(2, 4, 3))
