# https://www.acmicpc.net/problem/10995
# 문제10995.별 찍기-20
# 시간: 1초, 메모리: 256MB



# 입력
'''
1. 정수 N
- 1 <= N <= 100
'''



# 출력
'''
1. 예제를 보고 규칙을 유추한 뒤에 첫째줄부터 차례대로 별을 출력
- 지그재그로 별을 출력함
    - 홀수번째는 왼쪽으로 붙어서 출력
    - 짝수번째는 젤 처음에 한칸의 공백을 출력
- N의 갯수만큼 별을 출력
'''



# 코드
import sys

sys.stdin = open('input_text/10995.txt')

N = int(input())

for n in range(1, N + 1):
    # 홀수번째인 경우
    if n % 2 == 1:
        print('* ' * N)
    # 짝수번째인 경우
    else:
        print(' *' * N)



# 실행 결과: 성공(메모리:30840kb, 시간:68ms)