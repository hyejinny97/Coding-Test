# https://school.programmers.co.kr/learn/courses/30/lessons/68936
# 코딩테스트연습 < 월간 코드 챌린지 시즌1 < 문제.쿼드압축 후 개수 세기



# 입력
'''
1. 0과 1로 이루어진 2n x 2n 크기의 2차원 정수 배열 arr
- 0 <= n <= 10
'''



# 출력
'''
1. arr을 압축했을 때, 배열에 최종적으로 남는 0의 개수와 1의 개수를 배열에 담아서 return
- arr을 쿼드 트리와 같은 방식으로 압축
- 쿼드 트리: https://en.wikipedia.org/wiki/Quadtree

<arr 압축 방법>
- 압축하고자 하는 특정 영역을 S라고 정의
- 만약 S 내부에 있는 모든 수가 같은 값이라면, S를 해당 수 하나로 압축
- 그렇지 않다면, S를 정확히 4개의 균일한 정사각형 영역으로 쪼갠 후, 각 정사각형 영역에 대해 위와 같은 방식으로 압축 시도
'''



# 코드 1
import sys

sys.stdin = open('input_text/쿼드압축후개수세기.txt')

# 정사각형 영역 내부에 있는 모든 수가 같은지 확인
def isSame(arr, start_r, start_c, length):
    prev = arr[start_r][start_c]
    for r in range(start_r, start_r + length):
        for c in range(start_c, start_c + length):
            if arr[r][c] != prev:
                return False
    return True

def solution(arr):
    # arr의 초기 1과 0의 갯수 세기
    cnt_0 = 0
    cnt_1 = 0
    for r in range(len(arr)):
        for c in range(len(arr)):
            if arr[r][c] == 1:
                cnt_1 += 1
            else:
                cnt_0 += 1

    # arr 압축하기 
    length = len(arr) // 2  # S의 한 변의 길이
    while length > 0:
        for r in range(0, len(arr), length):  # 정사각형 좌측 위 꼭짓점
            for c in range(0, len(arr), length):
                if arr[r][c] == 'checked':
                    continue

                if isSame(arr, r, c, length):
                    if arr[r][c] == 0:
                        cnt_0 = cnt_0 - length * length + 1
                    if arr[r][c] == 1:
                        cnt_1 = cnt_1 - length * length + 1
                    
                    # 압축 체크
                    for row in range(r, r + length):   
                        for col in range(c, c + length):
                            arr[row][col] = 'checked'

        length //= 2
    
    return [cnt_0, cnt_1]


# 실행 결과: 실패(TC 10번만 실패 - arr가 하나의 숫자로 전부 가득 차있는 경우)



# 코드 2
import sys

sys.stdin = open('input_text/쿼드압축후개수세기.txt')

# 정사각형 영역 내부에 있는 모든 수가 같은지 확인
def isSame(arr, start_r, start_c, length):
    prev = arr[start_r][start_c]
    for r in range(start_r, start_r + length):
        for c in range(start_c, start_c + length):
            if arr[r][c] != prev:
                return False
    return True

def solution(arr):
    # arr의 초기 1과 0의 갯수 세기
    cnt_0 = 0
    cnt_1 = 0
    for r in range(len(arr)):
        for c in range(len(arr)):
            if arr[r][c] == 1:
                cnt_1 += 1
            else:
                cnt_0 += 1

    # arr 압축하기 
    length = len(arr)  # S의 한 변의 길이
    while length > 0:
        for r in range(0, len(arr), length):  # 정사각형 좌측 위 꼭짓점
            for c in range(0, len(arr), length):
                if arr[r][c] == 'checked':
                    continue

                if isSame(arr, r, c, length):
                    if arr[r][c] == 0:
                        cnt_0 = cnt_0 - length * length + 1
                    if arr[r][c] == 1:
                        cnt_1 = cnt_1 - length * length + 1
                    
                    # 압축 체크
                    for row in range(r, r + length):   
                        for col in range(c, c + length):
                            arr[row][col] = 'checked'

        length //= 2
    
    return [cnt_0, cnt_1]


# 실행 결과: 성공