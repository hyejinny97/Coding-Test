# https://www.acmicpc.net/problem/9498
# 문제9498.시험성적
# 시간: 1초, 메모리: 128MB



# 입력
'''
1. 시험 점수
- 0 <= 점수 <= 100
'''



# 출력
'''
1. 시험 성적을 출력
'''



# 코드
import sys

sys.stdin = open('input_text/9498.txt')

score = int(input())

if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')
else:
    print('F')


# 실행 결과: 성공(메모리:30840kb, 시간:68ms)