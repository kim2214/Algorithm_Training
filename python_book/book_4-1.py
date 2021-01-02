n = int(input())
x,y = 1, 1
plans = input().split()

for i in range(n):
    if plans[i] == 'R':
        if x < n:
            x += 1
        else:
            continue
    elif plans[i] == 'L':
        if x <= 1:
            x -= 1
        else:
            continue
    elif plans[i] == 'U':
        if y < n:
            y += 1
        else:
            continue
    elif plans[i] == 'D':
        if y < n:
            y -= 1
        else:
            continue

print(x,y)
