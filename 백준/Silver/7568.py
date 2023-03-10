# https://www.acmicpc.net/problem/7568
# 문제7568번.덩치
# 시간: 1초, 메모리: 128MB



# 입력
'''
1. 전체 사람의 수 N
- 2 ≤ N ≤ 50
2. N개의 줄에는 각 사람의 몸무게와 키 (x, y)
- 10 ≤ x, y ≤ 200
'''



# 출력
'''
1. 사람의 덩치 등수를 구해서 그 순서대로 첫 줄에 출력
- 덩치 등수 = 자신보다 더 "큰 덩치"의 사람의 수
- 몸무게와 키가 모두 커야만 덩치가 더 크다고 할 수 있음
'''



# 코드
import sys

sys.stdin = open('input_text/7568.txt')

N = int(input())

# N명의 몸무게, 키 입력 받기
people = []
for _ in range(N):
    weight, height = map(int, input().split())
    people.append((weight, height))

# 덩치 등수 구하기
for me in people:     # 자기 자신
    cnt = 0   # 자신보다 덩치가 큰 사람 수
    for cmp in people: # 비교 대상
        if me[0] < cmp[0] and me[1] < cmp[1]:
            cnt += 1
    print(cnt + 1, end=' ')


# 실행 결과: 성공(메모리:31256kb, 시간:40ms)