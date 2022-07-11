# 6028: 10진 정수 입력받아 16진수로 출력하기2
# 시간제한:1초 / 메모리제한:128MB
num = int(input())
# 풀이1
print('%X' % num)   # FF
# 풀이2
print(f'{num:X}')   # FF