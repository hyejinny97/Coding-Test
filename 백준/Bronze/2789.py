# https://www.acmicpc.net/problem/2789
# 문제2789.유학 금지
# 시간: 1초, 메모리: 128MB



# 입력
'''
1. 알파벳 대문자로 구성된 단어
- 3 <= 단어길이 <= 100
'''



# 출력
'''
1. 단어에서 CAMBRIDGE에 포함된 알파벳을 모두 지운 뒤 출력
'''



# 코드
import sys

sys.stdin = open('input_text/2789.txt')

word = input()

remove_alp = 'CAMBRIDGE'
rst = ''
for char in word:
    if char not in remove_alp:
        rst += char

print(rst)



# 실행 결과: 성공(메모리:30840kb, 시간:68ms)