# https://www.acmicpc.net/problem/14888
# 문제14888번.연산자 끼워넣기
# 시간: 2초, 메모리: 512MB



# 입력
'''
1. 수의 개수 N
- 2 ≤ N ≤ 11
2. N개의 수 (A1, A2, ..., AN)
- 1 ≤ Ai ≤ 100
3. 차례대로 덧셈(+)의 개수, 뺄셈(-)의 개수, 곱셈(×)의 개수, 나눗셈(÷)의 개수
- 총 N-1개의 연산자
'''



# 출력
'''
1. 만들 수 있는 식의 결과의 최댓값을 출력
2. 만들 수 있는 식의 결과의 최솟값을 출력

<조건>
- 주어진 수의 순서를 바꾸면 안 된다.
- 식의 계산은 연산자 우선 순위를 무시하고 앞에서부터 진행해야 한다.
- 나눗셈은 정수 나눗셈으로 몫만 취한다.
- 음수를 양수로 나눌 때는, 양수로 바꾼 뒤 몫을 취하고, 그 몫을 음수로 바꾼다.
'''



# 코드 

# 접근 방법
'''
nums = 1 2 3 4 5 6
연산자 = 2 1 1 1

                         2111
1번째         +↓           -↓         x↓         /↓ 
              1111          2011       2101       2110
2번째   +↓  -↓   x↓   /↓ 
        0111 1011 1101 1110 
...
5번째
'''
import sys

sys.stdin = open('input_text/14888.txt')

def calculation(operator_order):
    result = nums[0]
    for i in range(len(operator_order)):
        if operator_order[i] == 0:  # 덧셈
            result += nums[i + 1]
        if operator_order[i] == 1:  # 뺄셈
            result -= nums[i + 1]
        if operator_order[i] == 2:  # 곱셈
            result *= nums[i + 1]
        if operator_order[i] == 3:  # 나눗셈
            result = -(-result // nums[i + 1]) if result < 0 else result // nums[i + 1]

    return result


def ordering_operators(record=[]):
    if len(record) == len(nums) - 1:
        results.append(calculation(record))
        return
    
    for i in range(4):
        if operators[i]:
            operators[i] -= 1
            ordering_operators(record + [i])
            operators[i] += 1


N = int(input())
nums = list(map(int, input().split()))
operators = list(map(int, input().split()))

results = []   # 연산 결과 모든 경우의 수
ordering_operators()

print(max(results), min(results), sep='\n')


# 실행 결과: 성공(메모리:31256kb, 시간:112ms)