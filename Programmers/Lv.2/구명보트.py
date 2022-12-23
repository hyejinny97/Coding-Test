# https://school.programmers.co.kr/learn/courses/30/lessons/42885
# 코딩테스트연습 < 탐욕법(Greedy) < 문제.구명보트



# 입력
'''
1. 사람들의 몸무게를 담은 배열 people, 구명보트의 무게 제한 limit
- 1명 <= people 수 <= 50,000명
- 40kg <= 몸무게 <= 240kg
- 40kg <= limit <= 240kg
'''



# 출력
'''
1. 모든 사람을 구출하기 위해 필요한 구명보트 개수의 최솟값을 return
- 구명보트는 한 번에 최대 2명밖에 못탐
'''


# 코드 1
import sys

sys.stdin = open('input_text/구명보트.txt')

def solution(people, limit):
    people.sort()
    cnt = 0
    idx = 0
    while idx < len(people) - 1:
        if people[idx] + people[idx + 1] <= limit:
            cnt += 1
            idx += 2
            continue
        cnt += len(people) - idx
        break

    return cnt


# 실행 결과: 실패
# print(solution([20, 30, 50, 50, 70, 80], 100))의 경우, 3을 리턴해야하지만 위 코드로는 4를 리턴함



# 코드 2
import sys

sys.stdin = open('input_text/구명보트.txt')

def solution(people, limit):
    people.sort()
    cnt = 0
    left, right = 0, len(people) - 1
    while left < right:
        if people[left] + people[right] <= limit:
            left += 1
            right -= 1
        else:
            right -= 1
        cnt += 1
    return cnt + 1 if left == right else cnt

# print(solution([20, 30, 50, 50, 70, 80, 90], 100))
# print(solution([70, 50, 80, 50], 100))
# print(solution([70, 80, 50], 100))


# 실행 결과: 성공