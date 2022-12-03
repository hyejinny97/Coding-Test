# https://school.programmers.co.kr/learn/courses/30/lessons/12945 - 아직 해결 못 함!!!!
# 코딩테스트연습 < 연습문제 < 문제.피보나치 수

# 입력
'''
1. 자연수 n
- 2 <= n <= 100,000
'''



# 출력
'''
1. n번째 피보나치 수를 1234567으로 나눈 나머지를 리턴
'''


# 코드 1
import sys

sys.stdin = open('input_text/피보나치수.txt')

def solution(n):
    def fibonacci(n):
        if n == 1:
            return 1
        if n == 0:
            return 0
        
        return fibonacci(n - 1) + fibonacci(n - 2)

    return fibonacci(n)


# 실행 결과: 실패(런타임에러)



# 코드 2
import sys

sys.stdin = open('input_text/피보나치수.txt')

def solution(n):
    record = {}   # 키:n, 값:fibonacci(n)
    def fibonacci(n):
        if n == 1:
            return 1
        if n == 0:
            return 0
        
        record[n] = fibonacci(n - 1) + fibonacci(n - 2)

        return record[n]

    return fibonacci(n) % 1234567


# 실행 결과: 실패(런타임에러)


# 0  1  2  3  4  5  6   7
# 0  1  1  2  3  5  8   13   
#          n2 n1
      
 
# 코드 3
import sys

sys.stdin = open('input_text/피보나치수.txt')

def solution(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    n1 = 0
    n2 = 1
    for cur in range(2, n + 1):
        if cur % 2 == 0:
            n1 += n2
        else:
            n2 += n1
    
    return max(n1, n2) % 1234567


# 실행 결과: 성공



# 코드 3
import sys

sys.stdin = open('input_text/피보나치수.txt')

def fibonacci(num):
    answer = [0,1]

    for i in range(2,num+1):
        answer.append(answer[i-1]+answer[i-2])

    return answer[-1]


# 실행 결과: 성공
