n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
ans = -1

def check_carry(num1, num2, num3):
    max_len = max(len(str(num1)), len(str(num2)), len(str(num3)))
    str_num1 = str(num1).zfill(max_len)
    str_num2 = str(num2).zfill(max_len)
    str_num3 = str(num3).zfill(max_len)

    for idx in range(max_len):
        if int(str_num1[idx]) + int(str_num2[idx]) + int(str_num3[idx]) >= 10:
            return 0

    return num1 + num2 + num3

# 3개를 선택
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            summation = check_carry(arr[i], arr[j], arr[k])
            if summation:
                ans = max(ans, summation)
print(ans)