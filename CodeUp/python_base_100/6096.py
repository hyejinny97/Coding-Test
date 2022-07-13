# 6096: 바둑알 십자 뒤집기
# 시간제한:1초 / 메모리제한:128MB

# 뒤집기 함수
def reverse(m):
    if m == '0':
        return '1'
    if m == '1':
        return '0'

# 바둑판 현재 상태
plate = []
for _ in range(19):
    plate.append(input().split())

# 좌표 값에 따라 바둑알 십자 뒤집기
n = int(input())
for _ in range(n):
    y, x = map(int, input().split())
    # y축 아래로 내려가면서 동일한 x 좌표 뒤집기
    for i in range(19):
        plate[i][x - 1] = reverse(plate[i][x - 1])
    # y좌표에 해당하는 모든 x좌표 뒤집기
    for j in range(19):
        plate[y - 1][j] = reverse(plate[y - 1][j])

# 십자 뒤집기한 바둑판 출력
for i in range(19):
    print(' '.join(plate[i]))