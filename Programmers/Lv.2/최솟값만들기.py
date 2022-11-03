# https://school.programmers.co.kr/learn/courses/30/lessons/12941
# 코딩테스트연습 < 연습문제 < 문제.최솟값 만들기



# 입력
'''
1. 길이가 같은 배열 A, B
- 각 배열은 자연수로 이루어져 있음
'''



# 출력
'''
1. 배열 A, B가 주어질 때 최종적으로 누적된 최솟값을 return
- 배열 A, B에서 각각 한 개의 숫자를 뽑아 두 수를 곱함
- 위 과정을 배열의 길이만큼 반복하며, 두 수를 곱한 값을 누적하여 더함
- 단, 각 배열에서 k번째 숫자를 뽑았다면 다음에 k번째 숫자는 다시 뽑을 수 없음
'''


# 코드 
import sys



def solution(A,B):
    A.sort()
    B.sort(reverse=True)
    
    return sum(x[0] * x[1] for x in zip(A, B))

  
# 실행 결과: 성공