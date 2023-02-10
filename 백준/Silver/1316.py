# https://www.acmicpc.net/problem/1316
# 문제1316번.그룹 단어 체커
# 시간: 2초, 메모리: 128MB



# 입력
'''
1. 단어의 개수 N
- 0 < N <= 100
2. N개의 줄에 단어
- 알파벳 소문자로 구성
- 0 < 단어 길이 <= 100
'''



# 출력
'''
1. 그룹 단어의 개수를 출력

<그룹 단어>
- 각 문자가 연속해서 나타나는 단어
'''



# 코드
import sys

sys.stdin = open('input_text/1316.txt')

N = int(input())
group_word = 0   # 그룹 단어 개수

for _ in range(N):
    word = input()
    record = set()   # 이전에 나온 알파벳 기록
    for i in range(len(word)):
        # 그룹 단어가 아닌 경우
        if word[i] in record:
            break
        
        # 그룹 알파벳이 끝날 때 기록
        if i + 1 < len(word) and word[i] == word[i + 1]:
            continue
        record.add(word[i])
    else:
        group_word += 1

print(group_word)


# 실행 결과: 성공(메모리:31256kb, 시간:44ms)