# https://www.acmicpc.net/problem/20920
# 문제20920번.영단어 암기는 괴로워
# 시간: 1초, 메모리: 1024MB



# 입력
'''
1. 영어 지문에 나오는 단어의 개수 N, 외울 단어의 길이 기준이 되는 M
- 1 <= N <= 100,000 
- 1 <= M <= 10
2. N개의 줄에 외울 단어를 입력받음
- 0 < 단어 길이 <= 10
'''



# 출력
'''
1. 화은이의 단어장에 들어 있는 단어를 단어장의 앞에 위치한 단어부터 한 줄에 한 단어씩 순서대로 출력
- 단어 길이가 M 이상인 단어들만 외움

<단어장의 단어 순서 우선순위>
1. 자주 나오는 단어일수록 앞에 배치한다.
2. 해당 단어의 길이가 길수록 앞에 배치한다.
3. 알파벳 사전 순으로 앞에 있는 단어일수록 앞에 배치한다
'''



# 코드 1
import sys

sys.stdin = open('input_text/20920.txt')

N, M = map(int, input().split())

words = dict()  # key: 단어, value: 단어 등장 개수
for _ in range(N):
    word = input()
    if len(word) < M:
        continue
    words[word] = words.get(word, 0) + 1

print('\n'.join(sorted(words, key=lambda word: (-words[word], -len(word), word))))


# 실행 결과: 시간 초과



# 코드 2
import sys

sys.stdin = open('input_text/20920.txt')

N, M = map(int, sys.stdin.readline().strip().split())

words = dict()  # key: 단어, value: 단어 등장 개수
for _ in range(N):
    word = sys.stdin.readline().strip()
    if len(word) < M:
        continue
    words[word] = words.get(word, 0) + 1

print('\n'.join(sorted(words, key=lambda word: (-words[word], -len(word), word))))


# 실행 결과: 성공(메모리:53296kb, 시간:252ms)