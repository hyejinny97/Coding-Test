# 6058: 둘다 거짓일 경우 참 출력하기
# 시간제한:1초 / 메모리제한:128MB

a, b = map(lambda x: bool(int(x)), input().split())
print((not a) and (not b))
# print(not(a or b))