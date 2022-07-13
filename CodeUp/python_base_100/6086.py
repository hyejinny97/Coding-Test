# 6086: 거기까지! 이제 그만~
# 시간제한:1초 / 메모리제한:128MB

limit = int(input())
n = 1
rst = 0
while rst < limit:
    rst += n
    n += 1
print(rst)