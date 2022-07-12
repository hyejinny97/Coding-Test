# 6057: 참/거짓이 서로 같을 때에만 참 출력하기
# 시간제한:1초 / 메모리제한:128MB

a, b = map(lambda x: bool(int(x)), input().split())
print(((not a) and (not b)) or (a and b))