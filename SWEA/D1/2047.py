# 문제2047.신문 헤드라인
# 시간: 30초, 메모리: 256MB

# 입력
'''
1. 문자열
'''

# 출력
'''
1. 문자열의 소문자를 모두 대문자로 변경된 결과 출력
'''

# 접근 방법
'''
풀이1) upper()함수 사용
풀이2) 아스키 코드에서 알파벳 대문자 A~Z는 65~90, 알파벳 소문자 a~z는 97~122에 해당
'''

# 코드 1
import sys

sys.stdin = open('SWEA/input_text/2047.txt', 'r')

string = input()
print(string.upper())

# 실행 결과: 성공(메모리:56,692 kb, 시간:127 ms)

# 코드 2
sys.stdin = open('SWEA/input_text/2047.txt', 'r')

string = input()
for char in string:
    if char.islower():
        print(chr(ord(char) - 32), end='')
    else:
        print(char, end='')

# 실행 결과: 성공(메모리:56,692 kb, 시간:137 ms)