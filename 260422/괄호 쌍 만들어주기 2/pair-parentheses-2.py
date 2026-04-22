A = input()

ans = 0
n = len(A)
# Please write your code here.
for i in range(n-3):
    for j in range(i + 2, n - 1):
        if A[i: i+2] == "((":
            if A[j: j+2] == "))":
                ans += 1

print(ans)