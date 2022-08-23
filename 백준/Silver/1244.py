# https://www.acmicpc.net/problem/1244
# 문제1244번.스위치 켜고 끄기
# 시간제한:2초, 메모리제한:128MB



# 입력
'''
1. 스위치 갯수
- 0 < 스위치 갯수 <= 100
2. 각 스위치의 상태
- 1부터 연속적으로 번호가 붙어있는 스위치들
- 1: 스위치가 켜져 있음
- 0: 스위치가 꺼져 있음
3. 학생 수
- 0 < 학생 수 <= 100
4. 한 학생의 성별, 학생이 받은 수
- 성별: 1은 남학생, 2는 여학생
- 0 < 학생이 받은 수 <= 스위치 갯수
'''



# 출력
'''
1. 스위치 상태를 1번 스위치에서 시작하여 마지막 스위치까지 한 줄에 20개씩 출력
- 예를 들어, 21번 스위치가 있다면 이 스위치의 상태는 둘째 줄에 출력
- 1: 켜진 스위치
- 0: 꺼진 스위치
<스위치 조작 방법>
- 자신의 성별과 받은 수에 따라 스위치 조작
- 남학생: 스위치 번호가 자기가 받은 수의 배수이면, 그 스위치 상태를 바꿈
- 여학생: 자기가 받은 수와 같은 번호가 붙은 스위치를 중심으로 좌우가 대칭이면서 가장 많은 스위치를 포함하는 구간을 찾아서, 그 구간에 속한 스위치의 상태를 모두 바꿈(이때, 구간에 속한 스위치 개수는 항상 홀수)
'''



# 코드 1
import sys

sys.stdin = open('input_text/1244.txt')

# 스위치 정보 입력 받기
N = int(input())
switch = [None] + list(map(int, input().split()))   # 인덱스: 스위치 번호, 값: 스위치 on/off

# 학생별 번호 정보 받기
nums = int(input())
for _ in range(nums):
    sex, num = map(int, input().split())
    # 남자인 경우, 배수의 스위치 상태 바꿈
    if sex == 1:
        for i in range(num, N + 1, num):
            switch[i] = 0 if switch[i] == 1 else 1 
    
    # 여자인 경우, 받은 수 중심으로 대칭이면서 가장 많은 스위치가 포함된 구간의 상태 바꿈
    elif sex == 2:
        switch[num] = 0 if switch[num] == 1 else 1 
        left = num - 1
        right = num + 1 
        while left > 0 and right <= N:
            if switch[left] == switch[right]:
                switch[left] = 0 if switch[left] == 1 else 1 
                switch[right] = 0 if switch[right] == 1 else 1 
                left -= 1
                right += 1
            else:
                break

# 한 줄에 20개씩 끊어서 출력
start = 1
while start <= N:
    print(*switch[start:start + 20])
    start += 20



# 실행 결과: 성공(메모리:30840kb, 시간:84ms)



# 코드 2
import sys

sys.stdin = open('input_text/1244.txt')

# 스위치 정보 입력 받기
N = int(input())
switch = [None] + list(map(int, input().split()))   # 인덱스: 스위치 번호, 값: 스위치 on/off

# 학생별 번호 정보 받기
change = {0:1, 1:0}
nums = int(input())
for _ in range(nums):
    sex, num = map(int, input().split())
    # 남자인 경우, 배수의 스위치 상태 바꿈
    if sex == 1:
        for i in range(num, N + 1, num):
            switch[i] = change[switch[i]]
    
    # 여자인 경우, 받은 수 중심으로 대칭이면서 가장 많은 스위치가 포함된 구간의 상태 바꿈
    elif sex == 2:
        switch[num] = change[switch[num]]
        left = num - 1
        right = num + 1 
        while left > 0 and right <= N and switch[left] == switch[right]:
            switch[left] = change[switch[left]]
            switch[right] = change[switch[right]]
            left -= 1
            right += 1

# 한 줄에 20개씩 끊어서 출력
start = 1
while start <= N:
    print(*switch[start:start + 20])
    start += 20



# 실행 결과: 성공(메모리:30840kb, 시간:80ms)