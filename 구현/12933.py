duck = input()
spell = ['q', 'u', 'a', 'c', 'k']
visited = [False] * len(duck)
count = 0
idx = 0

if len(duck) % 5 != 0:
    print(-1)
    exit()

for i in range(len(duck)):
    if duck[i] == 'q' and not visited[i]:
        first = True

        for j in range(len(duck)):
            if spell[idx] == duck[j] and not visited[j]:
                visited[j] = True

                if duck[j] == 'k': # idx를 증가시키며 'k'가 되면 한 문자 완성
                    if first:
                        count += 1
                        first = False
                    idx = 0
                    continue
                idx += 1

if count == 0 or not all(visited):
    print(-1)
else:
    print(count)