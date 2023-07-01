# https://www.acmicpc.net/problem/16139
# 문제16139번.인간-컴퓨터 상호작용
# 시간: 1초, 메모리: 256MB



# 입력
'''
1. 문자열 S
- 0 < 문자열 길이 <= 200,000
- 알파벳 소문자로만 구성
2. 질문의 수 q
- 1 <= q <= 200,000
3. q줄마다 질문(알파벳 소문자 x, l, r)
- [l, r]: 문자열의 구간 
- 0 <= l <= r < S
'''



# 출력
'''
1. 각 질문마다 S의 l번째 문자부터 r번째 문자 사이에 x가 나타나는 횟수 출력
- 문자는 0번째부터 셈
- l번째와 r번째 문자를 포함해서 생각
'''



# 코드 1
import sys

sys.stdin = open('input_text/16139.txt')

# 문자열 각 알파벳 위치 찾기
string = input()
new_string = {}
for i in range(len(string)):
    if new_string.get(string[i]):
        new_string[string[i]].append(i)
    else:
        new_string[string[i]] = [i]

num_questions = int(input())
for _ in range(num_questions):
    char, start, end = input().split()
    start, end = int(start), int(end)
    if new_string.get(char):
        cnt = 0
        for i in new_string.get(char):
            if start <= i <= end:
                cnt += 1
        print(cnt)
    else:
        print(0)


# 실행 결과: 성공 - 50점(메모리:31256kb, 시간:232ms)



# 코드 2
import sys

sys.stdin = open('input_text/16139.txt')

# 문자열 각 인덱스까지 각 알파벳 수 누적하기
string = input()     # aba
acc_strings = [dict(zip('abcdefghijklmnopqrstuvwxyz', [0] * 26))]   # [{...}, {a: 1, ...}, {a: 1, b: 1, ...}, {a: 2, b: 1, ...}]
for char in string:
    new_string = acc_strings[-1].copy()
    new_string[char] += 1
    acc_strings.append(new_string)

num_questions = int(input())
for _ in range(num_questions):
    char, start, end = input().split()
    print(acc_strings[int(end) + 1][char] - acc_strings[int(start)][char])


# 실행 결과: 성공 - 50점(메모리:31912kb, 시간:220ms)