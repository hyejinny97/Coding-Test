# 문제10804번.문자열의 거울상
# 시간: 3초, 메모리: 256MB



# 입력
'''
1. 테스트 케이스 T
2. b,d,p,q만으로 이루어진 하나의 문자열
- 1 <= 문자열 길이 <= 1,000
'''



# 출력
'''
1. #{테스트케이스} {문자열을 거울에 비춘 문자열}
'''



# 코드
import sys

sys.stdin = open('../input_text/10804.txt')

# 문자의 거울상
mirror = {
    "b": "d", 
    "d": "b", 
    "p": "q",
    "q": "p"}

T = int(input())
for test_case in range(1, T + 1):
    string = input()

    print(f'#{test_case} ', end="")
    for s in string[::-1]:
        print(mirror[s], end="")
    print()



# 실행 결과: 성공(메모리:63,032 kb, 시간:237 ms)