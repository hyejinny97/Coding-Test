# 6080: 주사위 2개 던지기
# 시간제한:1초 / 메모리제한:128MB

n, m = map(int, input().split())
for i in range(1, n + 1):
    for j in range(1, m + 1):
        print(f'{i} {j}')

