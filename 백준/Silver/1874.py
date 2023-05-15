# https://www.acmicpc.net/problem/1874
# 문제1874번.스택 수열
# 시간: 2초, 메모리: 128MB



# 입력
'''
1. 자연수 개수 n
- 1 ≤ n ≤ 100,000
2. n개의 줄에 수열을 이루는 1이상 n이하의 정수가 하나씩 주어짐
- 같은 정수가 두 번 나오는 일은 없음
'''



# 출력
'''
1. 입력된 수열을 만들기 위해 필요한 연산을 한 줄에 한 개씩 출력
- push연산은 +로, pop 연산은 -로 표현
- 불가능한 경우 NO를 출력

- 1부터 n까지의 수를 스택에 넣었다가 뽑아 늘어놓음으로써, 하나의 수열을 만들 수 있음
- 스택에 push하는 순서는 반드시 오름차순을 지키도록 하자
'''



# 코드 1
import sys

sys.stdin = open('input_text/1874.txt')

N = int(input())
target_nums = [int(input()) for _ in range(N)]  # 입력된 수열

rst = []   # 입력된 수열을 만들기 위해 필요한 연산
stack = []   # 1부터 N까지 수를 담을 스택
possible = True   # 연산 가능 여부
current_num = 1
for target_num in target_nums:
    while (not stack or stack[-1] != target_num) and current_num <= N:
        stack.append(current_num)
        rst.append('+')
        current_num += 1
    
    if stack and stack[-1] != target_num:
        possible = False
        break

    stack.pop()
    rst.append('-')
    
# print('\n'.join(rst) if possible else 'NO')

     
# 실행 결과: 성공(메모리:37480kb, 시간:3924ms)



# 코드 2
import sys

sys.stdin = open('input_text/1874.txt')

N = int(input())
target_nums = [int(input()) for _ in range(N)]  # 입력된 수열

rst = []   # 입력된 수열을 만들기 위해 필요한 연산
stack = []   # 1부터 N까지 수를 담을 스택
possible = True   # 연산 가능 여부
current_num = 1
for target_num in target_nums:
    while current_num <= target_num:
        stack.append(current_num)
        rst.append('+')
        current_num += 1
    
    if stack[-1] != target_num:
        possible = False
        break

    stack.pop()
    rst.append('-')
    
print('\n'.join(rst) if possible else 'NO')

     
# 실행 결과: 성공(메모리:37480kb, 시간:3704ms)