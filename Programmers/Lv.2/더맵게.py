# https://school.programmers.co.kr/learn/courses/30/lessons/42626
# 코딩테스트연습 < 힙(Heap) < 문제.더 맵게



# 입력
'''
1. 음식의 스코빌 지수를 담은 배열 scoville
- 2 <= scoville의 길이 <= 1,000,000
- 0 <= scoville의 원소 <= 1,000,000
2. 원하는 스코빌 지수 K
- 0 <= K <= 1,000,000,000
'''



# 출력
'''
1. 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 섞어야 하는 최소 횟수를 return
- 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우에는 -1을 return

<두 개의 음식을 섞는 방법>
- 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
'''


# 코드 1
import sys

sys.stdin = open('input_text/더맵게.txt')

def solution(scoville, K):
    mixing_cnt = 0   # 섞은 횟수
    while len(scoville) > 1:
        scoville.sort(reverse=True)
        first = scoville.pop()   # 가장 낮은 스코빌 지수
        sec = scoville.pop()     # 두번째로 가장 낮은 스코빌 지수
        if first >= K:
            return mixing_cnt
        mix = first + sec * 2    # 섞은 음식의 스코빌 지수
        scoville.append(mix)
        mixing_cnt += 1

    return 1 if scoville[0] >= K else -1


# 실행 결과: 실패(정확성 테스트 성공, 효율성 테스트는 시간초과로 실패)



# 코드 2

# 접근방법
'''
- 섞어야하는 두 개의 음식은 항상 스코빌 지수의 최솟값과 이 값 다음의 작은 값임
- 따라서, 최솟값을 K와 비교해 넘지 않으면 두 개의 최솟값을 가지고 계산하는 과정을 반복해야함
- 최소힙을 이용하면 매번 N개의 수를 다시 정렬(O(NlogN))할 필요없이 빠르게 최솟값을 얻을 수 있음(O(log(N)))

<최소힙>
- N개의 수 정렬: O(NlogN)
- 삽입, 삭제: O(logN)
- heapq 모듈 참고: https://littlefoxdiary.tistory.com/3
'''
import sys
import heapq

sys.stdin = open('input_text/더맵게.txt')

def solution(scoville, K):
    heapq.heapify(scoville)   # 최소 힙 정렬

    mixing_cnt = 0   # 섞은 횟수
    while len(scoville) > 1:
        first = heapq.heappop(scoville)   # 가장 낮은 스코빌 지수
        sec = heapq.heappop(scoville)     # 두번째로 가장 낮은 스코빌 지수
        if first >= K:
            return mixing_cnt
        mix = first + sec * 2    # 섞은 음식의 스코빌 지수
        heapq.heappush(scoville, mix)
        mixing_cnt += 1

    return 1 if scoville[0] >= K else -1


# 실행 결과: 성공