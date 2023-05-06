# https://school.programmers.co.kr/learn/courses/30/lessons/131704
# 코딩테스트연습 < 연습문제 < 문제.택배상자



# 입력
'''
1. 택배 기사님이 원하는 상자 순서를 나타내는 정수 배열 order
- 1 ≤ order의 길이 ≤ 1,000,000
'''



# 출력
'''
1. 영재가 몇 개의 상자를 실을 수 있는지 return
- 1번 상자부터 n번 상자까지 번호가 증가하는 순서대로 컨테이너 벨트에 일렬로 놓여 영재에게 전달됨
- 택배 기사님이 미리 알려준 순서에 맞게 영재가 택배상자를 트럭에 실어야 함
- 만약 컨테이너 벨트의 맨 앞에 놓인 상자가 현재 트럭에 실어야 하는 순서가 아니라면, 보조 컨테이너 벨트에 넣음
- 이때, 가장 마지막에 보조 컨테이너 벨트에 보관한 상자부터 꺼낼 수 있음
- 보조 컨테이너 벨트를 이용해도 기사님이 원하는 순서대로 상자를 싣지 못 한다면, 더 이상 상자를 싣지 않음
'''



# 코드 
import sys

sys.stdin = open('input_text/택배상자.txt')

def solution(order):
    subContainer = []  # 보조 컨테이너 벨트
    cnt = 0   # 트럭에 실을 수 있는 상자 개수
    curBox = 1  # 일렬로 전달되어 오는 상자 (1~n번)
    for wantBox in order: 
        # 컨테이너 벨트에 가장 앞에 있는 상자 확인
        if curBox == wantBox:
                curBox += 1
                cnt += 1    
                continue 
        
        # 보조 컨테이너 벨트 가장 뒤에 있는 상자 확인
        if subContainer and subContainer[-1] == wantBox:
                subContainer.pop()
                cnt += 1    
                continue

        # 컨테이너 벨트에 내가 원하는 상자가 없으면, 더이상 실지 못함
        if curBox > wantBox:
              break

        # 원하는 상자를 찾을 때까지 컨테이너에 있는 상자를 보조 컨터테이너에 옮기기
        while curBox < wantBox:
              subContainer.append(curBox)
              curBox += 1
        curBox += 1
        cnt += 1 

    return cnt


# 실행 결과: 성공