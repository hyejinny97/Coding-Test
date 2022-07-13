# 6094: 이상한 출석 번호 부르기3
# 시간제한:1초 / 메모리제한:128MB

n = input()
nums = list(map(int, input().split()))
min_num = nums[0]
for num in nums:
    if min_num > num:
        min_num = num
print(min_num)
