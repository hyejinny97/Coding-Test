# 6074: 정수 1개 입력받아 알파벳 출력하기
# 시간제한:1초 / 메모리제한:128MB

alph = ord(input())
now = ord('a')
while now <= alph:
    print(chr(now), end=' ')
    now += 1
