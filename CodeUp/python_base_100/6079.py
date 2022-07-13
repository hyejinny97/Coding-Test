# 6079: 언제까지 더해야 할까?
# 시간제한:1초 / 메모리제한:128MB

limit = int(input())
n = 1
rst = 0
while True:
    rst += n
    if rst >= limit:
        print(n)
        break
    n += 1
    
