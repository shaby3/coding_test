N, M, K = map(int, input().split())
student = [int(input()) for _ in range(M)]

# Please write your code here.
# 학생 N명(1 ~ N)
# 한 학생이 k번 이상 벌칙을 받게 되면 벌금 내야함
# M번에 걸쳐 벌칙에 걸린 학생 번호가 순서대로 제공, 최초로 벌금을 내게되는 학생은 누구인지 알아내기

count = [0] * (N + 1)

for student_num in student:
    count[student_num] += 1
    if count[student_num] == K:
        print(student_num)
        break
else:
    print(-1)