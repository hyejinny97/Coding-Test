# https://school.programmers.co.kr/learn/courses/30/lessons/43165?language=python3
# 코딩테스트연습 < 깊이/너비 우선 탐색(DFS/BFS) < 문제.타겟 넘버



# 입력
'''
1. 양의 정수가 담긴 배열 numbers, 타겟 넘버 target
- 2 <= numbers 길이 <= 20
- 1 <= 숫자 <= 50
- 1 <= target <= 1,000
'''



# 출력
'''
1. 숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수를 return 
'''


# 코드 1 - 재귀함수로 풀이
import sys

sys.stdin = open('input_text/타겟넘버.txt')

def solution(numbers, target):
    def makes_number(cnt, signs):
        if cnt == len(numbers):
            num = sum(map(lambda x: x[0] * x[1], zip(numbers, signs)))
            rst.append(num)
            return 
        
        for sign in [1, -1]:
            makes_number(cnt + 1, signs + [sign])

    rst = []
    makes_number(0, [])
    return rst.count(target)


# 실행 결과: 성공



# 코드 2 - dfs로 풀이
import sys

sys.stdin = open('input_text/타겟넘버.txt')

def solution(numbers, target):
    stack = [(0, 0)]   # (다음 인덱스, 현재까지 값을 모두 더한 결과)
    answer = 0    # 타겟 넘버 수
    while stack:
        idx, num = stack.pop()

        if idx == len(numbers):
            if num == target:
                answer += 1
            continue

        stack += [(idx + 1, num + numbers[idx]), (idx + 1, num - numbers[idx])]
    
    return answer


# 실행 결과: 성공



# 코드 3 - bfs로 풀이
import sys
from collections import deque

sys.stdin = open('input_text/타겟넘버.txt')

def solution(numbers, target):
    q = deque([(0, 0)])   # (다음 인덱스, 현재까지 값을 모두 더한 결과)
    answer = 0    # 타겟 넘버 수
    while q:
        idx, num = q.popleft()

        if idx == len(numbers):
            if num == target:
                answer += 1
            continue

        q += [(idx + 1, num + numbers[idx]), (idx + 1, num - numbers[idx])]
    
    return answer


# 실행 결과: 성공



# 코드 4 - 트리
import sys

sys.stdin = open('input_text/타겟넘버.txt')

def solution(numbers, target):
    if not numbers and target == 0:
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target - numbers[0]) + solution(numbers[1:], target + numbers[0])


# 실행 결과: 성공



# 코드 5 - 중복순열

# 접근방법
'''
중복순열 참고: https://hinos.tistory.com/94
product() 참고: https://docs.python.org/ko/3/library/itertools.html#itertools.product
'''
import sys
from itertools import product

sys.stdin = open('input_text/타겟넘버.txt')

def solution(numbers, target):
    signed_numbers = [(num, -num) for num in numbers] 
    sum_numbers = list(map(sum, product(*signed_numbers)))
    return sum_numbers.count(target)


# 실행 결과: 성공