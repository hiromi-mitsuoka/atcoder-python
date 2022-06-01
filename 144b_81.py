N = int(input())

list = []
# NOTE: 最初に候補を全て計算しておく
for i in range(1, 10):
  for j in range(1, 10):
    list.append(i*j)

# NOTE: 配列内にNがあるかどうか
result = N in list
if result:
  print("Yes")
else:
  print("No")
