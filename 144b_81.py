N = int(input())

list = []

for i in range(1, 10):
  for j in range(1, 10):
    list.append(i*j)

result = N in list
if result:
  print("Yes")
else:
  print("No")
