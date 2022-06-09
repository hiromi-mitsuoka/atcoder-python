a,b,c,x,y = map(int, input().split())
ans = 10**10
for i in range(10**5+1): # 2c = a+b になるため，2cに着目して全探索する
  ans = min(ans, a*max(x-i, 0) + b*max(y-i, 0) + 2*c*i) # a, bはそれぞれ，ABをi枚買った時に，買い増しが必要かどうかチェックする
print(ans)


# #  =================================================================
# # 公式解説: https://img.atcoder.jp/arc096/editorial.pdf
# ポイント
# - ABピザを奇数枚買って，1枚余らせるのは無意味なため，ABピザは2枚1組 → 2*c → ABに着目して全探索するのが一番効率が良い