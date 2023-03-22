# https://www.acmicpc.net/problem/15649
# 문제15649번.N과 M(1)
# 시간: 1초, 메모리: 512MB



# 입력
'''
1. 자연수 N과 M
- 1 ≤ M ≤ N ≤ 8
'''



# 출력
'''
1. 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열을 한 줄에 하나씩 출력
- 수열은 사전 순으로 증가하는 순서로 출력해야 함
'''



# 코드 
import sys

sys.stdin = open('input_text/15649.txt')

def permutation(cnt, nums, seq):
    if len(seq) == cnt:
        print(*seq)
        return

    for num in nums:
        new_nums = nums[:]
        new_nums.remove(num)
        permutation(cnt, new_nums, seq + [num])


N, M = map(int, input().split())
permutation(M, list(range(1, N + 1)), [])


# 실행 결과: 성공(메모리:31256kb, 시간:180ms)