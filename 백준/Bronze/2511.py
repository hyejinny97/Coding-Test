# https://www.acmicpc.net/problem/2511
# 문제2511번.카드 놀이
# 시간: 1초, 메모리: 128MB



# 입력
'''
1. A가 늘어놓은 카드의 숫자들 10개(0부터 9까지)
2. B가 늘어놓은 카드의 숫자들 10개(0부터 9까지)
'''



# 출력
'''
1. A와 B가 받은 총 승점
- 두 숫자 중 튼 숫자를 가진 사람이 승자가 됨
- 승자에게는 3점이 주어짐
- 패자에게는 점수가 주어지지 않음
- 비기면 모두에게 1점이 주어짐
2. 이긴 사람이 A인지 B인지 결정한 후 출력
- 총점이 같은 경우 A와 B중 마지막으로 승부가 난 라운드의 승자가 게임의 최종 승자가 됨
- 만약 비기는 경우 D 출력
'''



# 코드
import sys

sys.stdin = open('input_text/2511.txt')

A = [None] + input().split()
B = [None] + input().split()

A_score = 0
B_score = 0

record = [None] * 11   # 1 ~ 10라운드에서 승자 기록
for idx in range(1, 10 + 1):
    if A[idx] > B[idx]:
        A_score += 3
        record[idx] = 'A'
    elif A[idx] < B[idx]:
        B_score += 3
        record[idx] = 'B'
    else:
        A_score += 1
        B_score += 1
        record[idx] = 'D'

print(A_score, B_score)

if A_score > B_score:
    print('A')
elif A_score < B_score:
    print('B')
else:
    for r in record[::-1]:
        if r == 'A':
            print('A')
            break
        elif r == 'B':
            print('B')
            break
    else:
        print('D')



# 실행 결과: 성공(메모리:30840kb, 시간:72ms)