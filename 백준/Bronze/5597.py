# https://www.acmicpc.net/problem/5597
# 문제5597번.과제 안 내신 분..?
# 시간: 1초, 메모리: 128MB



# 입력
'''
1. 28줄에 각 제출자(학생)의 출석번호 n이 입력됨
- 1 <= n <= 30
- 출석번호에 중복은 없음
'''



# 출력
'''
1. 제출하지 않은 학생의 출석번호 중 가장 작은 것을 출력
2. 그 다음 출석번호를 출력
'''



# 코드 
import sys

sys.stdin = open('input_text/5597.txt')

check = [0] * 31   # 숙제제출 여부 체크(idx:학생번호, value:제출여부)
for _ in range(28):
    num = int(input())  # 학생번호
    check[num] = 1   # 체크

nums = []  # 제출하지 않은 학생번호
for i in range(1, 30 + 1):
    if not check[i]:
        nums.append(i)
nums.sort()

print(nums[0], nums[1], sep='\n')


# 실행 결과: 성공(메모리:31256kb, 시간:40ms)