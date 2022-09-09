# 문제10804번.문자열의 거울상
# 시간: 3초, 메모리: 256MB



# 입력
'''
1. 테스트 케이스 T
2. 문자열 S
'''



# 출력
'''
1. #{테스트케이스} {S에 두 개의 서로 다른 문자가 정확히 두 번 등장하면 Yes, 아니면 No}
'''



# 코드
import sys
from collections import Counter

sys.stdin = open('../input_text/11856.txt')

T = int(input())
for test_case in range(1, T + 1):
    S = Counter(input())
    satisfied = True

    if len(S) == 2:
        for key in S:
            if S[key] != 2:
                satisfied = False
    else:
        satisfied = False
            
    if satisfied:
        print(f'#{test_case} Yes')
    else:
        print(f'#{test_case} No')
    

    
# 실행 결과: 성공(메모리:60,348 kb, 시간:181 ms)