# https://www.acmicpc.net/problem/10972
# 문제10972번.다음 순열
# 시간: 1초, 메모리: 256MB



# 입력
'''
1. 수열의 길이 N
- 1 <= N <= 10,000
2. N개의 수열
'''



# 출력
'''
1. 입력으로 주어진 순열의 다음에 오는 순열을 출력
- 만약, 사전순으로 가장 마지막에 오는 순열인 경우엔 -1을 출력
'''



# 접근 방법
'''
- 핵심: 다음 순열은 내림차순이어야하므로, 아래로 갈수록 '조금씩' 커져야 함!!
1) 입력받은 순열을 뒤에서부터 순회해서 앞 < 뒤인 경우
2) 앞=x, 뒤=y라고 하면 마지막 인덱스부터 x까지 순회하면서 x보다 큰 수를 마주치면 x와 스왑
3) x 뒤에 값들을 오름차순으로 sort()
'''



# 코드
import sys

sys.stdin = open('input_text/10972.txt')

N = int(input())
nums = list(map(int, input().split()))
last = True   # 입력받은 순열이 마지막 순열인지 여부 
finish = False   # 다음 순열을 구했는지 여부

for i in range(N - 1, 0, -1):
  if nums[i - 1] < nums[i]:
    last = False
    for j in range(N - 1, i - 1, -1):
      if nums[i - 1] < nums[j]:
        nums[i - 1], nums[j] = nums[j], nums[i - 1]
        next = nums[:i] + sorted(nums[i:])   # 다음 순열
        finish = True
        break
  if finish:
    break

if last:
  print(-1)
else:
  print(*next)



# 실행 결과: 성공(메모리:30840kb, 시간:76ms)