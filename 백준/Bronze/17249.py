# https://www.acmicpc.net/problem/17249
# 문제17249번.태보태보 총난타
# 시간: 1초, 메모리: 128MB



# 입력
'''
1. 문자열
- 0 < 문자열 길이 <= 1,000
'''



# 출력
'''
1. 왼손의 잔상의 수, 오른손의 잔상의 수
'''



# 코드
import sys

sys.stdin = open('input_text/17249.txt')

word = input()

cnt = 0
idx = 0
while idx < len(word):
    # 얼굴을 기준으로 다시 카운트
    if word[idx] == '(':
        print(cnt, end=' ')
        idx += 4
        cnt = 0    # 카운트 초기화
    
    # 잔상 카운트
    if word[idx] == '@':
        cnt += 1
    idx += 1

print(cnt)

# 실행 결과: 성공(메모리:30840kb, 시간:68ms)