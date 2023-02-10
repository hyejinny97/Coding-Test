# https://www.acmicpc.net/problem/2941
# 문제2941번.크로아티아 알파벳
# 시간: 1초, 메모리: 128MB



# 입력
'''
1. 크로아티아 알파벳으로 이루어진 단어
- 0 < 단어 길이 <= 100
- 알파벳 소문자와 '-', '='로만 이루어짐
'''



# 출력
'''
1. 단어가 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력

<변경된 크로아티아 알파벳>
- c=, c-, dz=, d-, lj, nj, s=, z=
- 위에 없는 알파벳은 한 글자씩 셈
'''



# 코드
import sys

sys.stdin = open('input_text/2941.txt')

word = input()
croatia_alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for alpha in croatia_alphabet:
    word = word.replace(alpha, '*')

print(len(word))


# 실행 결과: 성공(메모리:31256kb, 시간:44ms)