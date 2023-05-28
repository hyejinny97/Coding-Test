# https://www.acmicpc.net/problem/2579
# 문제2579번.계단 오르기
# 시간: 1초, 메모리: 128MB



# 입력
'''
1. 계단의 개수
- 0 < 개수 <= 300
2. 둘째 줄부터 한 줄에 하나씩 제일 아래에 놓인 계단부터 순서대로 각 계단에 쓰여 있는 점수가 주어짐
- 0 < 점수 <= 10,000
'''



# 출력
'''
1. 계단 오르기 게임에서 얻을 수 있는 총 점수의 최댓값을 출력

<계단 오르기 게임 규칙>
- 계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있다.
- 연속된 세 개의 계단을 모두 밟아서는 안 된다. (단, 시작점은 계단에 포함x)
- 마지막 도착 계단은 반드시 밟아야 한다.
'''



# 코드 1

# 접근방법
'''
- 현재 위치의 최댓값 = 이전까지의 수의 합 최댓값 + 현재의 수
- 즉, 각 칸은 현재 위치의 최댓값이 됨
'''
import sys

sys.stdin = open('input_text/2579.txt')

N = int(input())
scores = [int(input())for _ in range(N)]  
rst = [[10, False]] + [[0, False] for _ in range(N - 1)]  # [[현 위치까지 오는데 점수 최댓값, 직전 칸에서 한 칸 이동 여부], ...]

for i in range(N):
    # 한 칸 이동
    if not rst[i][1] and (i + 1) < N:   # 직전 칸에서 한 칸 이동한게 아닐 때
        if (rst[i][0] + scores[i + 1]) > rst[i + 1][0]:
            rst[i + 1] = [rst[i][0] + scores[i + 1], True]
    
    # 두 칸 이동
    if (i + 2) < N:
        if (rst[i][0] + scores[i + 2]) > rst[i + 2][0]:
            rst[i + 2] = [rst[i][0] + scores[i + 2], False]

print(rst[-1][0])


# 실행 결과: 실패(시작점을 따로 고려안해줬기 떄문)



# 코드 2

# 접근방법
'''
- 현재 위치의 최댓값 = 이전까지의 수의 합 최댓값 + 현재의 수
- 즉, 각 칸은 현재 위치의 최댓값이 됨
'''
import sys

sys.stdin = open('input_text/2579.txt')

def find_max_score(start_idx):
    rst = [[0, False] for _ in range(N)]  # [[현 위치까지 오는데 점수 최댓값, 직전 칸에서 한 칸 이동 여부], ...]
    rst[start_idx] = [scores[start_idx], False]

    for i in range(start_idx, N):
        # 한 칸 이동
        if not rst[i][1] and (i + 1) < N:   # 직전 칸에서 한 칸 이동한게 아닐 때
            if (rst[i][0] + scores[i + 1]) > rst[i + 1][0]:
                rst[i + 1] = [rst[i][0] + scores[i + 1], True]
        
        # 두 칸 이동
        if (i + 2) < N:
            if (rst[i][0] + scores[i + 2]) > rst[i + 2][0]:
                rst[i + 2] = [rst[i][0] + scores[i + 2], False]

    return rst[-1][0]


N = int(input())
scores = [int(input())for _ in range(N)]  

if N == 1:
    print(scores[0])
elif N >= 2:
    results = []
    for start_idx in range(2):
        results.append(find_max_score(start_idx))
    print(max(results))


# 실행 결과: 실패



# 코드 3

# 접근방법
'''
- 현재 위치의 최댓값 = 이전까지의 수의 합 최댓값 + 현재의 수
- 즉, 각 칸은 현재 위치의 최댓값이 됨

<점화식>
1. dp[i] = dp[i - 3] + scores[i - 1] + scores[i]
2. dp[i] = dp[i - 2] + scores[i]

참고) https://velog.io/@hyuntall/%EB%B0%B1%EC%A4%80-2579%EB%B2%88-%EA%B3%84%EB%8B%A8-%EC%98%A4%EB%A5%B4%EA%B8%B0-%EB%AC%B8%EC%A0%9C-%ED%92%80%EC%9D%B4-%ED%8C%8C%EC%9D%B4%EC%8D%AC
'''
import sys

sys.stdin = open('input_text/2579.txt')

N = int(input())
scores = [0] + [int(input()) for _ in range(N)]  
dp = [0] * (N + 1)  # 각 칸은 현 위치까지 오는데 점수 최댓값

if N == 1:
    print(scores[1])
elif N == 2:
    print(sum(scores[:3]))
else:
    dp[1] = scores[1]
    dp[2] = sum(scores[:3])
    for i in range(3, N + 1):
        dp[i] = max(dp[i - 3] + scores[i - 1] + scores[i], dp[i - 2] + scores[i])

    print(dp[-1])


# 실행 결과: 성공(메모리:31256kb, 시간:48ms)