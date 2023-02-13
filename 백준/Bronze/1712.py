# https://www.acmicpc.net/problem/1712
# 문제1712번.손익분기점
# 시간제한:0.35초, 메모리제한:128MB



# 입력
'''
1. 고정 비용 A, 가변 비용 B, 노트북 가격 C가 공백으로 구분되어 주어짐
'''



# 출력
'''
1. 손익분기점(최초로 이익이 발생하는 판매량) 출력
- 손익분기점이 존재하지 않으면 -1을 출력
'''



# 코드 1

# 접근방법
'''
노트북 판매량을 a라고 할 때,
총 비용 = A + B x a
총 수입 = C x a
따라서, 손익분기점은 A + B x a < C x a에서 a의 최솟값
=> A/(C - B) < a 
----------------------------------------------------------
만약 가변비용(B)이 노트북 한 대 가격(C)보다 크면 손익분기점이 존재하지 않음
'''

import sys

sys.stdin = open('input_text/1712.txt')

A, B, C = map(int, input().split())

if B > C:
    print(-1)
else:
    print(A // (C - B) + 1)


# 실행결과(실패: ZeroDivisionError)



# 코드 2
import sys

sys.stdin = open('input_text/1712.txt')

A, B, C = map(int, input().split())

if B >= C:
    print(-1)
else:
    print(A // (C - B) + 1)


# 실행결과(메모리:31256KB, 시간:40ms)