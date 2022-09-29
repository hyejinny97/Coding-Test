# 문제15230번.알파벳 공부
# 시간: 3초, 메모리: 256MB


# 입력
"""
1. 테스트 케이스 수 T
2. 길이 1이상 26이하인 문자열
"""


# 출력
"""
1. #{테스트케이스} {순서는 a부터 순서대로 일치하는 알파벳 개수}
"""


# 코드
import sys

sys.stdin = open("../input_text/15230.txt")

# 알파벳
alph = "abcdefghijklmnopqrstuvwxyz"

T = int(input())
for test_case in range(1, T + 1):
    string = input()

    cnt = 0
    for i in range(len(string)):
        if alph[i] != string[i]:
            break
        cnt += 1

    print(f"#{test_case} {cnt}")


# 실행 결과: 성공(메모리:63,576 kb, 시간:303 ms)
