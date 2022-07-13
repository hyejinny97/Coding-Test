# 6063: 정수 2개 입력받아 큰 값 출력하기
# 시간제한:1초 / 메모리제한:128MB

a, b = map(int, input().split())
print(a if a > b else b)