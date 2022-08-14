# https://www.acmicpc.net/problem/1264
# 문제1264번.모음의 개수
# 시간: 1초, 메모리: 128MB



# 입력
'''
1. 각 줄마다 문장이 주어짐
- 최대 255글자
2. 입력 종료 조건: #
'''



# 출력
'''
1. 각 줄마다 모음의 갯수(대소문자 포함) 출력
'''



# 코드
import sys

sys.stdin = open('input_text/1264.txt')

alph = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
while True:
    sentance = input()
    
    # 입력 종료 조건
    if sentance == '#':
        break
    
    # 모음 갯수 세기
    cnt = 0
    for char in sentance:
        if char in alph:
            cnt += 1
    
    print(cnt)



# 실행 결과: 성공(메모리:30840kb, 시간:68ms)