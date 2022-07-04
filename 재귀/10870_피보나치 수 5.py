# 언어 : Python, (성공/실패) : 1/0, 메모리 : 30840KB, 시간 : 72ms

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

n = int(input())
print(fibonacci(n))
