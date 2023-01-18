# https://school.programmers.co.kr/learn/courses/30/lessons/87390
# 코딩테스트연습 < 월간 코드 챌린지 시즌3 < 문제.n^2 배열 자르기



# 입력
'''
1. 정수 n, left, right
- 1 <= n <= 10^7
- 0 <= left <= right < n^2
- right - left < 10^5
'''



# 출력
'''
1. 1차원 배열을 return

<1차원 배열 만드는법>
1. n x n 크기의 2차원 배열을 만듦
2. 1행 1열부터 i행 i열까지의 영역 내의 모든 빈 칸을 숫자 i로 채움
3. 각 행을 잘라내어 모두 이어붙여 1차원 배열을 만듦
4. 1차열 배열의 idx = left부터 idx = right까지만 남김
'''



# 코드

# 접근방법
'''
<빈 칸에 값을 채우는 방법>
n x n 크기의 2차원 배열에서 
행이 0부터 (n-1)까지 있고, 열도 0부터 (n-1)까지 있다고 할 때
r행 c열에 들어가야하는 값 = max(r+1, c+1)

<새로운 1차원 배열 배열에서 특정 인덱스가 몇번째 행열에 있었는지 아는 방법>
10번째 인덱스(#10)의 (r, c) = (10 // n) 행, (10 % n) 열

<left ~ right까지의 수 구하는 방법>
left = 2, right = 4일때
[2번 인덱스(#2)의 값, ..., 4번 인덱스(#4)의 값]을 구해야 함
즉, n = 3일때 
[#2, #3, #4]
=> [(2 // 3)행 (2 % 3)열, (3 // 3)행 (3 % 3)열, (4 // 3)행 (4 % 3)열]
=> [0행2열, 1행0열, 1행1열]
=> [max(0+1, 2+1), max(1+1, 0+1), max(1+1, 1+1)]
=> [3, 2, 2]
'''

import sys

sys.stdin = open('input_text/n2배열자르기.txt')

def solution(n, left, right):
    answer = []
    for idx in range(left, right + 1):
        answer.append(max(idx // n + 1, idx % n + 1))
    return answer


# 실행 결과: 성공