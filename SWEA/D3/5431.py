# 문제5431번.민석이의 과제 체크하기
# 시간: 4초, 메모리: 256MB



# 입력
'''
1. 테스트 케이스 T
2. 수강생 수 N, 과제를 제출한 사람의 수 K
- 2 <= N <= 100
- 1 <= K <= N
3. K개의 과제를 제출한 사람의 번호
- 1 <= 번호 <= N
'''



# 출력
'''
1. #{테스트케이스} {과제를 제출하지 않은 사람의 번호를 오름차순으로 출력}
'''



# 코드 1
import sys

sys.stdin = open('../input_text/5431.txt')

T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    nums = list(map(int, input().split()))

    # 과제를 제출한 사람 체크
    submit = [0] * (N + 1)
    for num in nums:
        submit[num] = 1
    
    # 과제를 제출하지 않은 사람 찾기
    rst = []
    for i in range(1, N + 1):
        if not submit[i]:
            rst.append(i)
    
    print(f'#{test_case}', *rst)



# 실행 결과: 성공(메모리:64,584 kb, 시간:382 ms)



# 코드 2
import sys

sys.stdin = open('../input_text/5431.txt')

T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    nums = set(map(int, input().split()))

    # 과제를 제출하지 않은 사람 찾기
    rst = []
    for n in range(1, N + 1):
        if n not in nums:
            rst.append(n)

    print(f'#{test_case}', *rst)



# 실행 결과: 성공(메모리:64,868 kb, 시간:378 ms)