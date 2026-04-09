N = int(input())

# Please write your code here.


def func(pre2, pre1, n, N):
    if N == 1:
        return pre2
    if N == 2:
        return pre1
    
    pre2, pre1 = pre1, (pre2 * pre1) % 100
    if n == N:
        return pre1
    return func(pre2, pre1, n + 1, N)

print(func(2, 4, 3, N))
