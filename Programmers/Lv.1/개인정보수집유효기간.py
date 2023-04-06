# https://school.programmers.co.kr/learn/courses/30/lessons/150370
# 코딩테스트연습 < 2023 KAKAO BLIND RECRUITMENT < 문제.개인정보 수집 유효기간



# 입력
'''
1. 오늘 날짜를 의미하는 문자열 today
- "YYYY.MM.DD" 형태
2. 약관의 유효기간을 담은 1차원 문자열 배열 terms
- 1 ≤ terms의 길이 ≤ 20
- terms의 원소: "약관 종류 유효기간"
    - 약관 종류: A~Z중 알파벳 대문자 하나
    - 유효 기간: 개인정보를 보관할 수 있는 달 수(1 <= 기간 <= 100)
3. 수집된 개인정보의 정보를 담은 1차원 문자열 배열 privacies
- 1 ≤ privacies의 길이 ≤ 100
- privacies의 원소: "날짜 약관 종류"
    - 날짜: "YYYY.MM.DD"
'''



# 출력
'''
1. 파기해야 할 개인정보의 번호를 오름차순으로 1차원 정수 배열에 담아 return
'''



# 코드 1
import sys

sys.stdin = open('input_text/개인정보수집유효기간.txt')

# 현재 날짜(date)에서 일정 기간(period)가 지난 후의 날짜를 반환
def calc_date(date, period):
    year, month, day = map(int, date.split('.'))
    period = int(period)
    
    if (month + period) > 12:
        year += 1
        month = (period + month) - 12
    else:
        month = period + month
    
    if day == 1:
        month -= 1
        day = 28
    else:
        day -= 1

    return '.'.join(map(lambda x: str(x).zfill(2), [year, month, day]))


def solution(today, terms, privacies):
    # 약관 종류 및 유효 기간
    tot_terms = dict(map(lambda term: term.split(), terms))
    
    # 유효기간이 끝난 개인정보 찾기
    rst = []
    for i in range(len(privacies)):
        privacy = privacies[i]
        date, term = privacy.split()
        if calc_date(date, tot_terms[term]) < today:
            rst.append(i + 1)

    return rst


# 실행 결과: 실패(이유: 1 <= 유효기간 <= 100)



# 코드 2
import sys

sys.stdin = open('input_text/개인정보수집유효기간.txt')

# 현재 날짜(date)에서 일정 기간(period)가 지난 후의 날짜를 반환
def calc_date(date, period):
    year, month, day = map(int, date.split('.'))
    month += int(period) - 1   # 임시로 month를 0 ~ 11월로 취급
    
    year += month // 12
    month %= 12
    
    if day == 1:
        month -= 1
        day = 28
    else:
        day -= 1

    return '.'.join(map(lambda x: str(x).zfill(2), [year, month + 1, day]))


def solution(today, terms, privacies):
    # 약관 종류 및 유효 기간
    tot_terms = dict(map(lambda term: term.split(), terms))
    
    # 유효기간이 끝난 개인정보 찾기
    rst = []
    for i in range(len(privacies)):
        privacy = privacies[i]
        date, term = privacy.split()
        if calc_date(date, tot_terms[term]) < today:
            rst.append(i + 1)

    return rst


# 실행 결과: 성공