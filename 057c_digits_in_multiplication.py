def divisor(n):
  i = 1
  table = []
  while i * i <= n:
    if n % i == 0:
      table.append(i)
      table.append(n//i)
    i += 1
  # table = list(set(table)) # set(): 重複取り除き，set(集合) に変換
  table.sort()
  return table

n = int(input())
divisor = divisor(n)

ans = 10**10
while len(divisor) > 0:
  a = divisor.pop(0)
  b = divisor.pop(-1)
  if len(str(a)) >= len(str(b)):
    tmp = len(str(a))
  else:
    tmp = len(str(b))
  if ans > tmp:
    ans = tmp

print(ans)
