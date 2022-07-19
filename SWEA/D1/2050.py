# 문제2050.알파벳을 숫자로 변환
# 시간: 30초, 메모리: 256MB

# 입력
'''
1. 알파벳으로 이루어진 문자열
- 문자열길이 <= 200
'''

# 출력
'''
1. 각 알파벳을 숫자로 변환한 결과값을 빈 칸을 두고 출력
'''

# 접근 방법
'''
아스키 코드에서 알파벳 A는 65, Z는 90에 해당
'''

# 코드
import sys

sys.stdin = open('SWEA/input_text/2050.txt', 'r')

string = input()
for char in string:
    print(ord(char) - 64, end=' ')

# 실행 결과: 성공(메모리:56,960 kb , 시간:127 ms)