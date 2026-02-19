hourse1 = int(input())
minute1 = int(input())
hourse2 = int(input())
minute2 = int(input())

start_time = hourse1 * 60 + minute1
end_time = hourse2 * 60 + minute2

while start_time <= end_time:
    hourse = start_time // 60
    minute = start_time % 60
    print(f"{hourse:02d}:{minute:02d}")
    start_time += 1

