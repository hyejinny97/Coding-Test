# 6064: 정수 3개 입력받아 가장 작은 값 출력하기
# 시간제한:1초 / 메모리제한:128MB

a, b, c = map(int, input().split())
print(c if (b if a > b else a) > c else (b if a > b else a))