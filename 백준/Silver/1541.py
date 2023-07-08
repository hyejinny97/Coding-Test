# https://www.acmicpc.net/problem/1541
# 문제1541번.잃어버린 괄호
# 시간: 2초, 메모리: 128MB



# 입력
'''
1. 식
- 0~9, +, -만으로 구성
- 가장 처음과 마지막 문자는 숫자임
- 0 < 식의 길이 <= 50
- 수는 0으로 시작할 수 있음
- 5자리보다 많이 연속되는 숫자는 없음
'''



# 출력
'''
1. 괄호를 적절히 쳐서 이 식의 값을 최소로 만들어 출력
'''



# 코드

# 접근방법
'''
+ 부분을 괄호 쳐서 먼저 더해 큰 값을 만들어준 후 -로 빼줌 
'''
import sys

sys.stdin = open('input_text/1541.txt')

problem = input()

subnums = problem.split('-')
sum_subnums = []
for subnum in subnums:
    sum_subnums.append(sum(map(int, subnum.split('+'))))

rst = sum_subnums[0]
for i in range(1, len(sum_subnums)):
    rst -= sum_subnums[i]

print(rst)


# 실행 결과: 성공(메모리:31256kb, 시간:40ms)