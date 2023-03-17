# https://school.programmers.co.kr/learn/courses/30/lessons/49993
# 코딩테스트연습 < Summer/Winter Coding(~2018) < 문제.스킬트리



# 입력
'''
1. 선행 스킬 순서 skill
- 알파벳 대문자
- 1 <= skill의 길이 <= 26
- 1 <= skill_trees는 길이 <= 20
- 2 <= skill_trees의 원소는 길이 <= 26
2. 유저들이 만든 스킬트리를 담은 배열 skill_trees
'''



# 출력
'''
1. 가능한 스킬트리 개수를 return
'''


# 코드 
import sys

sys.stdin = open('input_text/스킬트리.txt')

def solution(skill, skill_trees):
    cnt = 0  # 가능한 스킬트리 개수
    for skill_tree in skill_trees:
        next = 0  # 다음에 학습해야할 스킬
        for cur_skill in skill_tree:
            if cur_skill in skill:
                if cur_skill == skill[next]:
                    next += 1
                    continue
                break
        else:
            cnt += 1

    return cnt


# 실행 결과: 성공