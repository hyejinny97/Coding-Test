# https://www.acmicpc.net/problem/4948
# 문제4948번.베르트랑 공준
# 시간: 1초, 메모리: 256MB



# 입력
'''
1. 각 줄에 자연수 n이 주어짐
- 입력의 마지막엔 0이 주어짐
- 1 ≤ n ≤ 123,456
'''



# 출력
'''
1. 각 테스트 케이스에 대해서, n보다 크고, 2n보다 작거나 같은 소수의 개수를 출력
'''



# 코드 1
import sys

sys.stdin = open('input_text/4948.txt')

def is_prime(num):
    if num == 1:
        return False

    for n in range(2, int(num ** 0.5) + 1):
        if num % n == 0:
            return False

    return True


while True:
    N = int(input())
    if N == 0:
        break
    
    cnt = 0   # 소수 개수
    for num in range(N + 1, 2 * N + 1):
        if is_prime(num):
            cnt += 1
    print(cnt)


# 실행 결과: 실패(시간초과)



# 코드 2

# 접근방법
'''
에라토스테네스의 체: https://ko.wikipedia.org/wiki/%EC%97%90%EB%9D%BC%ED%86%A0%EC%8A%A4%ED%85%8C%EB%84%A4%EC%8A%A4%EC%9D%98_%EC%B2%B4
'''
import sys

sys.stdin = open('input_text/4948.txt')

# 소수인지 확인해주는 함수
def is_prime(num):
    if num == 1:
        return False

    for n in range(2, int(num ** 0.5) + 1):
        if num % n == 0:
            return False

    return True


# 에라토스테네스의 체
sieve = [True] * 250001   # idx: 0부터 250,000까지의 수, value: 소수면 True
for num in range(1, 250001):
    # num이 소수이면, num의 배수 모두 제거
    if sieve[num] and is_prime(num):
        for i in range(2 * num, 250001, num):
            sieve[i] = False


# n 초과 2n 이하의 수 중 소수 개수 출력
while True:
    N = int(input())
    if N == 0:
        break
    
    print(sum(sieve[N + 1:2 * N + 1]))


# 실행 결과: 성공(메모리:34788kb, 시간:492ms)



# 코드 3

# 접근방법
'''
앞 숫자 배수에 해당이 안되었다면, 굳이 소수인지 다시 한번 체크할 필요없이 그 수는 소수임
'''
import sys

sys.stdin = open('input_text/4948.txt')

# 에라토스테네스의 체
sieve = [True] * 250001   # idx: 0부터 250,000까지의 수, value: 소수면 True
for num in range(2, 250001):
    # num이 소수이면, num의 배수 모두 제거
    if sieve[num]:
        for i in range(2 * num, 250001, num):
            sieve[i] = False

# n 초과 2n 이하의 수 중 소수 개수 출력
while True:
    N = int(input())
    if N == 0:
        break
    
    print(sum(sieve[N + 1:2 * N + 1]))


# 실행 결과: 성공(메모리:34788kb, 시간:212ms)