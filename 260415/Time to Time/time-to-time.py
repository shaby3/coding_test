a, b, c, d = map(int, input().split())

# Please write your code here.
start_time = a * 60 + b
end_time = c * 60 + d

print(end_time - start_time)