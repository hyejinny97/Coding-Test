# https://school.programmers.co.kr/learn/courses/30/lessons/42583
# 코딩테스트연습 < 스택/큐 < 문제.다리를 지나는 트럭



# 입력
'''
1. 다리에 올라갈 수 있는 트럭 수 bridge_length
- 1 <= bridge_length <= 10,000
2. 다리가 견딜 수 있는 무게 weight
- 1 <= weight <= 10,000
3. 트럭 별 무게 truck_weights
- 1 <= truck_weights 길이 <= 10,000
- 1 <= 트럭 무게 <= weight
'''



# 출력
'''
1. 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 return
- 트럭은 다리를 정해진 순으로 건너야 함
'''



# 코드 1

# 접근방법
'''
bridge_length = 2, weight = 10kg

경과시간  다리를 지난 트럭   다리를 건너는 트럭   대기 트럭
0                            0 0                  7 4 5 6
1         0                  0 7                  4 5 6
2         0 0                7 0                  4 5 6
3         0 0 7              0 4                  5 6
4         0 0 7 0            4 5                  6
5         0 0 7 0 4          5 0                  6
6         0 0 7 0 4 5        0 6              
7         0 0 7 0 4 5 0      6 0
8         0 0 7 0 4 5 0 6    0 0
'''
import sys
from collections import deque

sys.stdin = open('input_text/다리를지나는트럭.txt')

def solution(bridge_length, weight, truck_weights):
    trucks_standby = deque(truck_weights) # 대기 트럭
    trucks_crossing = deque([0] * bridge_length) # 다리를 건너는 트럭 
    weight_exit = 0 # 다리를 지난 트럭의 총 무게
    tot_trucks_weight = sum(truck_weights)
    tot_time = 0
    while weight_exit != tot_trucks_weight:
        # 다리를 건너는 트럭 → 다리를 지난 트럭
        weight_exit += trucks_crossing.popleft()

        # 대기 트럭 → 다리를 건너는 트럭
        if trucks_standby and sum(trucks_crossing) + trucks_standby[0] <= weight:
            trucks_crossing.append(trucks_standby.popleft())
        else:
            trucks_crossing.append(0)
        
        tot_time += 1
    
    return tot_time


# 실행 결과: 실패(TC 5번만 시간초과 - sum(trucks_crossing)의 시간복잡도: O(n))



# 코드 2
import sys
from collections import deque

sys.stdin = open('input_text/다리를지나는트럭.txt')

def solution(bridge_length, weight, truck_weights):
    trucks_standby = deque(truck_weights) # 대기 트럭
    trucks_crossing = deque([0] * bridge_length) # 다리를 건너는 트럭 
    weight_crossing = 0 # 다리를 건너는 트럭 총 무게
    weight_exit = 0 # 다리를 지난 트럭의 총 무게
    tot_trucks_weight = sum(truck_weights) # 전체 트럭의 총 무게
    tot_time = 0
    while weight_exit != tot_trucks_weight:
        # 다리를 건너는 트럭 → 다리를 지난 트럭
        exit_truck = trucks_crossing.popleft()
        weight_exit += exit_truck
        weight_crossing -= exit_truck

        # 대기 트럭 → 다리를 건너는 트럭
        if trucks_standby and weight_crossing + trucks_standby[0] <= weight:
            enter_truck = trucks_standby.popleft()  # 다리 위로 올라갈 트럭
            trucks_crossing.append(enter_truck)
            weight_crossing += enter_truck
        else:
            trucks_crossing.append(0)
        
        tot_time += 1
    
    return tot_time


# 실행 결과: 성공