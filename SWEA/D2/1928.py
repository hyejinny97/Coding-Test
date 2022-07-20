# 문제1928.Base64 Decoder
# 시간: 30초, 메모리: 256MB

# 입력
'''
1. 테스트 케이스 개수 T
2. encoding된 상태로 주어지는 문자열
- 문자열의 길이는 항상 4의 배수
- 문자열의 길이 <= 100,000
'''

# 출력
'''
1. #테스트케이스
2. 해당 문자열을 decoding하여 원문을 출력
'''

# 접근방법
'''
<Encoding 과정>
1. 문자 하나를 받아 아스키코드 표를 통해 10진수로 바꾼다
2. 10진수를 1 byte(8 bit)의 2진수로 변환한 후, 2진수들을 한 줄로 쭉 이어붙임
3. 6 bit씩 잘라 10진수로 변환
4. base64 encoding 표를 보고 10진수를 문자로 변환한다

<Decoding 과정>
1. base64 encoding 표를 보고 입력받은 문자열을 각각 대응하는 10진수로 변환
2. 10진수들을 6자리 2진수로 표현하고, 2진수들을 한 줄로 쭉 이어붙임
3. 한 줄로 쭉 이어붙인 2진수들을 8자리씩 끊어서 10진수로 바꾼다
4. 각각의 10진수를 아스키코드 표를 통해 문자로 변환

<요약>
문자 - (아스키코드)10진수 - 8 bit의 2진수 - 6 bit씩 끊어 10진수 변환 - (base64)문자
'''

# 코드
import sys

sys.stdin = open('SWEA/input_text/1928.txt', 'r')

# base64 encoding 표 만들기
base64_str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
base64_table = dict(zip(base64_str, range(0,64)))

T = int(input())
for test_case in range(1, T + 1):
    string = input()
    binarys = ''
    # (base64)문자 -> 10진수 -> 6 bit의 2진수
    for char in string:
        binarys += f'{base64_table[char]:06b}'
   
    # 2진수들을 8 bit씩 끊기 -> 10진수 -> (아스키코드)문자
    start = 0
    rst = ''
    while start < len(binarys):
        byte = binarys[start:start + 8]
        rst += chr(int(byte, 2))
        start += 8

    print(f'#{test_case} {rst}')

# 실행 결과: 성공(메모리:56,676 kb, 시간:148 ms)