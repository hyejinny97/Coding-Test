# 문제12368번.24시간
# 시간: 3초, 메모리: 256MB



# 입력
'''
1. 테스트 케이스 T
2. 현재 A시, 앞으로 지나는 시간 B시간
- 0 ≤ A, B ≤ 23
'''



# 출력
'''
1. #{테스트케이스} {현재 A시인 상황에서 앞으로 B시간이 지나면 몇 시가 되는지를 출력}
- 자정은 '0시'
'''



# 코드
import sys

sys.stdin = open('../input_text/12368.txt')

T = int(input())
for test_case in range(1, T + 1):
    A, B = map(int, input().split())
    
    print(f'#{test_case} {(A + B) % 24}')



# 실행 결과: 성공(메모리:61,460 kb, 시간:266 ms)