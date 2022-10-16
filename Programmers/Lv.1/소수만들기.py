# https://school.programmers.co.kr/learn/courses/30/lessons/12977
# 코딩테스트연습 < Summer/Winter Coding(~2018) < 문제.소수 만들기



# 입력
'''
1. 숫자들이 들어있는 배열 nums
- 3 <= 숫자의 개수 <= 50
- 1 <= 수 <= 1,000
'''



# 출력
'''
1. nums에 있는 숫자들 중 서로 다른 3개를 골라 더했을 때 소수가 되는 경우의 개수를 return
'''



# 코드
import sys

sys.stdin = open('input_text/소수만들기.txt')

def solution(nums):
    # 소수인지 확인해주는 함수
    def is_prime(num):
        for x in range(2, int(num ** 0.5) + 1):
            if num % x == 0:
                return False
        return True

    # 3개의 수 선택(조합)해서 더하기
    answer = 0   # 서로 다른 3개를 골라 더했을 때 소수가 되는 경우
    for fst in range(0, len(nums) - 2):
        for sec in range(fst + 1, len(nums) - 1):
            for thd in range(sec + 1, len(nums)):
                sum_3 = nums[fst] + nums[sec] + nums[thd]
                if is_prime(sum_3):
                    answer += 1

    return answer


# 실행 결과: 성공