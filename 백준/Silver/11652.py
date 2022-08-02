# https://www.acmicpc.net/problem/11652
# 문제11652번.카드
# 시간: 1초, 메모리: 256MB



# 입력
'''
1. 가지고 있는 숫자 카드의 갯수 N
- 1 <= N <= 100,000
2. N개의 줄에 숫자 카드에 적혀 있는 정수
- -2^62 <= 정수 <= 2^62
'''



# 출력
'''
1. 가장 많이 가지고 있는 정수 출력
- 가장 많이 가지고 있는 정수가 여러 개라면, 가장 작은 것을 출력
'''



# 코드 1
import sys, collections

sys.stdin = open('input_text/11652.txt')

# 카드의 각 숫자에 해당하는 갯수 기록
N = int(input())
cards = collections.Counter(int(sys.stdin.readline().strip()) for _ in range(N))   # 키: 카드 숫자, 값: 숫자 갯수

# 가장 많은 숫자 출력
max_cnt = 0
max_num = []
for num in cards:
    if cards[num] > max_cnt:
        max_num = [num]   # 초기화
        max_cnt = cards[num]   # 갱신
    elif cards[num] == max_cnt:
        max_num.append(num)

print(min(max_num))



# 실행 결과: 성공(메모리:42696kb, 시간:188ms)



# 코드 2
import sys, collections

sys.stdin = open('input_text/11652.txt')

# 카드의 각 숫자에 해당하는 갯수 기록
N = int(input())
cards = collections.Counter(int(sys.stdin.readline().strip()) for _ in range(N))   # 키: 카드 숫자, 값: 숫자 갯수

# 가장 많은 숫자 출력
# card[1](숫자 갯수)을 기준으로 내림차순 정렬
# card[1](숫자 갯수)가 동일하다면, card[0](숫자)을 기준으로 오름차순으로 정렬
print(sorted(cards.items(), key=lambda card: (card[1], -card[0]), reverse=True)[0][0])



# 실행결과(메모리:59028KB, 시간:200ms)