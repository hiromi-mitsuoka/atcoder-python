n, m = map(int, input().split())
k = []
s = []
for _ in range(m):
  tmp = list(map(int, input().split()))
  k.append(tmp[0])
  s.append(tmp[1:])
p = list(map(int, input().split()))

ans = 0
for i in range(2**n): # ビット探索で全パターンをまず列挙→テンプレ使える
  switch = [0]*n
  for j in range(n):
    if i >> j & 1:
      switch[j] = 1

  print("========== switch", switch)

  # 全ての電球が点灯するか
  check = True
  for j in range(m):
    k_sum = 0
    for s_i in range(k[j]):
      k_sum += switch[s[j][s_i]-1]
      print("switch[s[j][s_i]-1]", switch[s[j][s_i]-1], "k_sum", k_sum, "p[j]", p[j])
    if k_sum % 2 != p[j]:
      check = False
      break
  if check:
    ans += 1

print(ans)

# =================================================================
# 参考記事: https://amateur-engineer-blog.com/bit-search/