# 6084: 소리 파일 저장용량 계산하기
# 시간제한:2초 / 메모리제한:128MB

h, b, c, s = map(int, input().split())
print(f'{((h * b * c * s) / (8 * 1024 * 1024)):.1f} MB')