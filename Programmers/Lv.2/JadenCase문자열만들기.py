# https://school.programmers.co.kr/learn/courses/30/lessons/12951
# 코딩테스트연습 < 연습문제 < 문제.JandenCase 문자열 만들기



# 입력
'''
1. 문자열 s
- 1 <= s <= 200
- s는 알파벳과 숫자, 공백문자(" ")로 이루어져 있음
- 숫자는 단어의 첫 문자로만 나음
- 공백문자가 연속해서 나올 수 있음
'''



# 출력
'''
1. s를 JadenCase로 바꾼 문자열을 리턴
- JadenCase란 모든 단어의 첫 문자가 대문자이고, 그 외의 알파벳은 소문자인 문자열
- 단, 첫 문자가 알파벳이 아닐 때에는 이어지는 알파벳은 소문자
'''


# 코드 1
import sys

sys.stdin = open('input_text/JandenCase문자열만들기.txt')

def solution(s):
    words = s.split()
    answer = []
    for word in words:
        temp = ''
        for i in range(len(word)):
            if i == 0 and word[0].isalpha:
                temp += word[0].upper()
            elif word[i].isupper():
                temp += word[i].lower()
            else:
                temp += word[i]
        answer.append(temp)
    
    return ' '.join(answer)


# 실행 결과: 실패(부분 성공)




# 코드 2
import sys

sys.stdin = open('input_text/JandenCase문자열만들기.txt')

def solution(s):
    answer = s[0].upper()
    for i in range(1, len(s)):
        if s[i - 1] == ' ' and s[i] != ' ':
            answer += s[i].upper()
        else:
            answer += s[i].lower()
    
    return answer


# 실행 결과: 성공