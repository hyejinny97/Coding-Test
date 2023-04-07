# https://school.programmers.co.kr/learn/courses/30/lessons/92334
# 코딩테스트연습 < 2022 KAKAO BLIND RECRUITMENT < 문제.신고 결과 받기



# 입력
'''
1. 이용자의 ID가 담긴 문자열 배열 id_list
- 2 ≤ id_list의 길이 ≤ 1,000
2. 각 이용자가 신고한 이용자의 ID 정보가 담긴 문자열 배열 report
- 1 ≤ report의 길이 ≤ 200,000
- 3 ≤ report의 원소 길이 ≤ 21
- report의 원소: "이용자id 신고한id"
- 한 유저는 서로 다른 유저를 계속해서 신고 가능하고, 동일한 유저를 여러번 신고도 가능하지만 이때 신고 횟수는 1회로 처리됨
3. 정지 기준이 되는 신고 횟수 k
- 1 ≤ k ≤ 200
'''



# 출력
'''
1. 각 유저별로 처리 결과 메일을 받은 횟수를 배열에 담아 return
- k번 이상 신고된 유저는 게시판 이용이 정지되며, 해당 유저를 신고한 모든 유저에게 정지 사실을 메일로 발송됨
- id_list에 담긴 id 순서대로 각 유저가 받은 결과 메일 수를 반환
'''



# 코드
import sys

sys.stdin = open('input_text/신고결과받기.txt')

def solution(id_list, reports, k):
    user_reporting = dict()  # 각 유저별 신고한 유저 id (사용자 id : {신고당한 id})
    cnt_reported = dict()  # 각 유저별 신고 당한 횟수 (신고당한 id : 횟수)
    for report in reports:
        user_id, reported_id = report.split()
        
        # 유저별 신고당한 횟수 카운트
        if reported_id not in user_reporting.get(user_id, []):
            cnt_reported[reported_id] = cnt_reported.get(reported_id, 0) + 1

        # 유저별 신고한 id 기록
        if user_reporting.get(user_id):
            user_reporting[user_id].add(reported_id)
        else:
            user_reporting[user_id] = {reported_id}
        
    rst = []
    for user_id in id_list:
        cnt = 0   # 각 유저가 받은 결과 메일 수
        for reported_id in user_reporting.get(user_id, []):
            if cnt_reported.get(reported_id, 0) >= k:
                cnt += 1
        rst.append(cnt)
    
    return rst  


# 실행 결과: 성공
