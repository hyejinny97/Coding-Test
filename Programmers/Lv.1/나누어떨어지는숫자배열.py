# https://school.programmers.co.kr/learn/courses/30/lessons/12910
# 코딩테스트연습 < 연습문제 < 문제.나누어 떨어지는 숫자 배열



# 입력
'''
1. 자연수를 담은 배열 array
- 1 <= 길이
2. 자연수 divisor
'''



# 출력
'''
1. array의 각 element 중 divisor로 나누어 떨어지는 값을 오름차순으로 정렬한 배열을 반환
- divisor로 나누어 떨어지는 element가 하나도 없다면 배열에 -1을 담아 반환
'''



# 코드 
import sys

sys.stdin = open('input_text/나누어떨어지는숫자배열.txt')

def solution(arr, divisor):
    answer = []
    for ele in arr:
        if ele % divisor == 0:
            answer.append(ele)

    return sorted(answer) if answer else [-1]


# 실행 결과: 성공