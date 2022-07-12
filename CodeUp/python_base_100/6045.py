# 6045: 정수 3개 입력받아 합과 평균 출력하기
# 시간제한:1초 / 메모리제한:128MB

a, b, c = map(int, input().split())
sum3 = a + b + c
mean3 = sum3 / 3
print(f'{sum3} {mean3:.2f}')