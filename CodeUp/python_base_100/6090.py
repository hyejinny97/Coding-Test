# 6090: 수 나열하기3
# 시간제한:1초 / 메모리제한:128MB

def seq(start, m, d):
    return start * m + d

a, m, d, n = map(int, input().split())
for _ in range(n - 1):
    a = seq(a, m, d)
print(a)