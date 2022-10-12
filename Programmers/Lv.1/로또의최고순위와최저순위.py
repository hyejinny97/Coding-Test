# https://school.programmers.co.kr/learn/courses/30/lessons/77484
# 코딩테스트연습 < 2021 Dev-Matching: 웹 백엔드 개발 < 문제.로또의 최고 순위와 최저 순위



# 입력
'''
1. 로또 번호를 담은 배열 lottos
- lottos의 길이 = 6
- 0 <= 원소 <= 45
- 0: 알아볼 수 없는 숫자
2. 당첨 번호를 담은 배열 win_nums
- win_nums의 길이 = 6
- 1 <= 원소 <= 45
'''



# 출력
'''
1. 당첨 가능한 최고 순위와 최저 순위를 차례대로 배열에 담아서 return
'''


# 코드 1
import sys

sys.stdin = open('input_text/로또의최고순위와최저순위.txt')


def solution(lottos, win_nums):
    cnt_0 = 0   # 0의 갯수
    check = 0   # 일치하는 숫자의 갯수
    for num in lottos:
        if num == 0:
            cnt_0 += 1
        elif num in win_nums:
            check += 1
    
    # 최고 순위, 최저 순위
    max_rate = 6 if check + cnt_0 < 2 else 7 - (check + cnt_0)
    min_rate = 6 if check < 2 else 7 - check
    return [max_rate, min_rate]
        

# 실행 결과: 성공



# 코드 2
import sys

sys.stdin = open('input_text/로또의최고순위와최저순위.txt')


def solution(lottos, win_nums):
    cnt_0 = 0   # 0의 갯수
    check = 0   # 일치하는 숫자의 갯수
    for num in lottos:
        if num == 0:
            cnt_0 += 1
        elif num in win_nums:
            check += 1
    
    # 최고 순위, 최저 순위
    rank = [6, 6, 5, 4, 3, 2, 1]   # 인덱스:맞은 숫자 개수, 값: 순위
    return [rank[cnt_0 + check], rank[check]]
        

# 실행 결과: 성공