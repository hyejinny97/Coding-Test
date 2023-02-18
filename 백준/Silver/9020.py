# https://www.acmicpc.net/problem/9020
# 문제9020번.골드바흐의 추측
# 시간: 2초, 메모리: 256MB



# 입력
'''
1. 테스트 케이스의 개수 T
2. 각 테스트 케이스에 짝수 n
- 4 ≤ n ≤ 10,000
'''



# 출력
'''
1. n의 골드바흐 파티션을 출력
- 출력하는 소수는 작은 것부터 먼저 출력하며, 공백으로 구분
- 가능한 n의 골드바흐 파티션이 여러 가지인 경우, 두 소수의 차이가 가장 작은 것을 출력

<골드바흐 파티션>
- 골드바흐의 추측: 2보다 큰 모든 짝수는 두 소수의 합으로 나타낼 수 있다
- 골드바흐 파티션: 짝수를 두 소수의 합으로 나타내는 표현
'''



# 코드 1

# 접근방법
'''
- 2이상 N이하의 수 중 소수만 골라내, 중복 조합을 이용해서 수 두 개만 뽑기
- 뽑아낸 두 수의 합이 N과 같으면 골드바흐 파티션!
- 중복 조합 참고: https://juhee-maeng.tistory.com/91
'''
import sys
from itertools import combinations_with_replacement

sys.stdin = open('input_text/9020.txt')

# 에라토스테네스의 체
sieve = [True] * 10001
for num in range(2, 10001):
    if sieve[num]:
        for i in range(2 * num, 10001, num):
            sieve[i] = False

# N의 골드바흐 파티션
T = int(input())
for _ in range(T):
    N = int(input())
    primes = list(filter(lambda num: sieve[num], range(2, N)))
    cases = combinations_with_replacement(primes, 2)
    possible = [case for case in cases if sum(case) == N]

    # 골드바흐 파티션이 여러 가지인 경우, 두 소수의 차이가 가장 작은 것을 출력
    rst = min(possible, key=lambda case: case[1] - case[0])
    print(*rst)


# 실행 결과: 실패(시간 초과)



# 코드 2

# 접근방법
'''
- N의 중간값 아래이거나 위의 범위에서 파티션에 만족하는 두 소수가 모두 나올 순 없음
- 따라서, 한 소수는 중간값 이하의 범위에서 찾아야하고, 다른 한 소수는 중간값 이상의 범위에서 찾아야 함
- N의 중간값에서 2까지 내려가면서 num이 소수이면, (N - num)도 소수인지 확인하기
- N의 중간값에서 멀어지면 멀어질수록 두 소수의 차이는 커지니까, 위에서 두 소수의 합이 N이 되는 첫 파티션을 바로 출력하면 됨
'''
import sys

sys.stdin = open('input_text/9020.txt')

# 에라토스테네스의 체
sieve = [True] * 10001
for num in range(2, 10001):
    if sieve[num]:
        for i in range(2 * num, 10001, num):
            sieve[i] = False

# N의 골드바흐 파티션
T = int(input())
for _ in range(T):
    N = int(input())
    for num in range(N // 2, 2 - 1, -1):
        if sieve[num] and sieve[N - num]:
            print(num, N - num)
            break


# 실행 결과: 성공(메모리:31256kb, 시간:508ms)