# https://www.acmicpc.net/problem/15953
# 문제15953번.상금 헌터
# 시간: 1초, 메모리: 512MB



# 입력
'''
1. 가정한 횟수 T
- 1 <= T <= 1,000
2. T개의 줄에 가정에 대한 정보 => 두개의 정수 a, b
- 0 <= a <= 100 (제 1회 페스티벌 등수)
- 0 <= b <= 64 (제 2회 페스티벌 등수)
'''



# 출력
'''
1. T개줄에 각각 받을 상금을 하나씩 출력
'''



# 코드 1
import sys
from itertools import accumulate

sys.stdin = open('input_text/15953.txt')

# 제 1회 페스티벌에서의 순위 당 상금
reward1 = [0, 500, 300, 200, 50, 30, 10]   # 인덱스: 슨위, 값: 상금
reward1_rank = list(accumulate([0, 1, 2, 3, 4, 5, 6]))   # 값: 인원 누적값

# 제 2회 페스티벌에서의 순위 당 상금
reward2 = [0, 512, 256, 128, 64, 32]   # 인덱스: 슨위, 값: 상금
reward2_rank = list(accumulate([0, 1, 2, 4, 8, 16]))   # 값: 인원 누적값

T = int(input())
for _ in range(T):
    a, b = map(int, input().split())

    tot_reward = 0
    # 제 1회 페스티벟에서 받을 상금
    if a != 0 and a <= reward1_rank[-1]:
        for i in range(1, len(reward1_rank)):
            if reward1_rank[i - 1] < a <= reward1_rank[i]:
                tot_reward += reward1[i]
                break
    
    # 제 2회 페스티벟에서 받을 상금
    if b != 0 and b <= reward2_rank[-1]:
        for i in range(1, len(reward2_rank)):
            if reward2_rank[i - 1] < b <= reward2_rank[i]:
                tot_reward += reward2[i]
                break

    print(tot_reward * 10000)



# 실행 결과: 성공(메모리:30840kb, 시간:160ms)



# 코드 2
import sys

sys.stdin = open('input_text/15953.txt')

# 제 1회 페스티벌에서의 순위 당 상금
reward1 = [500, 300, 200, 50, 30, 10]   # 인덱스: 슨위, 값: 상금
person1 = [1, 2, 3, 4, 5, 6]
reward1_per_person = [0]   # 순위 당 상금
for i in range(len(person1)):
    reward1_per_person += [reward1[i]] * person1[i]

# 제 1회 페스티벌에서의 순위 당 상금
reward2 = [512, 256, 128, 64, 32]   # 인덱스: 슨위, 값: 상금
person2 = [1, 2, 4, 8, 16]   
reward2_per_person = [0]   # 순위 당 상금
for i in range(len(person2)):
    reward2_per_person += [reward2[i]] * person2[i]


T = int(input())
for _ in range(T):
    a, b = map(int, input().split())

    tot_reward = 0
    if a < len(reward1_per_person):
        tot_reward += reward1_per_person[a]
    if b < len(reward2_per_person):
        tot_reward += reward2_per_person[b]

    print(tot_reward * 10000)



# 실행 결과: 성공(메모리:30840kb, 시간:156ms)