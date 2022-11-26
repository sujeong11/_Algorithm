N = int(input())
recommend_cnt = int(input())
student_num = list(map(int, input().split()))
picture = []
score = []

for i in range(recommend_cnt):
    if student_num[i] in picture:
        for j in range(len(picture)):
            if student_num[i] == picture[j]:
                score[j] += 1
    else: # 사진틀에 없을 때
        if len(picture) >= N: # 꽉 차있다면
            for j in range(N):
                if score[j] == min(score): # 가장 작은 값을 삭제
                    del picture[j]
                    del score[j]
                    break

        picture.append(student_num[i])
        score.append(1)

picture.sort()
print(' '.join(map(str, picture)))