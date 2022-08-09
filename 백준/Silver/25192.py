# https://www.acmicpc.net/problem/25192
# 문제25192번.인사성 밝은 곰곰이
# 시간제한:1초, 메모리제한:1024MB



# 입력
'''
1. 채팅방의 기록 수 N
- 1 <= N <= 100,000
2. N개의 줄에 새로운 사람의 입장을 나타내는 ENTER, 혹은 채팅을 입력한 유저의 닉네임이 문자열로 주어짐
- 1 <= 닉네임 크기 <= 20
- 첫번째 문자열은 반드시 ENTER
'''



# 출력
'''
1. 채팅 기록 중 곰곰티콘이 사용된 횟수 출력
- 새로운 사람이 입장한 이후(ENTER 등장 이후) 처음 채팅을 입력하는 사람은 곰곰티콘으로 인사함
'''



# 코드
import sys

sys.stdin = open('input_text/25192.txt')

N = int(input())

log_cnt = 0
chatted = set()   # 채팅한 사람 기록 
emoticon = 0   # 곰곰이콘 사용 횟수  
while log_cnt < N:
    log = input()
    
    # 입장 후 처음 채팅한 사람이면, 곰곰이콘 사용
    if log != 'ENTER':
        if log not in chatted:
            emoticon += 1
            chatted.add(log)
    # ENTER가 등장할 경우, 채팅 기록이 리셋됨
    elif log == 'ENTER':
        chatted.clear()
    
    log_cnt += 1

print(emoticon)



# 실행 결과: 성공(메모리:42108kb, 시간:3856ms)