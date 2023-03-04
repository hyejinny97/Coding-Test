# https://www.acmicpc.net/problem/25501
# 문제25501번.재귀의 귀재
# 시간: 2초, 메모리: 1024MB



# 입력
'''
1. 테스트케이스의 개수 T
- 0 <= T <= 1,000
2. T개의 줄에 알파벳 대문자로 구성된 문자열 S
- 1 <= S 길이 <= 1,000
'''



# 출력
'''
1. isPalindrome 함수의 반환값, recursion 함수의 호출 횟수를 출력
'''



# 코드
import sys

sys.stdin = open('input_text/25501.txt')

def recursion(s, l, r):
  global cycle
  cycle += 1

  if l >= r:
    return 1
  if s[l] != s[r]:
    return 0

  return recursion(s, l + 1, r - 1)


def isPalindrome(s):
  return recursion(s, 0, len(s) - 1)


T = int(input())
for _ in range(T):
  cycle = 0
  s = input()
  print(isPalindrome(s), cycle)


# 실행 결과: 성공(메모리:31316kb, 시간:532ms)