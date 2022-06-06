def divisor(n):
  i = 1
  table = []
  while i * i <= n:
    if n % i == 0:
      table.append(i)
      table.append(n//i)
    i += 1
  table = list(set(table)) # set(): 重複取り除き，set(集合) に変換
  # table.sort()
  return len(table)

N = int(input())

count = 0
for i in range(1, N+1, 2):
  if divisor(i) == 8:
    count += 1

print(count)
