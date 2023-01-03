# https://school.programmers.co.kr/learn/courses/30/lessons/42747
# 코딩테스트연습 < 정렬 < 문제.H-index


# 입력
'''
1. 어떤 과학자가 발표한 논문의 인용 횟수를 담은 배열 citations
- 1 <= 논문의 수 n (=citations의 길이) <= 1,000
- 0 <= 인용 횟수 <= 10,000
'''



# 출력
'''
1. 과학자의 H-Index를 return
<H-Index>
- 어떤 과학자가 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 H-Index
'''


# 코드 1

# 접근방법
'''
citations = [0, 0, 1, 2, 2, 7, 9]
citations_reverse = [9, 7, 2, 2, 1, 0, 0]
       i(논문 수) =  1  2  3  4  5  6  7(편)
-----------------------------------------------
- 9번 이상 인용된 논문이 1편
- 7번 이상 인용된 논문이 2편
- 2번 이상 인용된 논문이 3편(2편 이상) => H-index = 2
'''

import sys

sys.stdin = open('input_text/H-index.txt')

def solution(citations):
    citations_reverse = sorted(citations, reverse=True)
    for i in range(len(citations_reverse)):
        if i + 1 >= citations_reverse[i]:
            return citations_reverse[i]


# 실행 결과: 부분 성공 (citations=[9, 7, 4, 2, 2, 1, 0, 0]일때, 3번 이상 인용된 논문이 3편 => H-index = 3)



# 코드 2

# 접근방법
'''
citations = [0, 0, 1, 2, 2, 7, 9]
citations_reverse = [9, 7, 4, 2, 2, 1, 0, 0]
     idx(논문 수) =  1  2  3  4  5  6  7  8(편)
     citation_std =  9
                     8
                        7
                        6
                        5
                            4
                            3   => H-index = 3
'''

import sys

sys.stdin = open('input_text/H-index.txt')

def solution(citations):
    citations_reverse = sorted(citations, reverse=True)
    idx = 0   
    citation_std = citations_reverse[0]   # 인용 횟수 기준
    while citation_std > 0:
        if (idx + 1) < len(citations) and citations_reverse[idx + 1] >= citation_std:
            idx += 1
        if idx + 1 >= citation_std:  # idx + 1 = 인용 횟수 기준 이상으로 인용된 논문 수
            return citation_std
        citation_std -= 1
    return 0


# 실행 결과: 성공



# 코드 3

# 접근방법
'''
citations = [0, 0, 1, 2, 2, 7, 9]
citations_reverse = [9, 7, 4, 2, 1, 0]
     idx(논문 수) =  1  2  3  4  5  6(편)
citation(인용 수) =  9  7  4  2  1  0 
                h =  1  2  3  2  1  0
--------------------------------------------------
- citations = [9]일 때, 1번 이상 인용된 논문이 1편 이상 => h = 1
- citations = [9, 7]일 때, 2번 이상 인용된 논문이 2편 이상 => h = 2
- citations = [9, 7, 4]일 때, 3번 이상 인용된 논문이 3편 이상 => h = 3
- citations = [9, 7, 4, 2]일 때, 2번 이상 인용된 논문이 2편 이상 => h = 2
- citations = [9, 7, 4, 2, 1]일 때, 1번 이상 인용된 논문이 1편 이상 => h = 1
- citations = [9, 7, 4, 2, 1, 0]일 때, 0번 이상 인용된 논문이 0편 이상 => h = 0
- h 값들 중에서 최댓값이 H-index이므로, H-index = 3
'''

import sys

sys.stdin = open('input_text/H-index.txt')

def solution(citations):
    citations.sort(reverse=True)
    return max(map(min, enumerate(citations, start=1)))


# 실행 결과: 성공