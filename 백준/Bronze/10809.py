# https://www.acmicpc.net/problem/10809
# 문제10809번.알파벳 찾기
# 시간제한:1초, 메모리제한:256MB



# 입력
'''
1. 단어 S
- 알파벳 소문자로만 이루어져 있음
- 0 < S <= 100
'''



# 출력
'''
1. 각각의 알파벳에 대해서, 단어에 포함되어 있는 경우에는 처음 등장하는 위치를, 포함되어 있지 않은 경우에는 -1을 출력
- 단어의 첫 번째 글자는 0번째 위치
'''



# 코드
import sys

sys.stdin = open('input_text/10809.txt')

word = input()
locations = ['-1'] * 26   # index: 알파벳 소문자 26개, value: 처음 등장 위치

for i in range(len(word)):
    char = word[i]
    if locations[ord(char) - 97] == '-1':
        locations[ord(char) - 97] = str(i)

print(' '.join(locations))


# 실행결과(메모리:31256KB, 시간:44ms)