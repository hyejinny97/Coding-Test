# https://school.programmers.co.kr/learn/courses/30/lessons/87946
# 코딩테스트연습 < 완전탐색 < 문제.피로도



# 입력
'''
1. 유저의 현재 피로도 k
- 1 <= k <= 5,000
2. 각 던전별 "최소 필요 피로도", "소모 피로도"가 담긴 2차원 배열 dungeons
- 1 <= 던전의 개수 <= 8
- 1 <= "최소 필요 피로도", "소모 피로도" <= 1,000
- 서로 다른 던전의 ["최소 필요 피로도", "소모 피로도"]가 서로 같을 수 있음
'''



# 출력
'''
1. 유저가 탐험할수 있는 최대 던전 수를 return
- "최소 필요 피로도": 해당 던전을 탐험하기 위해 가지고 있어야 하는 최소한의 피로도
- "소모 피로도": 던전을 탐험한 후 소모되는 피로도
'''


# 코드 

# 접근방법
'''
순열을 이용해서 유저가 탐험해야하는 던전 순서 경우의 수 구하기 
'''
import sys
from itertools import permutations

sys.stdin = open('input_text/피로도.txt')

def solution(k, dungeons):
    order_cases = permutations(dungeons, len(dungeons))
    
    max_cnt = 0   # 탐험할 수 있는 최대 던전 수
    for order_case in order_cases:
        cnt = 0   # 탐험 던전 수
        now = k   # 현재 피로도
        for dungeon in order_case:
            required, consume = dungeon   # 최소 필요 피로도, 소모 피로도
            if now >= required:
                cnt += 1
                now -= consume
        max_cnt = max(max_cnt, cnt)

    return max_cnt


# 실행 결과: 성공