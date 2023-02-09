# https://www.acmicpc.net/problem/11720
# 문제11720번.숫자의 합
# 시간제한:1초, 메모리제한:256MB



# 입력
'''
1. 숫자의 개수 N
- 1 ≤ N ≤ 100
2. 숫자 N개가 공백없이 주어짐
'''



# 출력
'''
1. 숫자 N개의 합을 출력
'''



# 코드
import sys

sys.stdin = open('input_text/11720.txt')

N = int(input())
num = input()

sum_num = 0
for n in num:
    sum_num += int(n)
print(sum_num)


# 실행결과(메모리:31256KB, 시간:44ms)