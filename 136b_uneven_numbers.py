N = int(input())
cnt = 0

for i in range(1, N+1):
  s = str(i)
  if len(s) % 2 != 0:
    cnt += 1

print(cnt)
