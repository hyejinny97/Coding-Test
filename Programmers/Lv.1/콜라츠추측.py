# https://school.programmers.co.kr/learn/courses/30/lessons/12943
# 코딩테스트연습 < 연습문제 < 문제.콜라츠 추측



# 입력
'''
1. 입력된 수 num
- 1 <= num <= 8,000,000
'''



# 출력
'''
1. 아래 작업을 몇 번이나 반복해야 하는지 반환
- 단, 주어진 수가 1인 경우에는 0을, 작업을 500번 반복할 때까지 1이 되지 않는다면 –1을 반환
<작업>
- 입력된 수가 짝수라면 2로 나눕니다. / 입력된 수가 홀수라면 3을 곱하고 1을 더합니다. 
- 결과로 나온 수에 같은 작업을 1이 될 때까지 반복합니다. 
'''



# 코드 
import sys

sys.stdin = open('input_text/콜라츠추측.txt')

def solution(num):
    cnt = 0
    while num != 1 and cnt < 500:
        if num % 2 == 0:
            num //= 2
        else:
            num = num * 3 + 1
        cnt += 1
    return -1 if cnt == 500 else cnt


# 실행 결과: 성공