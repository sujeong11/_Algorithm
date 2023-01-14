import sys
input = sys.stdin.readline

dic = {}
count = 0

while True:
    tree = input().rstrip()

    if not tree:
        break

    if tree in dic:
        dic[tree] += 1
    else:
        dic[tree] = 1
    count += 1

sort_tree = sorted(dic.keys()) # 사전 순으로 정렬

for st in sort_tree:
    print("%s %.4f" %(st, (dic[st] / count) * 100))