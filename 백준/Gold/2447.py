# https://www.acmicpc.net/problem/2447
# 문제2447번.별찍기 - 10
# 시간: 1초, 메모리: 256MB



# 입력
'''
1. N
- N = 3^k (1 <= k <= 8)
'''



# 출력
'''
1. N번째 줄까지 별 출력

<별 찍는 방법>
- N x N 크기의 별
- N = 3의 패턴
    ***
    * *
    ***
- N >= 3 인 경우, 크기 N의 패턴은 공백으로 채워진 가운데의 (N / 3) x (N / 3) 정사각형을 크기 N / 3의 패턴으로 둘러싼 형태
'''



# 코드

# 접근방법
'''
1. N = 3 일 때

  012
0 ***
1 * *
2 ***

패턴 = *

2. N = 3^2 = 3 x 3 일 때
    
  012345678
0 *********
1 * ** ** *
2 *********
3 ***   ***
4 * *   * *
5 ***   ***
6 *********
7 * ** ** *
8 *********

패턴 = ***
       * *
       ***


<규칙>
1. 3^k의 별 = 3^(k-1)의 별을 세번, 두번, 세번 찍어냄
2. N = 3 (즉, k = 1)일 때, 패턴 = *
'''
import sys

sys.stdin = open('input_text/2447.txt')

def make_star(k, pattern = ['*'], rst = []):
    if k == 0:
        print('\n'.join(pattern))
        return
    
    for row in range(1, 3 + 1):  # 행 3번
        for line in pattern:     # 패턴을 열 3번
            if row == 2:
                rst.append(line * 1 + ' ' * len(line) + line * 1)
                continue
            rst.append(line * 3)  

    make_star(k - 1, rst, [])


def find_k(num):   # 3의 몇 승인지
    acc = 1
    for k in range(1, 8 + 1):
        acc *= 3
        if acc == num:
            return k
    

N = int(input())
make_star(find_k(N))


# 실행 결과: 성공(메모리:45228kb, 시간:52ms)