# https://school.programmers.co.kr/learn/courses/30/lessons/72410
# 문제.신규 아이디 추천



# 입력
'''
1. 신규 유저가 입력한 아이디(new_id)
- 1 <= new_id의 길이 <= 1,000
- 알파벳 대문자, 알파벳 소문자, 숫자, 특수문자로 구성
- 특수문자는 -_.~!@#$%^&*()=+[{]}:?,<>/ 로 한정
'''



# 출력
'''
1. 7단계의 처리 과정을 거친 후의 추천 아이디를 return
- 신규 유저가 입력한 아이디가 카카오 아이디 규칙에 맞는 지 검사하고 규칙에 맞지 않은 경우 규칙에 맞는 새로운 아이디를 추천

<카카오 아이디의 규칙>
- 3 <= 아이디의 길이 <= 15
- 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.) 문자만 사용가능
- 단, 마침표(.)는 처음과 끝에 사용할 수 없으며 또한 연속으로 사용할 수 없음

<규칙에 맞는 새로운 아이디를 추천하는 과정>
1) 모든 대문자를 소문자로 치환
2) 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거
3) 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환
4) 마침표(.)가 처음이나 끝에 위치한다면 제거
5) 빈 문자열이라면, new_id에 "a"를 대입
6-1) 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거
6-2) 만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거
7) new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙임
'''



# 코드 1
import sys

sys.stdin = open('input_text/신규아이디추천.txt')

def solution(new_id):
    answer = ''
    special = {'-', '_', '.'}
    upper_alph = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    lower_alph = set('abcdefghijklmnopqrstuvwxyz')
    nums = set('0123456789')

    # 규칙에 맞는 새로운 아이디를 추천
    def recommendation(id):
        # 1) 모든 대문자를 소문자로 치환
        rule_1 = ''
        for i in range(len(id)):
            if id[i] in upper_alph:
                rule_1 += chr(ord(id[i]) + 32)
                continue
            rule_1 += id[i]
        # 2) 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거
        rule_2 = ''
        for i in range(len(rule_1)):
            if rule_1[i] in special or rule_1[i] in lower_alph or rule_1[i] in nums:
                rule_2 += rule_1[i]
        # 3) 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환
        rule_3 = ''
        for i in range(len(rule_2)):
            if rule_2[i] == '.' and i - 1 >= 0 and rule_2[i - 1] == '.':
                continue
            rule_3 += rule_2[i]
        # 4) 마침표(.)가 처음이나 끝에 위치한다면 제거
        rule_4 = rule_3
        if rule_3[0].startswith('.'):
            rule_4 = rule_4[1:]
        if rule_3[-1].endswith('.'):
            rule_4 = rule_4[:-1]
        # 5) 빈 문자열이라면, new_id에 "a"를 대입
        rule_5 = rule_4
        if not rule_4:
            rule_5 = 'a'
        # 6-1) 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거
        rule_6 = rule_5[:15]
        # 6-2) 만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거
        rule_7 = rule_6
        if rule_6[-1] == '.':
            rule_7 = rule_6[:-1]
        # 7) new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙임
        recommendation_id = rule_7
        if len(rule_7) <= 2:
            while len(recommendation_id) < 3:
                recommendation_id += rule_7[-1]

        return recommendation_id


    # 신규 유저가 입력한 아이디가 카카오 아이디 규칙에 맞는지 검사
    # 1) 3 <= 아이디의 길이 <= 15
    if not(3 <= len(new_id) <= 15):
        answer = recommendation(new_id)
        return answer
    # 2) 마침표(.)는 처음과 끝에 사용할 수 없음
    if new_id[0] == '.' or new_id[-1] == '.':
        answer = recommendation(new_id)
        return answer
    # 3) 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.) 문자만 사용가능
    # 4) 마침표(.)는 연속으로 사용할 수 없음
    for i in range(len(new_id)):
        if not(new_id[i] in special or new_id[i] in lower_alph or new_id[i] in nums):
            answer = recommendation(new_id)
            return answer
        if new_id[i] == '.' and i + 1 < len(new_id) and new_id[i + 1] == '.':
            answer = recommendation(new_id)
            return answer
    answer = new_id
    return answer

for _ in range(5):
    new_id = input()
    print(solution(new_id))
        

# 실행 결과: 성공



# 코드 2
# 참고(정규표현식으로 풀이): https://sumim.tistory.com/entry/Kakao-Blind-%EC%8B%A0%EA%B7%9C-%EC%95%84%EC%9D%B4%EB%94%94-%EC%B6%94%EC%B2%9C
# 참고(re.sub 메서드): https://docs.python.org/ko/3/library/re.html?highlight=re#re.sub
# 참고(re.sub 메서드): https://ponyozzang.tistory.com/335
# 참고(re.sub 메서드): https://dojang.io/mod/page/view.php?id=2438

import sys
import re

sys.stdin = open('input_text/신규아이디추천.txt')

def solution(new_id):
    # 1) 모든 대문자를 소문자로 치환
    new_id = new_id.lower()
    # 2) 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거
    new_id = re.sub('[^a-z0-9-_.]', '', new_id)
    # 3) 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환
    new_id = re.sub('[.]+', '.', new_id)
    # 4) 마침표(.)가 처음이나 끝에 위치한다면 제거
    new_id = new_id[1:] if new_id.startswith('.') else new_id
    new_id = new_id[:-1] if new_id.endswith('.') else new_id
    # 5) 빈 문자열이라면, new_id에 "a"를 대입
    new_id = 'a' if not new_id else new_id
    # 6-1) 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거
    # 6-2) 만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거
    new_id =  new_id[:15][:-1] if new_id[:15][-1] == '.' else new_id[:15]
    # 7) new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙임
    new_id = new_id + new_id[-1] * (3 - len(new_id)) if len(new_id) <= 2 else new_id
    
    return new_id

for _ in range(5):
    new_id = input()
    print(solution(new_id))


# 실행 결과: 성공



# 코드 3
# 참고(정규 표현식 cheat sheet): https://chrisjune-13837.medium.com/%EC%A0%95%EA%B7%9C%EC%8B%9D-%ED%8A%9C%ED%86%A0%EB%A6%AC%EC%96%BC-%EC%98%88%EC%A0%9C%EB%A5%BC-%ED%86%B5%ED%95%9C-cheatsheet-%EB%B2%88%EC%97%AD-61c3099cdca8
import sys
import re

sys.stdin = open('input_text/신규아이디추천.txt')

def solution(new_id):
    # 1) 모든 대문자를 소문자로 치환
    new_id = new_id.lower()
    # 2) 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거
    new_id = re.sub('[^a-z0-9-_.]', '', new_id)
    # 3) 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환
    new_id = re.sub('[.]+', '.', new_id)
    # 4) 마침표(.)가 처음이나 끝에 위치한다면 제거
    new_id = re.sub('^[.]|[.]$', '', new_id)
    # 5) 빈 문자열이라면, new_id에 "a"를 대입
    new_id = 'a' if not new_id else new_id
    # 6-1) 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거
    # 6-2) 만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거
    new_id =  re.sub('[.]$', '', new_id[:15])
    # 7) new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙임
    new_id = new_id + new_id[-1] * (3 - len(new_id)) if len(new_id) <= 2 else new_id
    
    return new_id

for _ in range(5):
    new_id = input()
    print(solution(new_id))

    
# 실행 결과: 성공