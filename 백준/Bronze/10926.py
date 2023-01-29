# https://www.acmicpc.net/problem/10926
# 문제10926번.??!
# 시간: 1초, 메모리: 256MB



# 입력
'''
1. 사이트에 이미 존재하는 아이디
- 알파벳 소문자로 구성
- 0 < 아이디 길이 <= 50
'''



# 출력
'''
1. 준하의 놀람을 출력
- 놀람은 아이디 뒤에 ??!를 붙여서 나타냄
'''



# 코드
import sys

sys.stdin = open('input_text/10926.txt')

id = input()
print(f'{id}??!')


# 실행 결과: 성공(메모리:30864kb, 시간:68ms)