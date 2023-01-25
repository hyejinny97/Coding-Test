# https://school.programmers.co.kr/learn/courses/30/lessons/42577?language=python3
# 코딩테스트연습 < 해시 < 문제.전화번호 목록



# 입력
'''
1. 전화번호부에 적힌 전화번호를 담은 배열 phone_book
- 1 <= phone_book 길이 <= 1,000,000
- 1 <= 전화번호 길이 <= 20
- 같은 전화번호가 중복해서 들어있지는 않음
'''



# 출력
'''
1. 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return
'''



# 코드 1
def solution(phone_book):
    # 전화번호부 오름차순으로 정렬
    phone_book.sort()

    # 첫번째 전화번호부터 일치하는지 확인
    for i in range(0, len(phone_book)):     
        for j in range(i + 1, len(phone_book)):
            if phone_book[j][0:len(phone_book[i])] == phone_book[i]:
                return False
    return True


# 실행 결과: 성공



# 코드 2

# 접근방법
'''
phone_book = ['119', '19', '1092']일 때,
주의) 문자열을 오름차순 정렬하면 phone_book = ['1092', '119', '19']가 됨!
숫자 문자열을 사전 순으로 정렬한 경우, 뒤에 있는 문자열은 앞의 문자열에 일부 문자열을 더한 것이거나 동일한 위치에 앞의 문자열보다 큰 숫자가 배치된 경우일 뿐이다. 
따라서, 한 전화번호를 나머지 모든 전화번호와 비교할 필요없이 인접한 두 문자열끼리만 비교하면 된다.
'''

def solution(phone_book):
    # 전화번호부를 문자열 오름차순으로 정렬
    phone_book.sort()

    # 인접한 두 전화번호가 일치하는지 확인
    for i in range(0, len(phone_book) - 1): 
        now = phone_book[i]
        next = phone_book[i + 1]
        if len(now) <= len(next) and next[0:len(now)] == now:
            return False
    return True


# 실행 결과: 성공



# 코드 3

# 접근방법
'''
startswith 메소드 참고: https://www.w3schools.com/python/ref_string_startswith.asp
'''

def solution(phone_book):
    # 전화번호부를 문자열 오름차순으로 정렬
    phone_book.sort()

    # 인접한 두 전화번호가 일치하는지 확인
    for i in range(0, len(phone_book) - 1): 
        now = phone_book[i]
        next = phone_book[i + 1]
        if next.startswith(now):
            return False
    return True


# 실행 결과: 성공