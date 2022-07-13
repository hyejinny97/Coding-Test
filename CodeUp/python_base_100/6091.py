# 6091: 함께 문제 푸는 날
# 시간제한:1초 / 메모리제한:128MB
# 공배수

# 풀이1
a, b, c = map(int, input().split())
day = 1
while True:
    if day % a == 0 and day % b == 0 and day % c == 0:
        print(day)
        break
    day += 1

# 풀이2
a, b, c = map(int, input().split())
day = 1
while True:
    if day % a != 0 or day % b != 0 or day % c != 0:
        day += 1
    else:    
        print(day)
        break
    