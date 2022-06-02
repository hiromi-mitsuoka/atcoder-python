# S = str(input())
# max_length = 0

# for i in range(len(S)):
#   if S[i] == 'A' or S[i] == 'C' or S[i] == 'G' or S[i] == 'T':
#     tmp = 1
#     for j in range(i+1, len(S)):
#       if S[j] == 'A' or S[j] == 'C' or S[j] == 'G' or S[j] == 'T':
#         tmp += 1
#       else:
#         if tmp > max_length:
#           max_length = tmp
#         tmp = 0
#         break

# print(max_length)

#================================================================
# https://onecheese.com/2021/12/10/atcoder-abc-122-b/

s = input()

cnt = 0
ans = 0
a = ['A', 'C', 'G', 'T']

for i in s:
  if i in a:
    cnt += 1
    ans = max(ans, cnt)
  else:
    cnt = 0

print(ans)
