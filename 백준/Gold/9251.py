# https://www.acmicpc.net/problem/9251
# 문제9251번.LCS
# 시간: 0.1초, 메모리: 256MB



# 입력
'''
1. 첫째 줄과 둘째 줄에 두 문자열이 주어짐
-  문자열은 알파벳 대문자로만 이루어져 있음
- 0 < 문자열 길이 <= 1,000
'''



# 출력
'''
1. 두 문자열의 LCS의 길이를 출력
- LCS(Longest Common Subsequence, 최장 공통 부분 수열)
'''



# 코드 1

# 접근방법
'''
두 문자열 각각 투 포인터를 사용해 앞에서부터 하나씩 비교해나감

각각 앞에서부터 한칸씩 right 포인터를 옮김
left와 right 포인터 사이에 있는 문자열을 비교
두 문자열에 모두 존재하는 문자열이 있으면 그 문자열 다음으로 left 포인터를 옮김
'''
import sys

sys.stdin = open('input_text/9251.txt')

# def find_char(string, char):  # 문자열 타겟, 찾고자하는 문자
#     string.find(char, left, right)

str1, str2 = input(), input()
left1, left2 = 0, 0
right1, right2 = -1, -1

lcs1, lcs2 = '', ''
max_idx = max(len(str1), len(str2)) - 1
while right1 < max_idx and right2 < max_idx:
    right1 = right1 if right1 == len(str1) -1 else right1 + 1
    right2 = right2 if right2 == len(str2) -1 else right2 + 1

    # str1: 찾고자하는 기준 문자, str2: 비교대상 문자열 
    if right1 >= right2:
        rst1 = str2.find(str1[right1], left2, right2 + 1)
        if rst1 != -1:
            left2 = rst1 + 1
            lcs1 += str1[right1]

    # str2: 찾고자하는 기준 문자, str1: 비교대상 문자열 
    if right2 >= right1:
        rst2 = str1.find(str2[right2], left1, right1 + 1)
        if rst2 != -1:
            left1 = rst2 + 1
            lcs2 += str2[right2]

print(max(len(lcs1), len(lcs2)))

# 실행 결과: 실패



# 코드 2

# 접근방법
'''
참고) https://velog.io/@piopiop/%EB%B0%B1%EC%A4%80-9251-LCS-%ED%8C%8C%EC%9D%B4%EC%8D%AC
'''
import sys

sys.stdin = open('input_text/9251.txt')

str1, str2 = '0' + input(), '0' + input()
lcs = [[0] * len(str1) for _ in range(len(str2))]

for r in range(1, len(str2)):
    for c in range(1, len(str1)):
        if str2[r] == str1[c]:
            lcs[r][c] = lcs[r - 1][c - 1] + 1
        else:
            lcs[r][c] = max(lcs[r - 1][c], lcs[r][c - 1])

print(lcs[-1][-1])


# 실행 결과: 성공(메모리:55712kb, 시간:544ms)