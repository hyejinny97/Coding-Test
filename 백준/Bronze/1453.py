# https://www.acmicpc.net/problem/1453
# 문제1453번.피시방 알바
# 시간: 2초, 메모리: 128MB



# 입력
'''
1. 손님의 수 N
- 0 < N <= 100
2. 손님이 들어오는 순서대로 각 손님이 앉고 싶어하는 자리
'''



# 출력
'''
1. 거절당하는 사람의 수 출력
- 말한 번호에 다른 손님이 앉아있으면 거절당함
'''



# 코드 
import sys

sys.stdin = open('input_text/1453.txt')

N = int(input())
seats = [False] * (100 + 1)   # 인덱스: 0 ~ 100번 컴퓨터, 값: 앉아있는 손님 여부

people = map(int, input().split())
cnt = 0   # 거절당하는 사람 수
for p in people:
    if seats[p]:
        cnt += 1
    else:
        seats[p] = True
print(cnt)



# 실행 결과: 성공(메모리:30840kb, 시간:88ms)