# 문제6190번.정곤이의 단조 증가하는 수
# 시간: 4초, 메모리: 500MB



# 입력
'''
1. 테스트 케이스 수 T
2. 양의 정수 갯수 N 
- 1 <= N <= 1,000
3. N개의 양의 정수 
- 1 <= A <= 30,000
'''



# 출력
'''
1. #{테스트케이스} {단조 증가하는 수인 Ai x Aj중에서 그 최댓값을 출력, 없다면 -1을 출력}
<단조 증가하는 수>
- 각 숫자의 자릿수가 단순하게 증가하는 수
- 어떤 k자리 수 X = d1d2…dk 가 d1 ≤ d2 ≤ … ≤ dk 를 만족하면 단조 증가하는 수
'''



# 코드 
import sys
from itertools import combinations

sys.stdin = open('../input_text/6190.txt')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))

    # N개의 정수 중 2개 뽑아 곱하기
    select = combinations(nums, 2)
    special_nums = []   # 단조 증가하는 수들
    for fst, sec in select:
        two = str(fst * sec)   # 2개 뽑아 곱한 값
        
        # 단조 증가하는 수인지 확인
        for i in range(len(two) - 1):
            if two[i] > two[i + 1]:
                break
        else:
            special_nums.append(int(two))
    
    # 단조 증가하는 수 중 최댓값 출력
    if special_nums:
        print(f'#{test_case} {max(special_nums)}')
    else:
        print(f'#{test_case} -1')



# 실행 결과: 성공(메모리:63,292 kb, 시간:1,077 ms)