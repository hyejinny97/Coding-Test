# https://www.acmicpc.net/problem/2864
# 문제2864번.5와 6의 차이
# 시간제한:1초, 메모리제한:128MB



# 입력
'''
1. 두 정수 A, B
- 1 <= A, B <= 1,000,000
'''



# 출력
'''
1. 구할 수 있는 두 수의 합 중 최솟값과 최댓값 출력
- 5 -> 6, 6 -> 5
'''



# 코드
import sys

sys.stdin = open('input_text/2864.txt')

A, B = input().split()
As = [int(A.replace('5', '6')), int(A.replace('6', '5'))]
Bs = [int(B.replace('5', '6')), int(B.replace('6', '5'))]

print(min(As) + min(Bs), max(As) + max(Bs))



# 실행 결과: 성공(메모리:30840kb, 시간:80ms)