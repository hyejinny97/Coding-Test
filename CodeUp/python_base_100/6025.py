# 6025: 정수 2개 입력받아 합 계산하기
# 시간제한:1초 / 메모리제한:128MB
# 풀이1
a, b = input().split()
print(int(a) + int(b))

# 풀이2
a, b = map(int, input().split())
print(a + b)
