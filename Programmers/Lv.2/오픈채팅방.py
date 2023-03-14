# https://school.programmers.co.kr/learn/courses/30/lessons/42888
# 코딩테스트연습 < 2019 KAKAO BLIND RECRUITMENT < 문제.오픈채팅방



# 입력
'''
1. 채팅방에 들어오고 나가거나, 닉네임을 변경한 기록이 담긴 문자열 배열 record
- 1 <= record 길이 <= 100,000
- record 원소: "[Enter|Leave|Change] [유저 아이디] [닉네임]"
- 1 <= 유저 아이디, 닉네임 <= 10
- 유저 아이디, 닉네임: 알파벳 대문자, 소문자를 구별함
'''



# 출력
'''
1. 모든 기록이 처리된 후, 최종적으로 방을 개설한 사람이 보게 되는 메시지를 문자열 배열 형태로 return
- 채팅방에서 누군가 들어오면 "[닉네임]님이 들어왔습니다." 메시지가 출력됨
- 채팅방에서 누군가 나가면 "[닉네임]님이 나갔습니다." 메시지가 출력됨

<채팅방에서 닉네임을 변경하는 방법>
1. 채팅방을 나간 후, 새로운 닉네임으로 다시 들어간다.
2. 채팅방에서 닉네임을 변경한다.
- 닉네임을 변경할 때는 기존에 채팅방에 출력되어 있던 메시지의 닉네임도 전부 변경됨
'''


# 코드 
import sys

sys.stdin = open('input_text/오픈채팅방.txt')

def solution(records):
    id_nickname = {}      # key: user id, value: nickname
    entry_history = []    # 출입 내역 ([유저 아이디], [Enter|Leave])
    for record in records:
        record = record.split()

        # user의 id와 nickname 기록(기존 id가 있는 경우 이전 nickname 덮어쓰기)
        if record[0] == 'Leave':
            entry, user_id = record
        else:
            entry, user_id, nickname = record
            id_nickname[user_id] = nickname

        # 출입 내역 순서대로 기록
        if entry != 'Change':
            entry_history.append((user_id, entry))

    # 출입 내역에 따라 결과 메시지 작성하기
    result = []
    for user_id, entry in entry_history:
        if entry == 'Enter':
            result.append(f'{id_nickname[user_id]}님이 들어왔습니다.')
        elif entry == 'Leave':
            result.append(f'{id_nickname[user_id]}님이 나갔습니다.')

    return result
print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))

# 실행 결과: 성공