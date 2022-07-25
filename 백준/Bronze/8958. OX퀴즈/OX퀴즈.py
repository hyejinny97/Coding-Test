# 내 풀이

N = int(input())

while N > 0:
  cnt = 0
  rst = 0
  line = list(input())
  for idx in range(0, len(line)):
    if line[idx] == "X":
      cnt = 0
      continue
    cnt += 1
    rst += cnt
  print(rst)
  N -= 1