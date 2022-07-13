# 6092: 이상한 출석 번호 부르기1
# 시간제한:1초 / 메모리제한:128MB

n = int(input())
nums = map(int, input().split())
rst = [0] * 24
for num in nums:
    rst[num] += 1

print(' '.join(map(str, rst[1:])))
