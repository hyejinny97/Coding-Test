# https://www.acmicpc.net/problem/2635
# 문제2635번.수 이어가기
# 시간: 1초, 메모리: 128MB



# 입력
'''
1. 정수 N
- 0 < N <= 30,000
'''



# 출력
'''
1. 최대 갯수 출력
- 최대 개수의 수들이 여러 개일때, 그중 하나의 수들만 출력
2. 최대 갯수의 수들을 차례대로 출력
<규칙>
1) 첫번째 양의 정수가 입력으로 주어짐
2) 두번째 양의 정수 하나 선택
3) 세번째 이후의 수들은 현재 i위치라고 하면, (i-2)위치의 수에서 (i-1)위치의 수를 뺀 값
- 음의 정수가 만들어지면, 이 음의 정수를 버리고 더이상 수를 만들지 않음
'''



# 코드 
import sys

sys.stdin = open('input_text/2635.txt')

fst = int(input())

# 수들의 최대 갯수 구하기
max_nums = []
for sec in range(fst, 0, -1):
    # 현재 sec에서부터 시작된 세번째 이후의 숫자 넣기
    nums = [fst, sec]
    while True:
        next = nums[-2] - nums[-1]
        if next < 0:
            break
        nums.append(next)
    
    # 최대 갯수 갱신
    if len(nums) > len(max_nums):
        max_nums = nums

print(len(max_nums))
print(*max_nums) 
    


# 실행 결과: 성공(메모리:30840kb, 시간:92ms)