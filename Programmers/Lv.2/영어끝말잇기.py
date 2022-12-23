# https://school.programmers.co.kr/learn/courses/30/lessons/12981
# 코딩테스트연습 < Summer/Winter Coding(~2018) < 문제.영어 끝말잇기



# 입력
'''
1. 사람의 수 n, 사람들이 순서대로 말한 단어 words
- 2 <= n <= 10
- n <= words 길이 <= 100
- 2 <= 단어 길이 <= 50
- 단어는 알파벳 소문자로만 이루어짐
'''



# 출력
'''
1. [가장 먼저 탈락하는 사람의 번호, 그 사람이 자신의 몇 번째 차례에 탈락하는지 차례] 형태로 return
- 만약 주어진 단어들로 탈락자가 생기지 않는다면, [0, 0]을 return

<영어 끝말잇기 규칙> 
- 앞사람이 말한 단어의 마지막 문자로 시작하는 단어를 말해야 함
- 이전에 등장했던 단어는 사용할 수 없음
- 한 글자인 단어는 인정되지 않음
'''


# 코드 
import sys

sys.stdin = open('input_text/영어끝말잇기.txt')

def solution(n, words):
    if len(words[0]) > 1:
        words_set = {words[0]}
    else:
        return [1, 1]
    
    for i in range(1, len(words)):
        person, order = i % n + 1, i // n + 1
        if len(words[i]) <= 1:
            return [person, order]
        if words[i] in words_set:
            return [person, order]
        if words[i][0] != words[i - 1][-1]:
            return [person, order]
        words_set.add(words[i])
    
    return [0, 0]


# 실행 결과: 성공