# https://www.acmicpc.net/problem/9012
# 문제9012번.괄호
# 시간: 1초, 메모리: 128MB



# 입력
'''
1. 테스트 케이스 개수 T
2. T개 줄에 괄호 문자열
- 2 <= 괄호 문자열 길이 <= 50
'''



# 출력
'''
1. 올바른 괄호 문자열(VPS)이면 “YES”, 아니면 “NO”를 출력
'''



# 코드 
import sys

sys.stdin = open('input_text/9012.txt')

N = int(input())

for _ in range(N):
    ps = input()

    left = 0   # 왼쪽 괄호 개수
    rst = 'YES'   # 올바른 괄호 문자열인지
    for char in ps:
        if char == '(':
            left += 1
        else: 
            left -= 1
        
        if left < 0:
            rst = 'NO'
            break
    
    if left:
        rst = 'NO'

    print(rst)
     

# 실행 결과: 성공(메모리:31256kb, 시간:52ms)