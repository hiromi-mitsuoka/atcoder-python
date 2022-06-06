# def divisor(n):
#   i = 1
#   table = []
#   while i * i <= n:
#     if n % i == 0:
#       table.append(i)
#       table.append(n//i)
#     i += 1
#   table = list(set(table)) # set(): 重複取り除き，set(集合) に変換
#   table.sort()
#   return table

a, b, k = map(int, input().split())

# set_a = set(divisor(a))
# set_b = set(divisor(b))

# duplication = list(set_a & set_b)
# duplication.sort(reverse=True)
# # print(duplication)
# print(duplication[k-1])

list = []
for i in range(100, 0, -1):
  if a % i == 0 and b % i == 0:
    list.append(i)

# print(list)
print(list[k-1])