# 6097: 설탕과자 뽑기
# 시간제한:1초 / 메모리제한:128MB

# 격자판 만들기
h, w = map(int, input().split())
plate = []
for _ in range(0, h + 1):   # 격자판 세로 인덱스: 0부터 h까지
    plate.append(['0'] * (w + 1))   # 격자판 가로 인덱스: 0부터 w까지

# 막대를 격자판 위에 올려놓기
n = int(input())
for _ in range(n):
    l, d, y, x = map(int, input().split())
    if d == 0:   # 가로방향
        for i in range(x, x + l):
            plate[y][i] = '1'
    else:   # 세로방향
        for j in range(y, y + l):
            plate[j][x] = '1'

# 격자판 출력
for i in range(1, h + 1):
    print(' '.join(plate[i][1:]))