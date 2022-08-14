# https://www.acmicpc.net/problem/1371
# 문제1371번.가장 많은 글자
# 시간: 2초, 메모리: 128MB



# 입력
'''
1. 문장
- 최대 50개 줄
- 각 줄은 최대 50개 글자
- 오직 알파벳 소문자만
'''



# 출력
'''
1. 가장 많이 나온 문자 출력
- 여러 개일 경우엔, 알파벳 사전 순으로 공백없이 출력
'''



# 코드 1
import sys
from collections import defaultdict

sys.stdin = open('input_text/1371.txt')

sentance = sys.stdin.readlines()
cnts = defaultdict(int)   # 키: 알파벳, 값: 등장 횟수

# 문장 내 알파벳 갯수 세기
for row in sentance:
    for char in row:
        cnts[char] += 1

# 가장 많이 나온 알파벳 출력
max_alph = []
max_cnt = 0
for alph in cnts:
    # 공백과 개행문자는 제외
    if alph == ' ' or alph == '\n':
        continue

    if cnts[alph] > max_cnt:
        max_cnt = cnts[alph]
        max_alph = [alph]   # 초기화
    elif cnts[alph] == max_cnt:
        max_alph.append(alph)

print(''.join(sorted(max_alph)))



# 실행 결과: 성공(메모리:32424kb, 시간:96ms)



# 코드 2
import sys

sys.stdin = open('input_text/1371.txt')

sentance = sys.stdin.readlines()
cnts = [0] * 26   # 인덱스: 알파벳, 값: 등장 횟수

# 문장 내 알파벳 갯수 세기
for row in sentance:
    for char in row:
        # 공백과 개행문자는 제외
        if char == ' ' or char == '\n':
            continue
        
        cnts[ord(char) - 97] += 1

# 가장 많이 나온 알파벳 출력
max_alph = []
max_cnt = 0
for i in range(len(cnts)):
    if cnts[i] > max_cnt:
        max_cnt = cnts[i]
        max_alph = [chr(i + 97)]   # 초기화
    elif cnts[i] == max_cnt:
        max_alph.append(chr(i + 97))

print(''.join(sorted(max_alph)))



# 실행 결과: 성공(메모리:30840kb, 시간:68ms)