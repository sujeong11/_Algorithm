N = int(input())
status = input()

color_dict = {'B': 0, 'R': 0}
color_dict[status[0]] += 1

for i in range(1, N):
    if (status[i-1] != status[i]):
        color_dict[status[i]] += 1

print(min(color_dict['B'], color_dict['R']) + 1)