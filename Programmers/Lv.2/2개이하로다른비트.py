# https://school.programmers.co.kr/learn/courses/30/lessons/77885
# 코딩테스트연습 < 월간 코드 챌린지 시즌2 < 문제.2개 이하로 다른 비트



# 입력
'''
1. 정수들이 담긴 배열 numbers
- 1 ≤ numbers의 길이 ≤ 100,000
- 0 ≤ numbers의 모든 수 ≤ 10^15
'''



# 출력
'''
1. numbers의 모든 수들에 대하여 각 수의 f 값을 배열에 차례대로 담아 return

<함수 f(x)>
- 1) x보다 크고, 2) x와 비트가 1~2개 다른 수들 중에서 제일 작은 수
'''


# 코드 1
import sys

sys.stdin = open('input_text/2개이하로다른비트.txt')

def f(num):
    target = num + 1   # num보다 큰 수
    binary_num = f'{num:b}'[::-1]
    while True:
        cnt = 0   # 다른 비트의 개수
        binary_tar = f'{target:b}'[::-1]
        for i in range(len(binary_num)):
            if binary_num[i] != binary_tar[i]:
                cnt += 1
        cnt += abs(len(binary_num) - len(binary_tar))
        
        if 1 <= cnt <= 2:
            return target
        
        target += 1


def solution(numbers):
    rst = []
    for num in numbers:
        rst.append(f(num))

    return rst


# 실행 결과: 실패(시간 초과)



# 코드 2

# 접근방법
'''
1. 정수 x가 짝수인 경우
- 짝수를 2진수로 변환했을 때, 일의 자리수는 0
- 따라서, f(x) = 일의 자리수만 1로 바꿔준 (x + 1)이 됨

2. 정수 x가 홀수인 경우
- f(x) = 가장 뒤에 있는 0의 인덱스(idx)를 찾아 1로 바꾼 후, idx+1 의 인덱스 값을 0으로 바꾸면 됨

참고) https://school.programmers.co.kr/questions/37104
참고) https://velog.io/@kerri/Python-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4Lv2-2%EA%B0%9C-%EC%9D%B4%ED%95%98%EB%A1%9C-%EB%8B%A4%EB%A5%B8-%EB%B9%84%ED%8A%B8
'''
import sys

sys.stdin = open('input_text/2개이하로다른비트.txt')

def f(num):
    binary_num = f'0{num:b}'[::-1]
    if num % 2 == 1:
        for i in range(len(binary_num)):
            if binary_num[i] == '0':
                return num + 2 ** i - 2 ** (i - 1)
    return num + 1


def solution(numbers):
    rst = []
    for num in numbers:
        rst.append(f(num))

    return rst


# 실행 결과: 성공