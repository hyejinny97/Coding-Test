# https://www.acmicpc.net/problem/2857
# 문제2857번.FBI
# 시간: 0.25초, 메모리: 128MB



# 입력
'''
1. 5개의 줄에 요원의 첩보원명
- 첩보원명: 알파벳 대문자, 숫자 0~9, - 으로만 구성됨
- 최대 10글자
'''



# 출력
'''
1. FBI요원이 몇 번째 입력으로 주어졌는지 출력
- 첩보원명에 FBI가 들어가 있음
- FBI요원이 없다면 'HE GOT AWAY!' 출력
'''



# 코드
import sys

sys.stdin = open('input_text/2857.txt')

FBI_num = []
for num in range(1, 5 + 1):
    name = input()

    if 'FBI' in name:
        FBI_num.append(num)

if FBI_num:
    print(*FBI_num)
else:
    print('HE GOT AWAY!')



# 실행 결과: 성공(메모리:30840kb, 시간:68ms)