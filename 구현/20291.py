N = int(input())
files = dict()

for _ in range(N):
    extension = input().split('.')[1]

    if extension in files:
        files[extension] += 1
    else:
        files[extension] = 1

files = sorted(files.items())

for key, val in files:
    print(key, val)