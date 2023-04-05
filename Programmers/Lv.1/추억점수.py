# https://school.programmers.co.kr/learn/courses/30/lessons/176963
# 코딩테스트연습 < 연습문제 < 문제.추억 점수



# 입력
'''
1. 그리워하는 사람의 이름을 담은 문자열 배열 name
- 3 ≤ name의 원소의 길이 ≤ 7
2. 각 사람별 그리움 점수를 담은 정수 배열 yearning
- 3 ≤ name의 길이 = yearning의 길이≤ 100
- 1 ≤ yearning[i] ≤ 100
3. 각 사진에 찍힌 인물의 이름을 담은 이차원 문자열 배열 photo
- 3 ≤ photo의 길이 ≤ 100
'''



# 출력
'''
1. 사진들의 추억 점수를 photo에 주어진 순서대로 배열에 담아 return
'''



# 코드 
import sys

sys.stdin = open('input_text/추억점수.txt')

def solution(names, yearning, photos):
    missing = dict(zip(names, yearning))
    rst = []
    for photo in photos:
        photo_score = 0
        for name in photo:
            photo_score += missing.get(name, 0)
        rst.append(photo_score)

    return rst


# 실행 결과: 성공