user2_id, user2_level = input().split()
user2_level = int(user2_level)

# Please write your code here.
class ID:
    def __init__(self, id = "codetree", level = 10):
        self.id = id
        self.level = level

ID1 = ID(user2_id, user2_level)
ID2 = ID()

print(f"user {ID2.id} lv {ID2.level}")
print(f"user {ID1.id} lv {ID1.level}")