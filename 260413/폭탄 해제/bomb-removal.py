unlock_code, wire_color, seconds = input().split()
seconds = int(seconds)

# Please write your code here.
class Class:
    def __init__(self, code, color, second):
        self.code = code
        self.color = color
        self.second = second

c = Class(unlock_code, wire_color, seconds)

print(f"code : {c.code}")
print(f"color : {c.color}")
print(f"second : {c.second}")