N = int(input())
S = input()
point = 0

# 100の位
for i in range(10):
  # SのN-2番目までにiがあるか
  str_i = str(i)
  for a in range(N-2):
    if S[a] == str_i:
      now_i = a
      print("i = ", i, "================================================================")
      print("===== now_i", now_i, "str_i", str_i)
      break
  else: # 作れなかった場合打ち切り
    continue
  # 10の位
  for j in range(10):
    str_j = str(j)
    for b in range(now_i+1, N-1):
      if S[b] == str_j:
        now_j = b
        print("===== now_j", now_j, "str_j", str_j)
        break
    else:
      continue
    # 1の位
    for k in range(10):
      str_k = str(k)
      for c in range(now_j+1, N):
        if S[c] == str_k: # 暗証番号完成
          point += 1
          print("===== str_k", str_k)
          print(str_i, str_j, str_k, sep='')
          print()
          break
print(point)


# =================================
# 参考記事
# https://algo-archit.hatenablog.com/entry/2020/06/17/131859