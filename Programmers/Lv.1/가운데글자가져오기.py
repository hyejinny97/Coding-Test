# https://school.programmers.co.kr/learn/courses/30/lessons/12903
# 코딩테스트연습 < 연습문제 < 문제.가운데 글자 가져오기



# 입력
'''
1. 단어 s
- 1 <= 길이 <= 100
'''



# 출력
'''
1. 단어 s의 가운데 글자를 반환
- 단어의 길이가 짝수라면 가운데 두글자를 반환
'''



# 코드 1
import sys

sys.stdin = open('input_text/가운데글자가져오기.txt')

def solution(s):
    if len(s) % 2 == 1:
        return s[len(s) // 2]
    else:
        return s[len(s) // 2 - 1:len(s) // 2 + 1]


# 실행 결과: 성공



# 코드 2
import sys

sys.stdin = open('input_text/가운데글자가져오기.txt')

def solution(s):
    return s[(len(s) - 1) // 2:len(s) // 2 + 1]


# 실행 결과: 성공