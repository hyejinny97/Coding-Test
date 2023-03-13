# https://school.programmers.co.kr/learn/courses/30/lessons/92341
# 코딩테스트연습 < 2022 KAKAO BLIND RECRUITMENT < 문제.주차 요금 계산



# 입력
'''
1. 주차 요금을 나타내는 정수 배열 fees
- fees의 길이 = 4
- fees[0] = 기본 시간(분), 1 ≤ fees[0] ≤ 1,439
- fees[1] = 기본 요금(원), 0 ≤ fees[1] ≤ 100,000
- fees[2] = 단위 시간(분), 1 ≤ fees[2] ≤ 1,439
- fees[3] = 단위 요금(원), 1 ≤ fees[3] ≤ 10,000

2. 자동차의 입/출차 내역을 나타내는 문자열 배열 records
- 1 ≤ records의 길이 ≤ 1,000
- 원소: "시각 차량번호 내역" 형식의 문자열
- "시각": 차량이 입차되거나 출차된 시각 (HH:MM 형식의 문자열)
- "차량번호": '0'~'9'로 구성된 길이 4인 문자열
- "내역": IN 또는 OUT
- 원소들은 시각을 기준으로 오름차순으로 정렬되어 주어짐
- 하루 동안의 입/출차된 기록만 담고 있음
- 마지막 시각(23:59)에 입차되는 경우는 입력으로 주어지지 않음
'''



# 출력
'''
1. 차량 번호가 작은 자동차부터 청구할 주차 요금을 차례대로 정수 배열에 담아서 return
- 어떤 차량이 입차된 후에 출차된 내역이 없다면, 23:59에 출차된 것으로 간주
- 초과한 시간이 단위 시간으로 나누어 떨어지지 않으면, 올림을 해야함
'''


# 코드 
import sys, math

sys.stdin = open('input_text/주차요금계산.txt')

# 현재 시각을 '분' 단위로 바꿔줌
def change_in_minutes(time):
    hour, minute = time.split(':')
    return int(hour) * 60 + int(minute)

# 주차 요금 계산
def calc_parking_fee(fees, parking_time):
    base_time, base_rate, unit_time, unit_rate = fees
    parking_fee = base_rate
    if base_time < parking_time:
        parking_fee += math.ceil((parking_time - base_time) / unit_time) * unit_rate
    return parking_fee

def solution(fees, records):
    # 자동차의 입/출차 내역에 따라 누적 주차 시간 구하기
    entrance_time = {}          # key: car_num, value: 입차 시간
    acc_parking_time = {}       # key: car_num, value: 누적 주차 시간
    for record in records: 
        time, car_num, state = record.split()
        if state == 'IN':
            entrance_time[car_num] = change_in_minutes(time)
        if state == 'OUT':
            departure_time = change_in_minutes(time)               # 출차 시간
            parking_time = departure_time - entrance_time[car_num] # 주차 시간
            acc_parking_time[car_num] = acc_parking_time.get(car_num, 0) + parking_time
            del entrance_time[car_num]
    
    # 입차 후 출차한 기록이 없는 차량은 23:59에 출차된 것으로 간주
    for car_num in entrance_time:
        parking_time = (24 * 60 - 1) - entrance_time[car_num]   # 주차 시간
        acc_parking_time[car_num] = acc_parking_time.get(car_num, 0) + parking_time

    # 차량 번호가 작은 자동차부터 청구할 주차 요금 구하기
    parking_fee = []
    parking_time_ordered_by_car_num = sorted(acc_parking_time.items(), key=lambda x: x[0])
    for car_num, parking_time in parking_time_ordered_by_car_num:
        parking_fee.append(calc_parking_fee(fees, parking_time))

    return parking_fee


# 실행 결과: 성공