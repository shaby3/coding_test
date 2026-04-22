a = list(map(str, input()))

# Please write your code here.
for idx in range(len(a)):
    if a[idx] != "1":
        a[idx] = "1"
        break

print(int("".join(a), 2))
