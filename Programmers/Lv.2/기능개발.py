# https://school.programmers.co.kr/learn/courses/30/lessons/42586
# 코딩테스트연습 < 스택/큐 < 문제.기능개발



# 입력
'''
1. 먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 progresses, 각 작업의 개발 속도가 적힌 정수 배열 speeds
- 0 < 작업의 개수(progresses, speeds배열의 길이) <= 100
- 0 < 작업 진도 <= 100
- 0 < 작업 속도 <= 100
- 배포는 하루에 한 번만 가능
'''



# 출력
'''
1. 각 배포마다 몇 개의 기능이 배포되는지를 return

<배포 방식>
- 각 기능은 진도가 100%일 때 배포 가능
- 각 기능의 개발속도는 모두 다름
- 어떤 기능이 먼저 완성되었더라도 앞에 있는 모든 기능이 완성되지 않으면 배포가 불가능
- 뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포됨
'''



# 코드 1
import sys

sys.stdin = open('input_text/기능개발.txt')

def solution(progresses, speeds):
    # 각 기능의 작업일 구하기
    working_day = []
    for i in range(len(progresses)):
        day = (100 - progresses[i]) // speeds[i]
        if (100 - progresses[i]) % speeds[i] != 0:
            day += 1
        working_day.append(day)

    # 각 배포마다 몇 개의 기능이 배포되는지 구하기
    deployed_service = []
    first = working_day[0]
    cnt = 1
    for i in range(1, len(working_day)):
        if working_day[i] <= first:
            cnt += 1
            continue
        deployed_service.append(cnt)
        first = working_day[i]
        cnt = 1

    deployed_service.append(cnt)
    
    return deployed_service


# 실행 결과: 성공



# 코드 2

# 접근방법
'''
파이썬에서 음수 값을 몫 나누기 연산자(//)를 이용해 나누면, 
나누기 결과보다 작은 정수 중 가장 큰 정수를 돌려준다.

print(-10 / 3)   => -3
print(-10 // 3)  => -4
'''

import sys

sys.stdin = open('input_text/기능개발.txt')

def solution(progresses, speeds):
    deployed_service = []
    for i in range(len(progresses)):
        day = - ((progresses[i] - 100) // speeds[i])
        if not deployed_service or deployed_service[-1][0] < day:
            deployed_service.append([day, 1])
        else:
            deployed_service[-1][1] += 1
    
    return [d[1] for d in deployed_service]


# 실행 결과: 성공