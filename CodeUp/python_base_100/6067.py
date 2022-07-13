# 6067: 정수 1개 입력받아 분류하기
# 시간제한:1초 / 메모리제한:128MB

num = int(input())
if num < 0:
    if num % 2 == 0:
        print('A')
    else:
        print('B')
else:
    if num % 2 == 0:
        print('C')
    else:
        print('D')