# 언어: Python, (성공/실패) : 1/0, 메모리 : 30840KB, 시간 : 68ms

a, b, c = map(int, input().split())

if (2 <= a, b, c <= 1000):
  print((a+b)%c)
  print(((a%c) + (b%c))%c)
  print((a*b)%c)
  print(((a%c) * (b%c))%c)