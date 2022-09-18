# https://www.acmicpc.net/problem/10973
# 문제10973번.이전 순열
# 시간: 1초, 메모리: 256MB



# 입력
'''
1. 수열의 길이 N
- 1 <= N <= 10,000
2. N개의 수열
'''



# 출력
'''
1. 입력으로 주어진 순열의 이전에 오는 순열을 출력
- 만약, 사전순으로 가장 처음에 오는 순열인 경우엔 -1을 출력
'''



# 접근 방법
'''
- 핵심: 이전 순열은 오름차순이어야하므로, 위로 올라갈수록 '조금씩' 작아져야 함
1) 뒤에서부터 순회하면서 앞 > 뒤인 경우
2) 앞=x, 뒤=y라 하고, 마지막 인덱스부터 x까지 순회하면서 x보다 작은 수 찾아서 스왑
3) x 뒤는 역으로 정렬 
'''



# 코드
import sys

sys.stdin = open('input_text/10973.txt')

N = int(input())
nums = list(map(int, input().split()))
first = True   # 입력받은 순열이 첫번째 순열인지 여부
finish = False   # 이전 순열을 구했는지 여부 

for i in range(N - 1, 0, -1):
  if nums[i] < nums[i - 1]:
    first = False
    for j in range(N - 1, i - 1, -1):
      if nums[i - 1] > nums[j]:
        nums[i - 1], nums[j] = nums[j], nums[i - 1]
        prev = nums[:i] + sorted(nums[i:], reverse=True)   # 이전 순열 
        finish = True
        break
  if finish:
    break

if first:
  print(-1)
else:
  print(*prev)



# 실행 결과: 성공(메모리:30840kb, 시간:72ms)