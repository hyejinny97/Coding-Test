# https://school.programmers.co.kr/learn/courses/30/lessons/84512
# 코딩테스트연습 < 완전탐색 < 문제.모음 사전



# 입력
'''
1. 단어 하나 word
- 1 <= word <= 5
- 알파벳 대문자 'A', 'E', 'I', 'O', 'U'로만 이루어짐
'''



# 출력
'''
1. word가 사전에서 몇 번째 단어인지 return

<사전>
- 알파벳 모음 'A', 'E', 'I', 'O', 'U'만을 사용하여 만들 수 있는, 길이 5 이하의 모든 단어가 수록되어있음
- "A" → "AA" → ... → "UUUUU"
'''



# 코드 1

# 접근방법
'''
사전에 수록된 모든 단어의 수 = 6 x 6 x 6 x 6 x 6 = 7776 이하

char  1  2  3  4  5  6
alph  .  .  .  .  .  .
      A  A  A  A  A  A
      E  E  E  E  E  E
      I  I  I  I  I  I
      O  O  O  O  O  O
      U  U  U  U  U  U 
'''
import sys

sys.stdin = open('input_text/모음사전.txt')

def solution(word):
    def make_word(new_word, cnt):  # 중복 순열
        if cnt == 0:
            dictionary.add(new_word)
            return 
 
        for a in alphabet:
            make_word(new_word + a, cnt - 1)

    alphabet = [''] + list('AEIOU')
    dictionary = set()
    make_word('', 5)

    return sorted(dictionary).index(word)


# 실행 결과: 성공



# 코드 2
import sys
from itertools import product

sys.stdin = open('input_text/모음사전.txt')

def solution(word):
    alphabet = 'AEIOU'
    dictionary = []
    for long in range(1, 5 + 1):
        cases = product(alphabet, repeat=long)
        for case in cases:
            dictionary.append(''.join(case))
    
    dictionary.sort()

    return dictionary.index(word) + 1
print(solution("AAAAE"))


# 실행 결과: 성공