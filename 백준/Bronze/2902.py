# https://www.acmicpc.net/problem/2902
# 문제2902번.KMP는 왜 KMP일까?
# 시간: 1초, 메모리: 128MB



# 입력
'''
1. 영어 알파벳 (대문자, 소문자, 하이픈으로 구성)
- 최대 100글자
'''



# 출력
'''
1. 짧은 형태 이름을 출력
'''



# 코드
import sys, collections

sys.stdin = open('input_text/2902.txt')

names = input().split('-')

for name in names:
    print(name[0], end='')



# 실행 결과: 성공(메모리:30840kb, 시간:72ms)