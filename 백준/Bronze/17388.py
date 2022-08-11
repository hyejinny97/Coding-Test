# https://www.acmicpc.net/problem/17388
# 문제17388번.와글와글 숭고한
# 시간: 1초, 메모리: 512MB



# 입력
'''
1. 숭실대 참여도 S, 고려대 참여도 K, 한양대 참여도 H
- 0 <= S, K, H <= 100
- 세 대학의 참여도는 다름
'''



# 출력
'''
1. 일처리가 잘되고 있어 무언의 압박이 필요 없으면 ok 출력, 아니면 참여도가 젤 낮은 대학 영문 이름 첫 단어 출력
- 참여도 합이 100 이상이면 일처리가 잘 되고 있음
- 100미만이면 일처리 잘 안됨
'''



# 코드
import sys

sys.stdin = open('input_text/17388.txt')

S, K, H = map(int, input().split())
sum_3 = S + K + H

if sum_3 >= 100:
    print('OK')
else:
    low_col = min(S, K, H)   # 가장 낮은 참여도를 보인 대학
    if low_col == S:
        print('Soongsil')
    elif low_col == K:
        print('Korea')
    else:
        print('Hanyang')



# 실행 결과: 성공(메모리:30840kb, 시간:68ms)