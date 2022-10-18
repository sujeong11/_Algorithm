def find_loc(word):
    keyboard = [['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
                    , ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
                    , ['z', 'x', 'c', 'v', 'b', 'n', 'm']]

    for i in range(3):
        for j in keyboard[i]:
            if (word == j):
                return i, keyboard[i].index(j)


left, right = map(str, input().split())
data = str(input())
time = 0

for i in data:
    if (left == i or right == i):
        time += 1
    else:
        left_locX, left_locY = find_loc(left)
        right_locX, right_locY = find_loc(right)
        data_locX, data_locY = find_loc(i)

        if i in "qwertasdfgzxcv":
            time += abs(left_locX - data_locX) + abs(left_locY - data_locY) + 1
            left, left_locX, left_locY = i, data_locX, data_locY
        else:
            time += abs(right_locX - data_locX) + abs(right_locY - data_locY) + 1
            right, right_locX, right_locY = i, data_locX, data_locY

print(time)