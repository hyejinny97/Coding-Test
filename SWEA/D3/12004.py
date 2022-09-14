# 문제12004번.구구단1
# 시간: 3초, 메모리: 256MB



# 입력
'''
1. 테스트 케이스 T
2. 정수 N
- 1 <= N <= 100
'''



# 출력
'''
1. #{테스트케이스} {N 이 1 이상 9 이하의 두 수 a, b의 곱으로 표현될 수 있으면 “Yes”, 아니면 “No”}
'''



# 코드
import sys

sys.stdin = open('../input_text/12004.txt')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    answer = 'No'
    for n in range(1, 9 + 1):
        if N % n == 0 and 1 <= N // n <= 9:
            answer = 'Yes'
            break
    print(f'#{test_case} {answer}')
    

    
# 실행 결과: 성공(메모리:56,940 kb, 시간:138 ms)