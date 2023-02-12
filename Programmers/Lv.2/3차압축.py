# https://school.programmers.co.kr/learn/courses/30/lessons/17684
# 코딩테스트연습 < 2018 KAKAO BLIND RECRUITMENT < 문제.[3차] 압축



# 입력
'''
1. 문자열 msg
- 입력으로 영문 대문자로만 이뤄짐
- 1 <= msg 길이 <= 1,000
'''



# 출력
'''
1. 주어진 문자열을 압축한 후의 사전 색인 번호를 배열로 출력
- 아래 압축 알고리즘은 영문 대문자만 처리

<무손실 압축 알고리즘 - LZW 압축>
1. 길이가 1인 모든 단어(A-Z)를 포함하도록 사전을 초기화
2. 사전에서 현재 입력과 일치하는 가장 긴 문자열 w를 찾음
3. w에 해당하는 사전의 색인 번호를 출력한 후, 입력에서 w를 제거
4. 입력에서 처리되지 않은 다음 글자가 남아있다면(c), w+c에 해당하는 단어를 사전에 등록
5. 단계 2로 돌아가 반복
'''


# 코드 
import sys

sys.stdin = open('input_text/3차압축.txt')

def solution(msg):
    # 초기 사전(A-Z 포함) 
    dictionary = dict(zip('ABCDEFGHIJKLMNOPQRSTUVWXYZ', range(1, 26 + 1)))

    # 메시지를 읽어가면서 색인번호 찾기 및 사전 등록
    max_idx = 26   # 사전 최대 색인 번호
    all_idx = []   # 사전 색인 번호
    idx = 0        # 메시지에서 확인할 현재 인덱스
    while idx < len(msg):
        # 사전에 존재하는 부분 문자열 최대 길이 구하기
        length = 0     # 부분 문자열 길이
        while (idx + length) < len(msg) and dictionary.get(msg[idx:idx + length + 1]):
            length += 1
        
        # 색인번호 찾기
        next_idx = idx + length   # 부분 문자열 직후의 인덱스
        all_idx.append(dictionary[msg[idx:next_idx]])

        # 다음 글자가 남아있다면, 사전에 등록
        if next_idx < len(msg):
            dictionary[msg[idx:next_idx + 1]] = max_idx + 1
            max_idx += 1
        
        idx = next_idx

    return all_idx


# 실행 결과: 성공