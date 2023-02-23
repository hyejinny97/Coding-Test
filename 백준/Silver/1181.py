# https://www.acmicpc.net/problem/1181
# 문제1181번.단어 정렬
# 시간: 2초, 메모리: 256MB



# 입력
'''
1. 단어의 개수 N
- 1 ≤ N ≤ 20,000
2. N개의 줄에 알파벳 소문자로 이루어진 단어가 입력됨
- 단어는 알파벳 소문자로 이루어짐
- 0 < 단어 길이 <= 50
'''



# 출력
'''
1. 아래 조건에 따라 단어들을 정렬한 후 출력

<정렬 조건>
1. 길이가 짧은 것부터
2. 길이가 같으면 사전 순으로
- 단, 중복된 단어는 하나만 남기고 제거해야 함
'''



# 코드 
import sys

sys.stdin = open('input_text/1181.txt')

# N개의 단어 모두 입력받기
N = int(input())
words = set()
for _ in range(N):
    words.add(input())

# 좌표가 증가하는 순으로 정렬
words = sorted(words, key=lambda word: (len(word), word))
for word in words:
    print(word)


# 실행 결과: 성공(메모리:36532kb, 시간:856ms)
