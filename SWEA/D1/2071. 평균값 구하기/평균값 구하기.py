T = int(input())
for test_case in range(1, T + 1):
    nums = list(map(int, input().split()))
    print(f'#{test_case} {round(sum(nums)/len(nums))}')