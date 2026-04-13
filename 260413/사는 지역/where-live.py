n = int(input())
name = []
street_address = []
region = []

for _ in range(n):
    n_i, s_i, r_i = input().split()
    name.append(n_i)
    street_address.append(s_i)
    region.append(r_i)

# Please write your code here.
class Person:
    def __init__(self, name, addr, city):
        self.name = name
        self.addr = addr
        self.city = city

persons = []
for n, s, r in zip(name, street_address, region):
    persons.append(Person(n, s, r))

persons.sort(lambda x: x.name)

print(f"name {persons[-1].name}")
print(f"addr {persons[-1].addr}")
print(f"city {persons[-1].city}")