# https://school.programmers.co.kr/learn/courses/30/lessons/42842
# 코딩테스트연습 < 완전탐색 < 문제.카펫

# 입력
'''
1. 갈색 격자의 수 brown, 노란색 격자의 수 yellow
- 8 <= brown 수 <= 5,000
- 1 <= yellow 수 <= 2,000,000
- 카펫의 가로 길이는 세로 길이와 같거나, 세로 길이보다 김
'''



# 출력
'''
1. 카펫의 가로, 세로 크기를 순서대로 배열에 담아 return
'''


# 코드 
import sys

sys.stdin = open('input_text/카펫.txt')

def solution(brown, yellow):
    for row in range(3, brown):  # row = 가로 격자 수
        yellow_row = row - 2
        yellow_col = (brown - 2 * row) // 2
        if yellow_row * yellow_col == yellow:
            return sorted([row, yellow_col + 2], reverse=True)


# 실행 결과: 성공