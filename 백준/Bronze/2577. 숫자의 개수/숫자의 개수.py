# 내 풀이

import sys
import collections

cnt = 3
nums = []
while cnt > 0:
  nums.append(int(input()))
  cnt -= 1

mul_num = str(nums[0] * nums[1] * nums[2])
dictionary = collections.Counter(mul_num)

for idx in range(0,9+1):
  print(dictionary[str(idx)])