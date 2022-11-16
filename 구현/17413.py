S = list(input())
idx = 0
start = 0

while idx < len(S):
    if S[idx] == "<":
        idx += 1
        while S[idx] != ">":
            idx += 1
        idx += 1 # ">" 다음으로 인덱스 증가

    elif S[idx].isalnum():
        start = idx
        while idx < len(S) and S[idx].isalnum():
            idx += 1
        temp = S[start:idx]
        temp.reverse()
        S[start:idx] = temp

    else: # 공백이라면
        idx += 1

print("".join(S))