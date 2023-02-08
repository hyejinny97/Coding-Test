# https://www.acmicpc.net/step/7
# 문제11654번.아스키 코드
# 시간제한:1초, 메모리제한:256MB



# 입력
'''
1. 알파벳 소문자, 대문자, 숫자 0-9 중 하나가 주어짐
'''



# 출력
'''
1. 입력으로 주어진 글자의 아스키 코드 값을 출력
'''



# 코드
import sys

sys.stdin = open('input_text/11654.txt')

val = input()
print(ord(val))


# 실행결과(메모리:31256KB, 시간:44ms)