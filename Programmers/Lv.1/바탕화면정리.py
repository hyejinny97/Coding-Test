# https://school.programmers.co.kr/learn/courses/30/lessons/161990
# 코딩테스트연습 < 연습문제 < 문제.바탕화면 정리



# 입력
'''
1. 컴퓨터 바탕화면의 상태를 나타내는 문자열 배열 wallpaper
- 1 ≤ wallpaper의 길이(행) ≤ 50
- 1 ≤ wallpaper[i]의 길이(열) ≤ 50
- wallpaper의 모든 원소의 길이는 동일
- 원소: '#' 또는 '.'
'''



# 출력
'''
1. 바탕화면의 파일들을 한 번에 삭제하기 위해 최소한의 이동거리를 갖는 드래그의 시작점과 끝점을 담은 정수 배열을 return
- 드래그의 시작점이 (lux, luy), 끝점이 (rdx, rdy)라면 정수 배열 [lux, luy, rdx, rdy]를 return
- 드래그 시작점 (lux, luy)와 끝점 (rdx, rdy)는 lux < rdx, luy < rdy를 만족해야함
'''



# 코드 
import sys

sys.stdin = open('input_text/바탕화면정리.txt')

def solution(wallpaper):
    lux, luy = 50, 50
    rdx, rdy = 0, 0
    for r in range(len(wallpaper)):
        for c in range(len(wallpaper[0])):
            if wallpaper[r][c] == '#':
                lux, luy = min(lux, r), min(luy, c)
                rdx, rdy = max(rdx, r), max(rdy, c)
    
    return [lux, luy, rdx + 1, rdy + 1]


# 실행 결과: 성공

