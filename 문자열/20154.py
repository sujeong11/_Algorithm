alphabet = [3, 2, 1, 2, 3, 3, 3, 3, 1, 1, 3, 1, 3, 3, 1, 2, 2, 2, 1, 2, 1, 1, 2, 2, 2, 1]
S = input()
arr = []

for i in S:
    temp = ord(i) - ord('A')
    arr.append(alphabet[temp])

result = sum(arr) % 10

if result % 2:
    print("I'm a winner!")
else:
    print("You're the winner?")