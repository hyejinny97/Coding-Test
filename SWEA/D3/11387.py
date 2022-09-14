# 문제11387번.몬스터 사냥
# 시간: 2초, 메모리: 256MB



# 입력
'''
1. 테스트 케이스 T
2. 세 정수 데미지 D, 레벨 L, 공격 횟수 N
- 100 <= D <= 10,000
- 0 <= L <= 100
- 1 <= N <= 100
'''



# 출력
'''
1. #{테스트케이스} 용사가 몬스터에게 가한 총 데미지}
- 용사가 몬스터에게 가한 총 데미지 = D(1+nㆍL%)
- n: 지금까지 몬스터를 때린 횟수(가장 처음은 당연히 때린 횟수가 0번)
'''



# 코드 1
import sys

sys.stdin = open('../input_text/11387.txt')

T = int(input())
for test_case in range(1, T + 1):
    D, L, N = map(int, input().split())
    
    tot_damage = 0
    for n in range(N):
        tot_damage += D * (1 + n * L * 0.01)
    
    print(f'#{test_case} {int(tot_damage)}')
    


# 실행 결과: 성공(메모리:63,304 kb, 시간:1,229 ms)



# 코드 2
import sys

sys.stdin = open('../input_text/11387.txt')

T = int(input())
for test_case in range(1, T + 1):
    D, L, N = map(int, input().split())
    
    tot_damage = N * D + D * L * 0.01 * N * (N - 1) // 2
    
    print(f'#{test_case} {int(tot_damage)}')
    


# 실행 결과: 성공(메모리:63,272 kb, 시간:1,128 ms)