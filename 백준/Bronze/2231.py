# https://www.acmicpc.net/problem/2231
# 문제2231번.분해합
# 시간: 2초, 메모리: 192MB



# 입력
'''
1. 자연수 N
- 1 ≤ N ≤ 1,000,000
'''



# 출력
'''
1. N의 가장 작은 생성자를 출력
- 생성자가 없는 경우에는 0을 출력

<분해합과 생성자>
- 자연수 N의 분해합 = N과 N을 이루는 각 자리수의 합
- M의 분해합이 N인 경우, M을 N의 생성자
- 245 --분해합-→ 256
- 245는 256의 생성자 
'''



# 코드
import sys

sys.stdin = open('input_text/2231.txt')

N = int(input())

for num in range(1, N):
    # num을 분해합하기
    sum_num = num   
    for n in str(num):   
        sum_num += int(n)
    
    # 생성자인지 확인
    if sum_num == N:
        print(num)
        break
else: 
    print(0)


# 실행 결과: 성공(메모리:31256kb, 시간:1736ms)