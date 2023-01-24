# https://school.programmers.co.kr/learn/courses/30/lessons/138476?language=python3
# 코딩테스트연습 < 연습문제 < 문제.귤 고르기



# 입력
'''
1. 한 상자에 담으려는 귤의 개수 k, 귤의 크기를 담은 배열 tangerine
- 1 <= k <= tangerine 길이 <= 100,000
- 1 <= tangerine 원소 <= 10,000,000
'''



# 출력
'''
1. 귤 k개를 고를 때 크기가 서로 다른 종류의 수의 최솟값을 return
'''


# 코드
import sys
from collections import Counter

sys.stdin = open('input_text/귤고르기.txt')

def solution(k, tangerine):
    # 귤 크기에 따른 개수 세기
    cnt_by_size = Counter(tangerine)

    # 개수에 따라 귤 내림차순 정렬
    ordered_tangerine = sorted(cnt_by_size.items(), key=lambda item: item[1], reverse=True)

    # 크기가 최소가 되도록 k개만큼 선택
    accumulate = 0
    answer = 0
    for size, cnt in ordered_tangerine:
        accumulate += cnt
        answer += 1
        if accumulate >= k:
            return answer


# 실행 결과: 성공