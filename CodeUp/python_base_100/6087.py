# 6087: 3의 배수는 통과
# 시간제한:1초 / 메모리제한:128MB

n = int(input())
for i in range(1, n + 1):
    if i % 3 != 0:
        print(i, end=' ')