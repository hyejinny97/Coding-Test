# https://www.acmicpc.net/problem/10798
# 문제10798번.세로 읽기
# 시간: 1초, 메모리: 256MB



# 입력
'''
1. 5개의 줄에는 최소 1개 최대 15개의 글자들이 연속으로 주어짐
- 영어 대문자, 영어 소문자, 숫자
'''



# 출력
'''
1. 세로로 읽은 순서대로 글자들을 공백없이 출력
'''



# 코드 1 - 이 방법으로 풀면 크기가 다른 문자열은 틀리게 된다
'''
import sys

sys.stdin = open('input_text/10798.txt')

for ver in zip(*[input() for _ in range(5)]):
    print(*ver, sep='', end='')



# 실행 결과: 성공(메모리:30864kb, 시간:68ms)
'''



# 코드 2
import sys

sys.stdin = open('input_text/10798.txt')

max_len = 0
words = []
for _ in range(5):
    word = input()
    max_len = max(max_len, len(word))
    words.append(word)

for i in range(max_len):   # 각 단어의 인덱스
    for j in range(5):   # 5개의 단어
        if i > len(words[j]) - 1:
            continue
        print(words[j][i], end='')



# 실행 결과: 성공(메모리:30840kb, 시간:72ms)
