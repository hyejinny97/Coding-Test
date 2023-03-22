# https://www.acmicpc.net/problem/15652
# 문제15652번.N과 M(4)
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

<조건>
1) 1부터 N까지 자연수 중에서 M개를 고른 수열
2) 같은 수를 여러 번 골라도 됨(중복 허용)
3) 고른 수열은 비내림차순이어야 함
'''



# 코드 
import sys

sys.stdin = open('input_text/15652.txt')

def duplicate_combination(cnt, N, start, seq):
    if len(seq) == cnt:
        print(*seq)
        return

    for num in range(start, N + 1):
        duplicate_combination(cnt, N, num, seq + [num])


N, M = map(int, input().split())
duplicate_combination(M, N, 1, [])


# 실행 결과: 성공(메모리:31256kb, 시간:56ms)