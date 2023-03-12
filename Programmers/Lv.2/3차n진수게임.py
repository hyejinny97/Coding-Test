# https://school.programmers.co.kr/learn/courses/30/lessons/17687
# 코딩테스트연습 < 2018 KAKAO BLIND RECRUITMENT < 문제.[3차] n진수 게임



# 입력
'''
1. 진법 n
- 2 ≦ n ≦ 16
2. 미리 구할 숫자의 갯수 t
- 0 < t ≦ 1,000
3. 게임에 참가하는 인원 m
- 2 ≦ m ≦ 100
4. 튜브의 순서 p
- 1 ≦ p ≦ m
'''



# 출력
'''
1. 튜브가 말해야 하는 숫자 t개를 공백 없이 차례대로 나타낸 문자열을 출력
- 단, 10~15는 각각 대문자 A~F로 출력

<N진수 게임 규칙>
- 여러 사람이 둥글게 앉아서 숫자를 하나씩 차례대로 말하는 게임
1. 숫자를 0부터 시작해서 차례대로 말한다.
2. 10 이상의 숫자부터는 한 자리씩 끊어서 말한다. 
'''


# 코드

# 접근방법
'''
----------- 문제1 -----------
n = 2, t = 4, m = 2, p = 1

숫자   0 1 2  3  4   5   6   7   8    9    10   11   12   ...
n진법  0 1 10 11 100 101 110 111 1000 1001 1010 1011 1100 ...

순서   0 1 2 3 4 5 6 7 8 9 10 ...
한자리 0 1 1 0 1 1 1 0 0 1  0 ...
튜브   ✔   ✔   ✔   ✔

----------- 문제2 -----------
n = 16, t = 16, m = 2, p = 1

숫자   0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 ... 26
n진법  0 1 2 3 4 5 6 7 8 9  a  b  c  d  e  f 10 11 12 13 14 ... 1a
 
순서   0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 ...
한자리 0 1 2 3 4 5 6 7 8 9  a  b  c  d  e  f  1  0  1  1  1  2 ...
튜브   ✔   ✔   ✔   ✔   ✔    ✔     ✔     ✔     ✔     ✔     ✔    ...

<10진수를 n진수로 변환>
- string.digits ⇒ 0123456789
- string.ascii_lowercase ⇒ abcdefghijklmnopqrstuvwxyz
- ex) 26(10진수)을 16진수로 변환
    
    16 | 26
        ---   ... 10
    16 | 1
        ---   ... 1
         0

    => 1 + 10(a)  = 1a
    => 즉, 몫이 0이 될 때까지 나머지를 구해야 함
(참고: https://security-nanglam.tistory.com/508)

<접근방법>
- n진수으로 변환한 숫자 개수가 최소 m(인원 수) x t(튜브가 말해야하는 숫자 개수)만큼 있어야 함
'''
import sys, string

sys.stdin = open('input_text/3차n진수게임.txt')

# 10진수 → n진수로 변환
zero_to_z = string.digits + string.ascii_uppercase  # 숫자 0-9 + 대문자 A-Z
def convert(num, base):
    q, r = divmod(num, base)  # 몫, 나머지
    if q == 0:
        return zero_to_z[r]
    else:
        return convert(q, base) + zero_to_z[r]

def solution(n, t, m, p):
    # n진수 총 개수가 최소 m(인원 수) x t(튜브 개수)이 되도록 쌓기
    num = 0               # 변환되어야할 10진수
    converted_nums = ''   # 변환된 모든 n진수
    while len(converted_nums) < m * t:
        converted_nums += convert(num, n)
        num += 1

    # 튜브가 말해야하는 숫자 찾기
    result = ''
    for cycle in range(t):
        result += converted_nums[(cycle * m - 1) + p]

    return result


# 실행 결과: 성공