# 6073: 정수 1개 입력받아 카운트다운 출력하기2
# 시간제한:1초 / 메모리제한:128MB

n = int(input())
while True:
    n -= 1
    print(n)
    if n == 0:
        break