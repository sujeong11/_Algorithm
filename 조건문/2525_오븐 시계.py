# 언어: Python, (성공/실패) : 1/1, 메모리 : 30840KB, 시간 : 68ms

H, M = map(int, input().split());
timer = int(input());

H += timer // 60;
M += timer % 60;

if M >= 60:
    H += 1;
    M -= 60;
if H >= 24:
    H -= 24;

print(H, M);