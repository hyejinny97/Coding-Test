# https://www.acmicpc.net/problem/14696
# 문제14696번.딱지 놓이
# 시간: 2초, 메모리: 512MB



# 입력
'''
1. 딱지놀이의 총 라운드 수 N
- 1 <= N <= 1,000
2. 어린이 A가 내는 딱지 갯수 a, a개의 딱지 그림
3. 어린이 B가 내는 딱지 갯수 b, b개의 딱지 그림
- 1 <= a, b <= 100
- 딱지의 그림은 4(별), 3(원), 2(네모), 1(세모) 중 하나
'''



# 출력
'''
1. 라운드 i줄의 결과
- A가 승자라면 A, B가 승자라면 B, 무승부라면 D를 출력
<규칙>
1) 만약 두 딱지의 별의 개수가 다르다면, 별이 많은 쪽의 딱지가 이긴다.
2) 별의 개수가 같고 동그라미의 개수가 다르다면, 동그라미가 많은 쪽의 딱지가 이긴다.
3) 별, 동그라미의 개수가 각각 같고 네모의 개수가 다르다면, 네모가 많은 쪽의 딱지가 이긴다.
4) 별, 동그라미, 네모의 개수가 각각 같고 세모의 개수가 다르다면, 세모가 많은 쪽의 딱지가 이긴다.
5) 별, 동그라미, 네모, 세모의 개수가 각각 모두 같다면 무승부이다.
'''



# 코드 1
import sys

sys.stdin = open('input_text/14696.txt')

N = int(input())

for _ in range(N):
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    # 어린이 A,B 각각 card 내 모양 갯수 기록
    card_a = [0] * 5   # 인덱스: 1~4번모양, 값: 각 모양의 갯수
    card_b = [0] * 5
    for shape in a[1:]:
        card_a[shape] += 1
    for shape in b[1:]:
        card_b[shape] += 1
    
    # 현재 라운드의 결과 출력
    for shape in range(4, 0, -1):
        if card_a[shape] == card_b[shape]:
            continue
        elif card_a[shape] > card_b[shape]:
            print("A")
            break
        else:
            print("B")
            break
    else:
        print("D")



# 실행 결과: 성공(메모리:30840kb, 시간:256ms)



# 코드 2
import sys

sys.stdin = open('input_text/14696.txt')

N = int(input())

for _ in range(N):
    a = sorted(input().split()[1:], reverse=True)
    b = sorted(input().split()[1:], reverse=True)

    # 현재 라운드의 결과 출력
    if a > b:
        print('A')
    elif a < b:
        print('B')
    else:
        print('D')



# 실행 결과: 성공(메모리:30840kb, 시간:228ms)