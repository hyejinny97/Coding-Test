# 6098: 성실한 개미
# 시간제한:1초 / 메모리제한:128MB

# 10 x 10크기의 개미집 생성
house = []
for _ in range(10):
    house.append(input().split())

# (2 - 1,2 - 1)부터 시작해 개미가 오른쪽, 아래로만 이동하는데, 이동한 경로는 9로 표시
x, y = 1, 1   # 개미의 출발좌표
while True:
    # 현재 위치에 먹이가 있는 경우
    if house[y][x] == '2':
        house[y][x] = '9'
        break
    # 현재 위치하는 좌표 마킹
    house[y][x] = '9'

    # 이동 가능한 곳(미로상자를 벗어나지 않고, 벽이 아닌 경우) 탐색한 후, 이동
    # 오른쪽 확인
    if x + 1 < 10 and house[y][x + 1] != '1':
        x += 1
    # 아래쪽 확인
    elif y + 1 < 10 and house[y + 1][x] != '1':
        y += 1
    # 이동 불가한 경우(맨 아래 가장 오른쪽에 도착한 경우, 더이상 움직일 수 없는 경우)
    else:
        break

# 개미집 출력
for i in range(10):
    print(' '.join(house[i]))