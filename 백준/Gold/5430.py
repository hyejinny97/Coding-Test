# https://www.acmicpc.net/problem/5430
# 문제5430번.AC
# 시간: 1초, 메모리: 256MB



# 입력
'''
1. 테스트 케이스의 개수 T
- 0 < T <= 100
2. 수행할 함수 p
- 1 <= p 길이 <= 100,000
- 'R': 뒤집는 함수
- 'D': 첫 번째 수를 버리는 함수
3. 배열에 들어있는 수의 개수 n
- 0 ≤ n ≤ 100,000
4. [x1,...,xn]과 같은 형태로 배열에 들어있는 정수
- 1 ≤ xi ≤ 100
'''



# 출력
'''
1. 각 테스트 케이스에 대해서, 입력으로 주어진 정수 배열에 함수를 수행한 결과를 출력
- 배열이 비어있는데 D를 사용한 경우에는 error를 출력
'''



# 코드
import sys, re
from collections import deque

sys.stdin = open('input_text/5430.txt')

T = int(input())
for _ in range(T):
    functions = input()
    N = int(input())
    arr = deque(re.compile('[0-9]+').findall(input()))

    front = True   # 배열을 앞에서 읽음
    error = False    
    for func in functions:
        if func == 'R':
            front = not front
        if func == 'D':
            if not arr:
                error = True
                print('error')
                break

            if front:
                arr.popleft()
            else:
                arr.pop()
    
    if not error:
        if front:
            print(f"[{','.join(arr)}]")
        else:
            print(f"[{','.join(reversed(arr))}]")


# 실행 결과: 성공(메모리:43256kb, 시간:352ms)