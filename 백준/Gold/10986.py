# https://www.acmicpc.net/problem/10986
# 문제10986번.나머지 합
# 시간: 1초, 메모리: 256MB



# 입력
'''
1. 수 N개, 자연수 M
- 1 ≤ N ≤ 10^6
- 2 ≤ M ≤ 10^3
2. N개의 수
- 0 ≤ Ai ≤ 10^9
'''



# 출력
'''
1. 연속된 부분 구간의 합이 M으로 나누어 떨어지는 구간의 개수를 출력
'''



# 코드

# 접근방법
'''
참고) https://zoosso.tistory.com/550
- 누적합을 M으로 나눈 나머지 값을 나열
- (나머지 = 0)인 곳은 처음부터 해당 위치까지의 합이 M으로 나누어떨어지는 곳
- (나머지 = x)로 같은 두 지점 사이의 합도 M으로 나누어떨어짐(mC2)
'''
import sys

sys.stdin = open('input_text/10986.txt')

N, M = map(int, input().split())
nums = list(map(int, input().split()))

# 누적합을 M으로 나눈 나머지들의 각 개수 구하기
remains = [0] * M   # idx: 나머지 0 ~ (M - 1) , value: 각 나머지 갯수
acc = 0
for i in range(N):
    acc += nums[i]
    remains[acc % M] += 1

# (나머지 = x)로 같은 두 지점의 조합 구하기
rst = remains[0]  # (나머지 = 0)인 곳 개수
for cnt in remains:
    rst += cnt * (cnt - 1) // 2   # nC2

print(rst)


# 실행 결과: 성공 - 50점(메모리:152756kb, 시간:580ms)

