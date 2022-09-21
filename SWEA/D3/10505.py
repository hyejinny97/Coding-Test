# 문제10505번.소득 불균형
# 시간: 2초, 메모리: 256MB



# 입력
'''
1. 테스트 케이스 T
2. 정수의 갯수 N
- 1 <= N <= 10,000
3. 각 사람의 소득을 뜻하는 N개의 양의 정수
- 1 <= 정수 <= 100,000
'''



# 출력
'''
1. #{테스트케이스} {평균 이하의 소득을 가진 사람들의 수}
'''



# 코드 
import sys

sys.stdin = open('../input_text/10505.txt')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    incomes = list(map(int, input().split()))

    # 평균 소득
    avg = sum(incomes) / len(incomes)

    # 평균 소득 이하의 사람의 수
    cnt = 0
    for income in incomes:
        if income <= avg:
            cnt += 1
    
    print(f'#{test_case} {cnt}')



# 실행 결과: 성공(메모리:63,656 kb, 시간:206 ms)