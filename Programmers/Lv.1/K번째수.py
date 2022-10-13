# https://school.programmers.co.kr/learn/courses/30/lessons/42748
# 코딩테스트연습 < 정렬 < 문제.K번째 수



# 입력
'''
1. 배열 array
- 1 <= array 길이 <= 100
- 1 <= 원소 <= 100
2. [i, j, k]를 원소로 가진 2차원 배열 commands
- 1 <= commands의 길이 <= 50
- 각 원소의 길이 = 3
'''



# 출력
'''
1. commands의 모든 원소에 대해 앞서 설명한 연산을 적용했을 때 나온 결과를 배열에 담아 return
- 배열 array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때, k번째에 있는 수
'''



# 코드 1
import sys

sys.stdin = open('input_text/K번째수.txt')

def solution(array, commands):
    answer = []
    for command in commands:
        subarray = array[command[0] - 1 : command[1]]
        subarray.sort()
        answer.append(subarray[command[2] - 1])
    
    return answer
        

# 실행 결과: 성공



# 코드 2
import sys

sys.stdin = open('input_text/K번째수.txt')

def solution(array, commands):
    return list(map(lambda command: sorted(array[command[0] - 1 : command[1]])[command[2] - 1], commands))


# 실행 결과: 성공