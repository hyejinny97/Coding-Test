# https://school.programmers.co.kr/learn/courses/30/lessons/68935
# 코딩테스트연습 < 월간 코드 챌린지 시즌1 < 문제.3진법 뒤집기



# 입력
'''
1. 자연수 n
- 1 <= n <= 100,000,000
'''



# 출력
'''
1. n을 3진법 상에서 앞뒤로 뒤집은 후, 이를 다시 10진법으로 표현한 수를 return 
'''



# 코드 1
# 참고(진법 변환): https://velog.io/@code_angler/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%A7%84%EC%88%98%EB%B3%80%ED%99%982%EC%A7%84%EB%B2%95-3%EC%A7%84%EB%B2%95-5%EC%A7%84%EB%B2%95-10%EC%A7%84%EB%B2%95n%EC%A7%84%EB%B2%95
import sys

sys.stdin = open('input_text/3진법뒤집기.txt')

def solution(n):
    # 10진법 -> 3진법 -> 앞뒤 반전
    rst = []
    while n > 2:
        rst.append(str(n % 3))
        n //= 3
    rst.append(str(n))

    # 다시 10진법으로 변환
    return int(''.join(rst), 3)


# 실행 결과: 성공



# 코드 2
import sys

sys.stdin = open('input_text/3진법뒤집기.txt')

def solution(n):
    # 10진법 -> 3진법 -> 앞뒤 반전
    rst = ''
    while n:
        rst += str(n % 3)
        n //= 3

    # 다시 10진법으로 변환
    return int(rst, 3)


# 실행 결과: 성공