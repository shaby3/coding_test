N = int(input())

# Please write your code here.
def func(n):
    if n <= 1:
        return n
    
    return n + func(n - 2)

print(func(N))