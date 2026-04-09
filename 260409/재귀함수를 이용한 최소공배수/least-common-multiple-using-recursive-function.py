n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

def get_gcd(n1, n2):
    while n2 > 0:
        n1, n2 = n2, n1 % n2
    
    return n1

def func(cur, idx):
    if idx == n:
        return cur
    
    gcd = get_gcd(cur, arr[idx])
    return func(cur * arr[idx] // gcd, idx + 1)


print(func(arr[0], 1))
