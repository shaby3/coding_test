n = int(input())

name = []
score1 = []
score2 = []
score3 = []

for _ in range(n):
    student_input = input().split()
    name.append(student_input[0])
    score1.append(int(student_input[1]))
    score2.append(int(student_input[2]))
    score3.append(int(student_input[3]))

# Please write your code here.
class Person:
    def __init__(self, name, score1, score2, score3):
        self.name = name
        self.score1 = score1
        self.score2 = score2
        self.score3 = score3

persons = []
for n, s1, s2, s3 in zip(name, score1, score2, score3):
    persons.append(Person(n, s1, s2, s3))

persons.sort(lambda x: x.score1 + x.score2 + x.score3)

for person in persons:
    print(person.name, person.score1, person.score2, person.score3)