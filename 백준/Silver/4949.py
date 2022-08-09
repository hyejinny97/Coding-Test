# https://www.acmicpc.net/problem/4949
# 문제4949번.균형 잡힌 세상
# 시간: 1초, 메모리: 128MB



# 입력
'''
1. 영문 알파벳, 공백, 소괄호, 대괄호로 구성된 문자열
- 0 < 문자열 길이 <= 100
- 각 문자열은 마침표로 끝남
2. 입력의 종료조건으로 . 하나가 들어옴
'''



# 출력
'''
1. 각 줄마다 해당 문자열이 균형을 이루고 있으면 'yes' 출력, 아니면 'no' 출력
<균형을 이루는 문자열 조건>
- 각 괄호는 짝이 맞아야 한다
'''



# 코드
import sys

sys.stdin = open('input_text/4949.txt')

while True:
    s = input()
    
    # 입력 종료 조건
    if s == '.':
        break

    # 균형 잡힌 문자열인지 확인
    balence = True
    ps = {
        ')':'(',
        ']':'['
    }
    stack = []
    for char in s:
        # 여는 괄호인 경우, 쌓음
        if char == '(' or char == '[':
            stack.append(char)
        # 닫는 괄호인 경우, 해당 짝 제거
        elif char == ')' or char == ']':
            if not stack or stack.pop() != ps[char]:
                balence = False
                break
    if stack:
        balence = False
    
    if balence:
        print('yes')
    else:
        print('no')
            


# 실행 결과: 성공(메모리:30840kb, 시간:368ms)