n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def func(cur_val, idx):
    if idx == n:
        return cur_val
        
    return func(max(cur_val, arr[idx]), idx + 1)

ans = func(arr[0], 1)
print(ans)