# 6082: 3 6 9 게임의 왕이 되자
# 시간제한:1초 / 메모리제한:128MB

n = int(input())
for i in range(1, n + 1):
    #  3, 6, 9의 수가 들어가면 박수
    if i % 10 == 3 or i % 10 == 6 or i % 10 == 9:
        print('X', end=' ')
    else:
        print(i, end=' ')
