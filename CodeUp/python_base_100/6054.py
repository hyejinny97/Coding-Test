# 6054: 둘 다 참일 경우만 참 출력하기
# 시간제한:1초 / 메모리제한:128MB

a, b = map(int, input().split())
print(bool(a) and bool(b))