# https://school.programmers.co.kr/learn/courses/30/lessons/67256
# 코딩테스트연습 < 2020 카카오 인턴십 < 문제.키패드 누르기



# 입력
'''
1. 순서대로 누를 번호가 담긴 배열 numbers
- 1 <= 배열 크기 <= 1,000
- 0 <= 원소 <= 9
2. 왼손잡이인지 오른손잡이인 지를 나타내는 문자열 hand
- "left" 또는 "right"
'''



# 출력
'''
1. 각 번호를 누른 엄지손가락이 왼손인 지 오른손인 지를 나타내는 연속된 문자열 형태로 return
- 왼손 엄지손가락을 사용한 경우는 L, 오른손 엄지손가락을 사용한 경우는 R

<키패드 누르는 규칙>
- 맨 처음 왼손 엄지손가락은 * 키패드에 오른손 엄지손가락은 # 키패드 위치에서 시작
- 엄지손가락은 상하좌우 4가지 방향으로만 이동할 수 있으며 키패드 이동 한 칸은 거리로 1에 해당
- 왼쪽 열의 3개의 숫자 1, 4, 7을 입력할 때는 왼손 엄지손가락을 사용
- 오른쪽 열의 3개의 숫자 3, 6, 9를 입력할 때는 오른손 엄지손가락을 사용
- 가운데 열의 4개의 숫자 2, 5, 8, 0을 입력할 때는 두 엄지손가락의 현재 키패드의 위치에서 더 가까운 엄지손가락을 사용
- 만약 두 엄지손가락의 거리가 같다면, 오른손잡이는 오른손 엄지손가락, 왼손잡이는 왼손 엄지손가락을 사용
'''



# 코드 
import sys

sys.stdin = open('input_text/키패드누르기.txt')

def distance(from_, to_):
    # 키패드 좌표료 변경
    dis = {1: [0, 0], 2: [0, 1], 3: [0, 2],
           4: [1, 0], 5: [1, 1], 6: [1, 2],
           7: [2, 0], 8: [2, 1], 9: [2, 2],
           '*':[3, 0], 0: [3, 1], '#': [3, 2]}

    r = abs(dis[from_][0] - dis[to_][0])   # 세로 이동 칸 수
    c = abs(dis[from_][1] - dis[to_][1])   # 가로 이동 칸 수

    return r + c

def solution(numbers, hand):
    answer = ''   # 각 번호를 누른 손
    left = '*'    # 현재 왼손 위치
    right = '#'   # 현재 오른손 위치
    for num in numbers:
        if num in {1, 4, 7}:
            answer += 'L'
            left = num
        elif num in {3, 6, 9}:
            answer += 'R'
            right = num
        else:
            d_left, d_right = distance(left, num), distance(right, num)
            if d_left == d_right:
                if hand == 'left':
                    answer += 'L'
                    left = num
                else:
                    answer += 'R'
                    right = num
            elif d_left > d_right:
                answer += 'R'
                right = num
            else:
                answer += 'L'
                left = num
    return answer    


# 실행 결과: 성공