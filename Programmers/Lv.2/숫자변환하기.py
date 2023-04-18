# https://school.programmers.co.kr/learn/courses/30/lessons/154538
# 코딩테스트연습 < 연습문제 < 문제.숫자 변환하기



# 입력
'''
1. 자연수 x, y, n
- 1 ≤ x ≤ y ≤ 1,000,000
- 1 ≤ n < y
'''



# 출력
'''
1. x를 y로 변환하기 위해 필요한 최소 연산 횟수를 return
- x를 y로 만들 수 없다면 -1을 return

<x를 y로 변환하기 위해 사용할 수 있는 연산>
- x에 n을 더합니다
- x에 2를 곱합니다.
- x에 3을 곱합니다.
'''



# 코드 1
import sys

sys.stdin = open('input_text/숫자변환하기.txt')

def solution(x, y, n):
    def dfs(rst, cnt):
        if rst == y:
            answer.append(cnt)

        if rst > y:
            return 

        dfs(rst * 3, cnt + 1)
        dfs(rst * 2, cnt + 1)
        dfs(rst + n, cnt + 1)

    answer = []
    dfs(x, 0)

    return min(answer) if answer else -1


# 실행 결과: 실패(런타임에러)



# 코드 2

# 접근방법 - DP
'''
[inf, inf, ...] 👈 1부터 y까지의 칸 
- 각 칸은 해당 위치의 칸에 도달하기 위한 연산 횟수 최솟값!!

시작칸(x)에서부터 끝칸(y)까지 아래를 각각 실행함
1. n 더하기
2. 2 곱하기
3. 3 곱하기

참고) https://school.programmers.co.kr/questions/45629
'''
import sys

sys.stdin = open('input_text/숫자변환하기.txt')

def solution(x, y, n):
    if x == y:
        return 0
    
    MAX = 1000000
    dp = [MAX] * (y + 1)
    dp[x] = 0

    for i in range(x, y + 1):
        # 한번도 닿지 않은 칸인 경우
        if dp[i] == MAX:
            continue

        if i + n <= y:
            dp[i + n] = min(dp[i + n], dp[i] + 1)
        
        if i * 2 <= y:
            dp[i * 2] = min(dp[i * 2], dp[i] + 1)
        
        if i * 3 <= y:
            dp[i * 3] = min(dp[i * 3], dp[i] + 1)

    return -1 if dp[y] == MAX else dp[y]


# 실행 결과: 성공