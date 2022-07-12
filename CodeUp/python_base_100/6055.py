# 6055: 하나라도 찹이면 참 출력하기
# 시간제한:1초 / 메모리제한:128MB

a, b = map(int, input().split())
print(bool(a) or bool(b))