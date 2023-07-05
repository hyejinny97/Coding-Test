# https://www.acmicpc.net/problem/11399
# 문제11399번.ATM
# 시간: 1초, 메모리: 256MB



# 입력
'''
1. 줄을 서 있는 사람의 수 N
- 1 ≤ N ≤ 1,000
2. 각 사람이 돈을 인출하는데 걸리는 시간 Pi
- 1 ≤ Pi ≤ 1,000
'''



# 출력
'''
1. 각 사람이 돈을 인출하는데 필요한 시간의 합의 최솟값을 출력
'''



# 코드

# 접근방법
'''
인출 시간이 적게 걸리는 사람부터 순서대로 돈을 뽑으면 됨 
'''
import sys

sys.stdin = open('input_text/11399.txt')

N = int(input())
times = list(map(int, input().split()))

times.sort()
acc_times = [times[0]]
for i in range(1, N):
    acc_times.append(acc_times[-1] + times[i])

print(sum(acc_times))


# 실행 결과: 성공(메모리:31256kb, 시간:40ms)