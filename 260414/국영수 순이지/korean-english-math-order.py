n = int(input())
name = []
korean = []
english = []
math = []

for _ in range(n):
    student_info = input().split()
    name.append(student_info[0])
    korean.append(int(student_info[1]))
    english.append(int(student_info[2]))
    math.append(int(student_info[3]))

# Please write your code here.
students = []

for n, k, e, m in zip(name, korean, english, math):
    students.append((n, k, e, m))

students.sort(lambda x: (-x[1], -x[2], -x[3]))

for x in students:
    print(x[0], x[1], x[2], x[3])