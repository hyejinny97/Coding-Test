# https://school.programmers.co.kr/learn/courses/30/lessons/12921
# 코딩테스트연습 < 연습문제 < 문제.소수 찾기



# 입력
'''
1. 숫자 n 
- 2 <= n <= 1,000,000
'''



# 출력
'''
1. 1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환
'''


 
# 코드 1
import sys

sys.stdin = open('input_text/소수찾기.txt')

def is_prime(num):
    for n in range(2, int(num ** 0.5) + 1):
        if num % n == 0:
            return False
    return True

def solution(n):
    cnt = 0
    for num in range(2, n + 1):
        if is_prime(num):
            cnt += 1
    return cnt


# 실행 결과: 성공




# 코드 2
# 참고(에라토스테네스의 체): https://ko.wikipedia.org/wiki/%EC%97%90%EB%9D%BC%ED%86%A0%EC%8A%A4%ED%85%8C%EB%84%A4%EC%8A%A4%EC%9D%98_%EC%B2%B4
import sys

sys.stdin = open('input_text/소수찾기.txt')

def solution(n):
    nums = set(range(2, n + 1))

    for num in range(2, int(n ** 0.5) + 1):
        if num in nums:
            nums -= set(range(2 * num, n + 1, num))

    return len(nums)


# 실행 결과: 성공