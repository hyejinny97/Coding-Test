# https://school.programmers.co.kr/learn/courses/30/lessons/17686
# 코딩테스트연습 < 2018 KAKAO BLIND RECRUITMENT < 문제.[3차] 파일명 정렬



# 입력
'''
1. 배열 files
- files: 파일명을 포함하는 문자열 배열
- 0 < files 길이 <= 1,000
- 파일명: 영문 대소문자/숫자/공백/마침표/빼기 부호로 구성, 영문자로 시작하며 숫자를 하나 이상 포함
- 0 < 파일명 길이 <= 100
'''



# 출력
'''
1. 기준에 따라 정렬된 배열을 출력

<파일 정렬 기준>
1. 파일명을 HEAD, NUMBER, TAIL의 세 부분으로 나눔
   - HEAD: 최소한 한 글자 이상의 문자
   - NUMBER: 한 글자에서 최대 다섯 글자 사이의 연속된 숫자(앞에 0이 올 수 있음)
   - TAIL: 나머지 부분(숫자, 문자일 수 있고, 아무 글자도 없을 수 있음)
2. 우선 HEAD 부분을 기준으로 사전 순으로 정렬
   - 대소문자 구분을 하지 않음
3. 다음으로 NUMBER의 숫자 순으로 정렬
   - 숫자 앞의 0은 무시
4. HEAD와 NUMBER 부분이 같을 경우, 원래 입력에 주어진 순서를 유지해 정렬
'''



# 코드 1
import sys, re

sys.stdin = open('input_text/3차파일명정렬.txt')

def solution(files):
    # 각 파일명의 (HEAD, NUMBER)만 추출
    new_files = []   # (HEAD, NUMBER, 원래 file명)
    for file in files:
        head = re.search('[a-zA-Z .-]+', file).group()
        number = re.search('[0-9]+', file).group()
        new_files.append((head.lower(), number[:5].lstrip('0'), file))
    
    # 기준에 따라 정렬
    ordered_files = sorted(new_files, key=lambda file: (file[0], int(file[1])))

    return [file[2] for file in ordered_files]


# 실행 결과: 실패(일부 TC 런타임에러, 이유: NUMBER가 '0'일때 strip을 하면 ''인 상태인데 여기서 int 형 변환하면 문제가 됨)



# 코드 2
import sys, re

sys.stdin = open('input_text/3차파일명정렬.txt')

def solution(files):
    # 각 파일명의 (HEAD, NUMBER)만 추출
    new_files = []   # (HEAD, NUMBER, 원래 file명)
    for file in files:
        head = re.search('[a-zA-Z .-]+', file).group()
        number = re.search('[0-9]+', file).group()
        new_files.append((head.lower(), number[:5], file))
    print(new_files)
    # 기준에 따라 정렬
    ordered_files = sorted(new_files, key=lambda file: (file[0], int(file[1])))

    return [file[2] for file in ordered_files]


# 실행 결과: 성공