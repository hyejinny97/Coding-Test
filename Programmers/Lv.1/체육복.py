# https://school.programmers.co.kr/learn/courses/30/lessons/42862
# 코딩테스트연습 < 탐욕법(Greedy) < 문제.체육복



# 입력
'''
1. 전체 학생의 수 n
- 2 <= n <= 30
2. 체육복을 도난당한 학생들의 번호가 담긴 배열 lost
3. 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve
'''



# 출력
'''
1. 체육수업을 들을 수 있는 학생의 최댓값을 return 
- 바로 앞번호의 학생이나 바로 뒷번호의 학생에게만 체육복을 빌려줄 수 있음
- 여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있음. 이때 이 학생은 체육복을 하나만 도난당했다고 가정하며, 남은 체육복이 하나이기에 다른 학생에게는 체육복을 빌려줄 수 없음
'''



# 코드 
import sys

sys.stdin = open('input_text/체육복.txt')

def solution(n, lost, reserve):
    lost, reserve = set(lost), set(reserve)
    acquired = n - len(lost) + len(lost & reserve)   # 체육 수업을 들을 자격이 있는 학생 수

    # 여벌 체육복을 가져온 학생이 도난당한 경우
    lost, reserve = lost - reserve, reserve - lost

    for s in lost:
        # 자신의 앞 번호 학생에게 여벌의 옷을 빌려입을 수 있는지
        if s - 1 in reserve:
            acquired += 1
            reserve.remove(s - 1)
        # 자신의 뒷 번호 학생에게 여벌의 옷을 빌려입을 수 있는지
        elif s + 1 in reserve:
            acquired += 1
            reserve.remove(s + 1)

    return acquired
        

# 실행 결과: 성공