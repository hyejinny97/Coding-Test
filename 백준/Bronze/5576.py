# https://www.acmicpc.net/problem/5576
# 문제5576번.콘테스트
# 시간: 1초, 메모리: 128MB



# 입력
'''
1. 처음 10개 줄은 W대학의 각 참가자의 검수
2. 다음 10개 줄은 K대학의 각 참가자의 점수
'''



# 출력
'''
1. W대학 점수와 K대학 점수를 순서대로 공백으로 구분하여 출력
'''



# 코드 1
import sys

sys.stdin = open('input_text/5576.txt')

# K대학
K = [int(input()) for _ in range(10)]
K.sort(reverse=True)
print(sum(K[:3]), end=' ')

# W대학
W = [int(input()) for _ in range(10)]
W.sort(reverse=True)
print(sum(W[:3]))



# 실행 결과: 성공(메모리:30840kb, 시간:84ms)



# 코드 2
import sys

sys.stdin = open('input_text/5576.txt')

for _ in range(2):
    university = [int(input()) for _ in range(10)]
    university.sort(reverse=True)
    print(sum(university[:3]), end=' ')



# 실행 결과: 성공(메모리:30840kb, 시간:76ms)