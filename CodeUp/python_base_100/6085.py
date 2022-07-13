# 6085: 그림 파일 저장용량 계산하기
# 시간제한:1초 / 메모리제한:128MB

w, h, bit = map(int, input().split())
print(f'{((w * h * bit) / (8 * 1024 * 1024)):.2f} MB')