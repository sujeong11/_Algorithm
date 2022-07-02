# 언어: Python, (성공/실패) : 1/0, 메모리 : 30840KB, 시간 : 80ms

# 개선한 코드
def hansu(num):
    count = 0

    for i in range(1, num + 1):
        num = list(map(int, str(i)))
        if i < 100:
            count += 1  # 자리수가 1이거나 2이면 비교할 대상이 없으므로 바로 한수가 되버린다.
        elif (num[0] - num[1]) == (num[1] - num[2]):
            count += 1

    return count

N = int(input())
print(hansu(N))


# 초기 코드
# def hansu(num):
#     num = str(num)
#     digit = []
#
#     for i in num:
#         digit.append(i)
#
#     if (len(num) == 1 or len(num) == 2):
#         return True
#     elif (len(num) == 3):
#         if (int(digit[2]) - int(digit[1]) == int(digit[1]) - int(digit[0])):
#             return True
#         return False
#
# N = int(input())
# count = 0
#
# for i in range(1, N+1):
#     if hansu(i):
#         count += 1
#
# print(count)

