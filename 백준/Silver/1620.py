# https://www.acmicpc.net/problem/1620
# 문제1620번.나는야 포켓몬 마스터 이다솜
# 시간: 2초, 메모리: 256MB



# 입력
'''
1. 도감에 수록되어 있는 포켓몬의 개수 N, 내가 맞춰야 하는 문제의 개수 M
- 1 <= N, M <= 100,000
2. N개의 줄에 1번부터 N번까지의 포켓몬
- 포켓몬 이름: 첫 글자만 대문자, 나머지는 소문자
- 2 <= 이름 길이 <= 20
3. M개의 줄에 내가 맞춰야하는 문제
- 문제가 알파벳 또는 숫자로 들어옴
- 1 <= 숫자 <= N
- 문자는 반드시 도감에 있는 포켓몬의 이름만 주어짐
'''



# 출력
'''
1. M개의 줄에 각각의 문제에 대한 답을 출력
- 문제가 알파벳으로 들어오는 경우: 포켓몬 번호를 출력
- 문제가 숫자로 들어오는 경우: 포켓몬 번호에 해당하는 포켓몬의 이름을 출력
'''



# 코드 1
import sys

sys.stdin = open('input_text/1620.txt')

N, M = map(int, input().split())
pokemons = {}

for n in range(1, N + 1):
    pokemon = input()
    pokemons[str(n)] = pokemon
    pokemons[pokemon] = n

for _ in range(M):
    q = input()
    print(pokemons[q])


# 실행 결과: 시간초과



# 코드 2
import sys

sys.stdin = open('input_text/1620.txt')

N, M = map(int, input().split())
pokemons = {}

for n in range(1, N + 1):
    pokemon = sys.stdin.readline().rstrip()
    pokemons[str(n)] = pokemon
    pokemons[pokemon] = n

for _ in range(M):
    q = sys.stdin.readline().rstrip()
    print(pokemons[q])


# 실행 결과: 성공(메모리:57880kb, 시간:280ms)