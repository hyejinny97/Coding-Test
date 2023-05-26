# https://www.acmicpc.net/problem/9184
# 문제9184번.신나는 함수 실행
# 시간: 1초, 메모리: 128MB



# 입력
'''
1. 세 정수 a, b, c
- -50 ≤ a, b, c ≤ 50
- 입력의 마지막은 -1 -1 -1
'''



# 출력
'''
1. w(a, b, c)를 출력
'''



# 코드 
import sys

sys.stdin = open('input_text/9184.txt')


records = {}

def w(a, b, c):
    if (a, b, c) in records:
        return records[(a, b, c)]

    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        records[(a, b, c)] = w(20, 20, 20)
    elif a < b and b < c:
        records[(a, b, c)] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
    else:
        records[(a, b, c)] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)

    return records[(a, b, c)]


while True:
    a, b, c = map(int, input().split())

    if a == -1 and b == -1 and c == -1:
        break
    
    print(f'w({a}, {b}, {c}) = {w(a, b, c)}')
    

# 실행 결과: pypy3로 성공(메모리:31544kb, 시간:972ms)