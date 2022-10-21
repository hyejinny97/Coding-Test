# https://school.programmers.co.kr/learn/courses/30/lessons/12930
# 코딩테스트연습 < 연습문제 < 문제.이상한 문자 만들기



# 입력
'''
1. 문자열 s
- 한 개 이상의 단어로 구성
'''



# 출력
'''
1. 각 단어의 짝수번째 알파벳은 대문자로, 홀수번째 알파벳은 소문자로 바꾼 문자열을 리턴
- 문자열 전체의 짝/홀수 인덱스가 아니라, 단어(공백을 기준)별로 짝/홀수 인덱스를 판단해야함
- 첫 번째 글자는 0번째 인덱스로 보아 짝수번째 알파벳으로 처리해야함
'''



# 코드 
import sys

sys.stdin = open('input_text/이상한문자만들기.txt')

def solution(s):
    words = s.split(' ')
    answer = []
    for word in words:
        temp = ''
        for i in range(len(word)):
            if i % 2 == 0:
                temp += word[i].upper()
            else:
                temp += word[i].lower()
        answer.append(temp)
    return ' '.join(answer)


# 실행 결과: 성공