# https://www.acmicpc.net/problem/10773
# 문제10773번.제로
# 시간: 1초, 메모리: 256MB



# 입력
'''
1. 정수 K
- 1 ≤ K ≤ 100,000
2. K개의 줄에 정수가 1개씩 주어짐
- 정수가 "0" 일 경우에는 가장 최근에 쓴 수를 지우고, 아닐 경우 해당 수를 쓴다
'''



# 출력
'''
1. 최종적으로 적어 낸 수의 합을 출력
'''



# 코드 
import sys

sys.stdin = open('input_text/10773.txt')

K = int(input())

stack = []
for _ in range(K):
    num = int(input())
    if num:
        stack.append(num)
        continue
    stack.pop()

print(sum(stack))


# 실행 결과: 성공(메모리:32036kb, 시간:3920ms)