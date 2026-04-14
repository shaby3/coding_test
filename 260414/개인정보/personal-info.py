n = 5
name = []
height = []
weight = []

for _ in range(n):
    n, h, w = input().split()
    name.append(n)
    height.append(int(h))
    weight.append(float(w))

# Please write your code here.
class Person:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

persons = []

for n, h, w in zip(name, height, weight):
    persons.append(Person(n, h, w))

print("name")
persons.sort(lambda x: x.name)
for p in persons:
    print(p.name, p.height, p.weight)

print()
print("height")
persons.sort(lambda x: -x.height)
for p in persons:
    print(p.name, p.height, p.weight)