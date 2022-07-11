# 6027: 10진 정수 입력받아 16진수로 출력하기1
# 시간제한:1초 / 메모리제한:128MB
num = int(input())
# 풀이1
print('%x' % num)   # ff
# 풀이2
print(f'{num:x}')   # ff
# 풀이3
print(hex(num))   # 0xff