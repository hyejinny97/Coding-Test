# https://www.acmicpc.net/problem/1065
# 문제1065번.한수
# 시간제한:2초, 메모리제한:128MB



# 입력
'''
1. 자연수 N
- 0 < N <= 1,000
'''



# 출력
'''
1. 1 <= 한수 <= N인 한수의 갯수를 출력
- 한수: 양의 정수 X의 각 자리가 등차수열인 수
'''



# 코드
import sys

sys.stdin = open('input_text/1065.txt')

# 양의 정수 각 자리가 등차수열이면 True 반환
def is_hansu(n: int) -> bool:   
    num = str(n)
    if len(num) <= 2:
        return True
        
    prev = int(num[1]) - int(num[0])
    for i in range(2, len(num)):
        if int(num[i]) - int(num[i - 1]) != prev:
            return False
    return True


N = int(input())

cnt = 0   # 한수의 갯수 카운트
for n in range(1, N + 1):
    if is_hansu(n):
        cnt += 1

print(cnt)



# 실행 결과: 성공(메모리:30840kb, 시간:72ms)