# https://school.programmers.co.kr/learn/courses/30/lessons/1845
# 코딩테스트연습<해시<문제.폰켓몬



# 입력
'''
1. N마리 폰켓몬의 종류 번호가 담긴 배열 nums
- 폰켓몬은 종류에 따라 번호를 붙여 구분
- 1 <= 길이 <=10,000(항상 짝수)
- 1 <= 번호 <= 200,000
'''



# 출력
'''
1. N/2마리의 폰켓몬을 선택하는 방법 중, 가장 많은 종류의 폰켓몬을 선택하는 방법을 찾아, 그때의 폰켓몬 종류 번호의 개수를 return
- 가장 많은 종류의 폰켓몬을 선택하는 방법이 여러 가지인 경우에도, 선택할 수 있는 폰켓몬 종류 개수의 최댓값 하나만 return
'''



# 코드 1
import sys

sys.stdin = open('input_text/폰켓몬.txt')

def solution(nums):
    if len(set(nums)) >= len(nums) // 2:
        return len(nums) // 2
    else:
        return len(set(nums))
        

# 실행 결과: 성공


# 코드 2
import sys

sys.stdin = open('input_text/폰켓몬.txt')

def solution(nums):
    return min(len(nums) // 2, len(set(nums)))
        

# 실행 결과: 성공