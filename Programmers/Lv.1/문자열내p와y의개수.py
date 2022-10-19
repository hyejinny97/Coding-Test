# https://school.programmers.co.kr/learn/courses/30/lessons/12916
# 코딩테스트연습 < 연습문제 < 문제.문자열 내 p와 y의 개수



# 입력
'''
1. 대문자와 소문자가 섞여있는 문자열 s
- s의 길이 <= 50
'''



# 출력
'''
1. s에 'p'의 개수와 'y'의 개수를 비교해 같으면 True, 다르면 False를 return
- 'p', 'y' 모두 하나도 없는 경우는 항상 True를 리턴
- 단, 개수를 비교할 때 대문자와 소문자는 구별하지 않음
'''



# 코드 
import sys

sys.stdin = open('input_text/문자열내p와y의개수.txt')

def solution(s):
    answer = True
    dic = {'p':0, 'y':0}
    for ele in s:
        if ele == 'p' or ele == 'P':
            dic['p'] += 1
        elif ele == 'y' or ele == 'Y':
            dic['y'] += 1

    if dic['p'] == dic['y']:
        return True
    else:
        return False


# 실행 결과: 성공