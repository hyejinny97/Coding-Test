# 6095: 바둑판에 흰 돌 놓기
# 시간제한:1초 / 메모리제한:128MB

# 바둑판 만들기
plate = []
for _ in range(20):
    plate.append(['0'] * 20)

# 바둑판에 바둑 놓기
n = int(input())
for _ in range(n):
    y, x = map(int, input().split())
    plate[y][x] = '1'

# 바둑판 출력
for i in range(1, 20): 
    print(' '.join(plate[i][1:]))