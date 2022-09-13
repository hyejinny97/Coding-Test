# 문제11736번.평범한 숫자
# 시간: 2초, 메모리: 256MB



# 입력
'''
1. 테스트 케이스 T
2. 순열 길이 N
- 3 <= N <= 20
3. N개의 정수 p
- 3 <= p <= N
- 모든 p는 서로 다름
'''



# 출력
'''
1. #{테스트케이스} {주어진 순열에서 평범한 숫자의 개수}
<평범한 숫자 정의 방법>
- pi-1, pi, pi+1 중 pi가 최솟값도, 최댓값도 아니라면 pi를 평범한 숫자라고 정의
'''



# 코드
import sys

sys.stdin = open('../input_text/11736.txt')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))
    normal_num = 0   # 평범힌 숫자 개수
    for i in range(1, N - 1):
        if nums[i - 1] < nums[i] < nums[i + 1] or nums[i - 1] > nums[i] > nums[i + 1]:
            normal_num += 1
    
    print(f'#{test_case} {normal_num}')

    
   
# 실행 결과: 성공(메모리:56,692 kb, 시간:141 ms)