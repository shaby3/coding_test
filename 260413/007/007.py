secret_code, meeting_point, time = input().split()
time = int(time)

# Please write your code here.
class Inform:
    def __init__(self, secret_code, meeting_point, time):
        self.secret_code = secret_code
        self.meeting_point = meeting_point
        self.time = time


inf = Inform(secret_code, meeting_point, time)

print(f"secret code : {inf.secret_code}")
print(f"meeting point : {inf.meeting_point}")
print(f"time : {inf.time}")