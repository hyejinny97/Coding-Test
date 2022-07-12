# 6044: 정수 2개 입력받아 자동 계산하기
# 시간제한:1초 / 메모리제한:128MB

a, b = map(int, input().split())

# 합
print(a + b)

# 차
print(a - b)

# 곱
print(a * b)

# 몫
print(a // b)

# 나머지
print(a % b)

# 나눈 값을 소수점 이하 둘째 자리까지 출력
print(f'{a/b:.2f}')