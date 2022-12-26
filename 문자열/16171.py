import re

S = input()
K = input()
string = re.sub("[0-9]", "", S)

if (K in string):
    print(1)
else:
    print(0)