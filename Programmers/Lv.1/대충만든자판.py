# https://school.programmers.co.kr/learn/courses/30/lessons/160586
# 코딩테스트연습 < 연습문제 < 문제.대충 만든 자판



# 입력
'''
1. 1번 키부터 차례대로 할당된 문자들이 순서대로 담긴 문자열배열 keymap
- 1 ≤ keymap의 길이 ≤ 100
- 1 ≤ keymap의 원소의 길이 ≤ 100
2. 입력하려는 문자열들이 담긴 문자열 배열 targets
- 1 ≤ targets의 길이 ≤ 100
- 1 ≤ targets의 원소의 길이 ≤ 100
'''



# 출력
'''
1. 각 문자열을 작성하기 위해 키를 최소 몇 번씩 눌러야 하는지 순서대로 배열에 담아 return
- 단, 목표 문자열을 작성할 수 없을 때는 -1을 저장
'''


# 코드 
import sys

sys.stdin = open('input_text/대충만든자판.txt')

def solution(keymap, targets):
    result = [] 
    for target in targets:
        tot_cnt = 0
        for char in target:
            cnt = []
            for ele in keymap:
                idx = ele.find(char)
                if idx != -1:
                    cnt.append(idx + 1)
            if cnt:
                tot_cnt += min(cnt)
            else:
                tot_cnt = 0
                break
        result.append(tot_cnt if tot_cnt else -1)
    
    return result


# 실행 결과: 성공