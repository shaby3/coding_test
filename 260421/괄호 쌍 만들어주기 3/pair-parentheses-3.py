A = input()

# Please write your code here.
# A를 순회하며 (를 만나면 그 다음 인덱스부터 )의 개수를 찾아서
# ANS에 추가

ans = 0

for i in range(len(A)):
    if A[i] == "(":
        for j in range(i + 1, len(A)):
            if A[j] == ")":
                ans += 1

print(ans)