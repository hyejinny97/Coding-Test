# 문제1288.새로운 불면증 치료법
# 시간: 4초, 메모리: 256MB

# 입력
'''
1. 테스트 케이스 개수 T
2. 자연수 N
- 1 <= N <= 10^6
'''

# 출력
'''
1. #테스트케이스
2. 최소 몇 번 양을 세었을 때, 이전에 봤던 숫자들의 자릿수에서 0에서 9까지의 모든 숫자를 보게 되는지 출력
- 민석이는 1xN, 2xN, 3xN, ..., M x N번 양을 세고 있음
'''

# 코드 1
import sys

sys.stdin = open('SWEA/input_text/1288.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    
    check = [False] * 10   # 인덱스: 0부터 9까지의 숫자, 값: 발견 여부
    M = 1   # N에 곱해나갈 값
    cnt = 0   # 발견한 숫자 갯수
    while cnt < 10:
        num = M * N
        # 각 자리수를 돌면서 아직 발견 못한 수인 경우 마킹
        for char in str(num):
            if not check[int(char)]:
                check[int(char)] = True
                cnt += 1
        M += 1

    print(f'#{test_case} {(M - 1) * N}')

# 실행 결과: 성공(메모리:61,676 kb, 시간:165 ms)


# 코드 2
sys.stdin = open('SWEA/input_text/1288.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    
    check = set()
    M = 1   # N에 곱해나갈 값
    while len(check) < 10:
        num = M * N
        while num:
            check.add(num % 10)
            num //= 10
        M += 1

    print(f'#{test_case} {(M - 1) * N}')

# 실행 결과: 성공(메모리:57,976 kb, 시간:151 ms)