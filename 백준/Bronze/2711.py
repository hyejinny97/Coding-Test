# https://www.acmicpc.net/problem/2711
# 문제2711번.오타맨 고창영
# 시간: 1초, 메모리: 128MB



# 입력
'''
1. 테스트케이스 T
- 1 <= T <= 1,000
2. 오타를 낸 위치, 문자열
- 문자열의 가장 첫문자는 1번째 문자
- 0 < 문자열 길이 <= 80
- 문자열은 대문자로만 이루어짐
'''



# 출력
'''
1. 오타를 지운 문자열 출력
'''



# 코드
import sys

sys.stdin = open('input_text/2711.txt')

T = int(input())
for _ in range(T):
    loc, word = input().split()
    rst = ''
    for idx in range(len(word)):
        if idx != int(loc) - 1:
            rst += word[idx]
    print(rst)


# 실행 결과: 성공(메모리:30840kb, 시간:76ms)