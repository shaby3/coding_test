N = input()

# Please write your code here.
# 이진수 N을 십진수로 변환
num_ten = int(N, 2)

# 십진수를 17배
num_ten *= 17

# 다시 이진수로 출력
print(bin(num_ten)[2:])