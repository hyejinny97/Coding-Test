# 6083: 빛 섞어 색 만들기
# 시간제한:2초 / 메모리제한:128MB

red, green, blue = map(int, input().split())
cnt = 0
for r in range(0, red):
    for g in range(0, green):
        for b in range(0, blue):
            print(f'{r} {g} {b}')
            cnt += 1
print(cnt)