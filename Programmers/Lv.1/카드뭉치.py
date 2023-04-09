# https://school.programmers.co.kr/learn/courses/30/lessons/159994
# 코딩테스트연습 < 연습문제 < 문제.카드 뭉치



# 입력
'''
1. 문자열로 이루어진 배열 cards1, cards2
- 1 ≤ cards1의 길이, cards2의 길이 ≤ 10
- 1 ≤ cards1[i]의 길이, cards2[i]의 길이 ≤ 10
- cards1과 cards2에는 서로 다른 단어만 존재
2. 원하는 단어 배열 goal
- 2 ≤ goal의 길이 ≤ cards1의 길이 + cards2의 길이
- 1 ≤ goal[i]의 길이 ≤ 10
- goal의 원소는 cards1과 cards2의 원소들로만 이루어져 있음
'''



# 출력
'''
1. cards1과 cards2에 적힌 단어들로 goal를 만들 있다면 "Yes", 만들 수 없다면 "No"를 return

<단어 배열 규칙>
1. 원하는 카드 뭉치에서 카드를 '순서대로' 한 장씩 사용
2. 한 번 사용한 카드는 다시 사용할 수 없음
3. 카드를 사용하지 않고 다음 카드로 넘어갈 수 없음
4. 기존에 주어진 카드 뭉치의 단어 순서는 바꿀 수 없음
'''



# 코드 
import sys
from collections import deque

sys.stdin = open('input_text/카드뭉치.txt')

def solution(cards1, cards2, goal):
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    for word in goal:
        if cards1 and cards1[0] == word:
            cards1.popleft()
            continue
        if cards2 and cards2[0] == word:
            cards2.popleft()
            continue
        return 'No'

    return 'Yes'


# 실행 결과: 성공

