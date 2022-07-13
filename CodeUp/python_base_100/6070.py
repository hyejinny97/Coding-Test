# 6070: 월 입력받아 계절 출력하기
# 시간제한:1초 / 메모리제한:128MB

month = int(input())
if month // 3 == 1:   # 3, 4, 5
    print('spring')
elif month // 3 == 2:   # 6, 7, 8
    print('summer')
elif month // 3 == 3:   # 9, 10, 11
    print('fall')
else:
    print('winter')