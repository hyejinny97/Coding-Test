# https://school.programmers.co.kr/learn/courses/30/lessons/17682
# 코딩테스트연습 < 2018 KAKAO BLIND RECRUITMENT < 문제.1차 다트 게임



# 입력
'''
1. 0~10의 정수와 문자 S, D, T, *, #로 구성된 문자열
- "점수|보너스|[옵션]"으로 이루어진 문자열 3세트.
- 점수: 0~10
- 보너스: S, D, T 
- 옵션: *, #
'''



# 출력
'''
1. 총점수를 반환
<다트 게임의 점수 계산 로직>
1) 다트 게임은 총 3번의 기회로 구성
2) 각 기회마다 얻을 수 있는 점수는 0점에서 10점까지
3) 점수와 함께 Single(S), Double(D), Triple(T) 영역이 존재
- 각 영역 당첨 시 점수에서 1제곱, 2제곱, 3제곱으로 계산
4) 옵션으로 스타상(*) , 아차상(#)이 존재
- 스타상(*) 당첨 시 해당 점수와 바로 전에 얻은 점수를 각 2배로 만든다. 
- 아차상(#) 당첨 시 해당 점수는 마이너스된다.
5) 스타상(*)이 첫 번째 기회에서 나올 경우, 첫 번째 스타상(*)의 점수만 2배가 된다.
6) 스타상(*)이 다른 스타상(*)의 효과와 중첩될 경우, 스타상(*) 점수는 4배가 된다.
7) 스타상(*)이 아차상(#)의 효과와 중첩될 경우, 중첩된 아차상(#)의 점수는 -2배가 된다.
8) Single(S), Double(D), Triple(T)은 점수마다 하나씩 존재
9) 스타상(*), 아차상(#)은 점수마다 둘 중 하나만 존재할 수 있으며, 존재하지 않을 수도 있다.
'''



# 코드 1
import sys

sys.stdin = open('input_text/1차다트게임.txt')

def solution(dartResult):
    answer = []
    skip = False
    for i in range(len(dartResult)):
        if skip:
            skip = not skip
            continue
        
        # 숫자
        if dartResult[i].isdigit():
            # 숫자가 10인 경우
            if dartResult[i:i+2] == '10':
                answer.append(10)
                skip = True
            else:
                answer.append(int(dartResult[i]))
        
        # 보너스
        elif dartResult[i] == 'D':
            answer[-1] = answer[-1] ** 2
        elif dartResult[i] == 'T':
            answer[-1] = answer[-1] ** 3

        # 옵션
        elif dartResult[i] == '*':
            answer[-1] *= 2
            if len(answer) >= 2:
                answer[-2] *= 2
        elif dartResult[i] == '#':
            answer[-1] *= -1
        print(answer)

    return sum(answer)


# 실행 결과: 성공




# 코드 2
import sys, re

sys.stdin = open('input_text/1차다트게임.txt')

def solution(dartResult):
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}
    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)
    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

    return sum(dart)


# 실행 결과: 성공