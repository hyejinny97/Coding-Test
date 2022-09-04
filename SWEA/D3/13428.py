# 문제13428번.숫자 조작
# 시간: 3초, 메모리: 256MB



# 입력
'''
1. 테스트 케이스 T
2. 음이 아닌 정수 N
- 0 <= N <= 999,999,999
'''



# 출력
'''
1. #{테스트케이스} {M의 최솟값} {M의 최댓값}
- 정수 N에서 한 쌍의 숫자를 골라 그 위치를 바꾸는 일을 최대 한 번 하여(안 하거나, 한 번만 하여) 새로운 수 M을 만들 수 있음
- M의 맨 앞에 ‘0’이 나타나면 안 됨
'''



# 코드 1
import sys

sys.stdin = open('../input_text/13428.txt')

def swap(N, sorted_N):
    # N과 sorted_N를 앞에서부터 차례로 순회하면서 비교
    for i in range(len(N)):
        if N[i] != sorted_N[i]:
            # sorted_N[i]의 값을 N[i]의 값과 스왑해줘야 함
            # N[i]의 값을 최대한 뒤로 보내기 위해
            # N을 뒤에서 부터 순회하면서 sorted_N[i]의 값이 가장 처음 나오는 인덱스 찾아 스왑
            for j in range(len(N) - 1, 0 - 1, -1):
                if N[j] == sorted_N[i]:
                    N[i], N[j] = N[j], N[i]
                    return N
    # 현재 값이 최소/최대값인 경우
    return N


T = int(input())
for test_case in range(1, T + 1):
    print(f'#{test_case}', end=' ')
    N1 = list(input())
    N2 = N1.copy()

    # M의 최솟값 구하기
    sorted_N1 = sorted(N1)   # 순방향 정렬
    # sorted_N의 0번 인덱스의 값이 0인 경우, 0이상 값이 나오는 인덱스와 스왑
    if sorted_N1[0] == '0':
        for i in range(1, len(N1)):
            if sorted_N1[i] != '0':
                sorted_N1[0], sorted_N1[i] = sorted_N1[i], sorted_N1[0]
    print(''.join(swap(N1, sorted_N1)), end=' ')

    # M의 최댓값 구하기
    sorted_N2 = sorted(N2, reverse=True)   # 역방향 정렬
    print(''.join(swap(N2, sorted_N2)))
    
    

# 실행 결과: 실패(100개의 테스트케이스 중 51개 통과)



# 코드 2
import sys
from itertools import combinations

sys.stdin = open('../input_text/13428.txt')

T = int(input())
for test_case in range(1, T + 1):
    N = list(input())
    
    # M의 최솟값/최댓값 구하기
    max_M, min_M = int(''.join(N)), int(''.join(N))
    for i, j in combinations(range(0, len(N)), 2):
        # i인덱스 값과 j인덱스 값 스왑
        N[i], N[j] = N[j], N[i]

        # N의 젤 앞자리가 0인 경우, 원상복구
        if N[0] == '0':
            N[i], N[j] = N[j], N[i]
            continue
        
        new = int(''.join(N))
        min_M = min(min_M, new)   # M 최솟값 갱신
        max_M = max(max_M, new)   # M 최댓값 갱신
        
        # N 원상복구
        N[i], N[j] = N[j], N[i]
    
    # N이 한자리 수인 경우
    if len(N) == 1:
        print(f'#{test_case} {int(N[0])} {int(N[0])}')
    else:
        print(f'#{test_case} {min_M} {max_M}')
    
    

# 실행 결과: 성공(메모리:61,736 kb, 175 ms)