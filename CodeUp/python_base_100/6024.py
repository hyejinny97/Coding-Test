# 6024: 단어 2개 입력받아 이어 붙이기
# 시간제한:1초 / 메모리제한:128MB
# 풀이1
w1, w2 = input().split()
print(w1 + w2)

# 풀이2
w1, w2 = input().split()
print(w1, w2, sep='')

# 풀이3
word = input().split()
print(''.join(word))