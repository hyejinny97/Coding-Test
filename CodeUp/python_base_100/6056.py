# 6056: 참/거짓이 서로 다를 때에만 참 출력하기
# 시간제한:1초 / 메모리제한:128MB

a, b = map(lambda x: bool(int(x)), input().split())
print((a and (not b)) or ((not a) and b))