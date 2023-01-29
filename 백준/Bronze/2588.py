# https://www.acmicpc.net/problem/2588
# 문제2588번.곱셈
# 시간: 1초, 메모리: 128MB



# 입력
'''
1. (1)의 위치에 들어갈 세 자리 자연수
2. (2)의 위치에 들어갈 세자리 자연수
'''



# 출력
'''
1. 첫째 줄부터 넷째 줄까지 차례대로 (3), (4), (5), (6)에 들어갈 값을 출력
'''



# 코드
import sys

sys.stdin = open('input_text/2588.txt')

num1 = int(input())
num2 = int(input())
reversed_num2 = str(num2)[::-1]
for n in reversed_num2:
    print(num1 * int(n))
print(num1 * num2)


# 실행 결과: 성공(메모리:30840kb, 시간:76ms)