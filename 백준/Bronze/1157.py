# https://www.acmicpc.net/problem/1157
# 문제1157번.단어 공부
# 시간제한:2초, 메모리제한:128MB



# 입력
'''
1. 단어
- 알파벳 대소문자로 이루어져 있음
- 0 < 단어 길이 <= 1,000,000
'''



# 출력
'''
1. 단어에서 가장 많이 사용된 알파벳을 대문자로 출력
- 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력
- 대문자와 소문자는 구분하지 않음
'''



# 코드
import sys

sys.stdin = open('input_text/1157.txt')

word = input()
alphabets = [0] * 26   # index: 알파벳 26개, value: 개수

# 단어에 사용된 각 알파벳 개수 카운트
for char in word:
    if 97 <= ord(char) <= 122:   # 소문자인 경우(97 ~ 122)
        alphabets[ord(char) - 97] += 1
    else:   # 대문자인 경우(65 ~ 90)
        alphabets[ord(char) - 65] += 1

# 가장 많이 사용된 알파벳 찾기
max_val = 0   # 최댓값
chars = []   # 가장 많이 사용된 알파벳
for i in range(26):
    if alphabets[i] > max_val:
        max_val = alphabets[i]
        chars = [i]
    elif alphabets[i] == max_val:
        chars.append(i)

print('?' if len(chars) > 1 else chr(chars[0] + 65))


# 실행결과(메모리:33212KB, 시간:312ms)