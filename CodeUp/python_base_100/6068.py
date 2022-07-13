# 6068: 점수 입력받아 평가 출력하기
# 시간제한:1초 / 메모리제한:128MB

score = int(input())
if score >= 90:
    print('A')
elif score >= 70:
    print('B')
elif score >= 40:
    print('C')
else:
    print('D')