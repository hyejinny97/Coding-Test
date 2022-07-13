# 6072: 정수 1개 입력받아 카운트다운 출력하기1
# 시간제한:1초 / 메모리제한:128MB

n = int(input())
while True:
    if n > 0:
        print(n)
    else:
        break
    n -= 1
