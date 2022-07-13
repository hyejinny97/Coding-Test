# 6077: 짝수 합 구하기
# 시간제한:1초 / 메모리제한:128MB

n = int(input())
rst = 0
for i in range(0, n + 1):
    if i % 2 == 0:
        rst += i
print(rst)