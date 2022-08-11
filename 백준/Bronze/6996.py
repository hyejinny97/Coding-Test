# https://www.acmicpc.net/problem/6996
# 문제6996번.애너그램
# 시간: 1초, 메모리: 128MB



# 입력
'''
1. 테스트 케이스 수 T
- T < 100
2. 두 단어 문자열
- 0 < 단어 길이 <= 100
- 오직 알파벳 소문자
'''



# 출력
'''
1. 애너그램이면 예제 출력과 같은 방식으로 출력
- 애너그램: 단어 A의 알파벳 순서를 바꿔서 B를 만들 수 있다면 애너그램이라고 함
'''



# 코드 1
import sys

sys.stdin = open('input_text/6996.txt')

T = int(input())

for _ in range(T):
    A, B = input().split()

    # 소문자 a ~ z가 인덱스인 리스트 만들기
    # ord('a') = 97, ord('z') = 122
    alph = [0] * 26

    # A 단어 각 알파벳 갯수 카운트
    for a in A:
        alph[ord(a) - 97] += 1
    # B 단어 각 알파벳 갯수 카운트
    for b in B:
        alph[ord(b) - 97] -= 1
    
    # alph의 모든 값이 0이면 애너그램
    for cnt in alph:
        if cnt != 0:
            print(f'{A} & {B} are NOT anagrams.')
            break
    else:   # break없이 반복문을 빠져나왔다면 애너그램
        print(f'{A} & {B} are anagrams.')



# 실행 결과: 성공(메모리:30840kb, 시간:72ms)



# 코드 2
import sys

sys.stdin = open('input_text/6996.txt')

T = int(input())

for _ in range(T):
    A, B = input().split()
    
    if sorted(A) == sorted(B):
        print(f'{A} & {B} are anagrams.')
    else:
        print(f'{A} & {B} are NOT anagrams.')



# 실행 결과: 성공(메모리:30840kb, 시간:68ms)