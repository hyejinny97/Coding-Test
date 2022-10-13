# https://school.programmers.co.kr/learn/courses/30/lessons/77884
# 코딩테스트연습 < 월간 코드 챌린지 시즌2 < 문제.약수의 개수와 덧셈



# 입력
'''
1. 두 정수 left와 right
- 1 ≤ left ≤ right ≤ 1,000
'''



# 출력
'''
1. left부터 right까지의 모든 수들 중에서, 약수의 개수가 짝수인 수는 더하고, 약수의 개수가 홀수인 수는 뺀 수를 return
'''



# 코드
import sys

sys.stdin = open('input_text/약수의개수와덧셈.txt')

def solution(left, right):
    # 약수 개수가 짝수면 더하고, 홀수면 빼기
    answer = 0
    for num in range(left, right + 1):
        if int(num ** 0.5) == num ** 0.5:
            answer -= num
        else:
            answer += num

    return answer
        

# 실행 결과: 성공