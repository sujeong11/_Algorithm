import re

T = int(input())
regex = re.compile('^[A-F]?A+F+C+[A-F]?$')

for _ in range(T):
    print("Good" if regex.match(input()) == None else "Infected!")