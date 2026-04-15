m1, d1, m2, d2 = map(int, input().split())
A = input()

# Please write your code here.
def num_of_days(m, d):
    days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    total_days = 0
    for i in range(1, m):
        total_days += days[i]
    
    total_days += d

    return total_days

total_days = num_of_days(m2, d2) - num_of_days(m1, d1)

dates = {'Mon': 0, "Tue": 1, "Wed": 2, "Thu": 3, "Fri": 4, "Sat": 5, "Sun": 6}

total_days -= dates[A]

print(total_days // 7 + 1)