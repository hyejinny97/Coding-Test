# https://www.acmicpc.net/problem/10769
# 문제10769번.행복한지 슬픈지
# 시간: 1초, 메모리: 256MB



# 입력
'''
1. 문자
- 1 <= 문자 길이 <= 255
'''



# 출력
'''
1. 다음 규칙에 따라 출력
<규칙>
1) 어떤 이모티콘도 없으면, none 출력
2) 둘 다 동일하게 포함되어있으면, unsure 출력
3) 행복이 슬픔보다 많으면, happy 출력
4) 슬픔이 행복보다 많으면, sad 출력
'''



# 코드 1
import sys

sys.stdin = open('input_text/10769.txt')

sentance = input()
happy = sentance.count(':-)')
sad = sentance.count(':-(')

if happy == 0 and sad == 0:
    print('none')
elif happy == sad:
    print('unsure')
elif happy > sad:
    print('happy')
elif happy < sad:
    print('sad')



# 실행 결과: 성공(메모리:30840kb, 시간:76ms)



# 코드 2
import sys

sys.stdin = open('input_text/10769.txt')

sentance = input()
happy = 0
sad = 0

# 이모티콘 카운트
for i in range(0, len(sentance) - 3):
    if sentance[i: i + 3] == ':-)':
        happy += 1
    elif sentance[i: i + 3] == ':-(':
        sad += 1

# 출력
if happy == 0 and sad == 0:
    print('none')
elif happy == sad:
    print('unsure')
elif happy > sad:
    print('happy')
elif happy < sad:
    print('sad')



# 실행 결과: 성공(메모리:30840kb, 시간:72ms)