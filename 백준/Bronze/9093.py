# https://www.acmicpc.net/problem/9093
# 문제9093번.단어 뒤집기
# 시간: 1초, 메모리: 128MB



# 입력
'''
1. 테스트 케이스 수 T
2. 문장
- 단어 길이 <= 20
- 문장 길이 <= 1,000
'''



# 출력
'''
1. 문자의 단어를 모두 뒤집어 출력
'''



# 코드
import sys

sys.stdin = open('input_text/9093.txt')

T = int(input())
for _ in range(T):
    strings = input().split()
    for word in strings:
        print(word[::-1], end=' ')
    print()



# 실행 결과: 성공(메모리:30840kb, 시간:784ms)