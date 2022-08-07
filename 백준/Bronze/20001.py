# https://www.acmicpc.net/problem/20001
# 문제20001번.고무오리 디버깅
# 시간: 1초, 메모리: 512MB



# 입력
'''
1. '고무오리 디버깅 시작'
2. '고무오리' 또는 '문제'
- 최대 100줄
3. '고무오리 디버깅 끝'이 주어질 때까지 2번 반복
'''



# 출력
'''
1. 고무오리 디버깅이 끝날 떄, 주어진 문제를 모두 해결했으면 '고무오리야 사랑해' 출력, 한문제라도 남았다면 '힝구' 출력
- 풀 문제가 없는데 고무오리를 사용한다면, 두 문제가 추가됨
'''



# 코드
import sys

sys.stdin = open('input_text/20001.txt', 'r', encoding='UTF-8')

start = input()
problem = 0   # 문제 수
while True:
    input_val = input()
    # 반복문 종료 조건
    if input_val == '고무오리 디버깅 끝':
        if problem:
            print('힝구')
        else: 
            print('고무오리야 사랑해')
        break
    elif input_val == '문제':
        problem += 1
    elif input_val == '고무오리':
        if problem:
            problem -= 1
        else:
            problem += 2



# 실행 결과: 성공(메모리:30840kb, 시간:80ms)