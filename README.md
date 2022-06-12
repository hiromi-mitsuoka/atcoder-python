# atcoder-python

## 標準入力

### 半角スペース区切りに入力を配列に分解して格納

- 固定長

```python
x, y, z = map(int, input().split())
```

- 可変長

```python
a = list(map(int, input().split())) # 3 11 18 25 40 58 69 81 88 99

print(a)
# [3, 11, 18, 25, 40, 58, 69, 81, 88, 99]
```

- ループ&可変長

```python
k = [None] * m
for i in range(m):
  k[i] = list(map(int, input().split()))
```

- i=0とそれ以外の要素に分けてリストに格納したい場合

```python
n, m = map(int, input().split()) # mを使っているため，一応記載
k = []
s = []
for _ in range(m):
  tmp = list(map(int, input().split()))
  k.append(tmp[0])  # i=0の値のみappend
  s.append(tmp[1:]) # i=1以降を配列にまとめてappend
```


## 標準出力

### 改行しないで出力

```python
print("Hello", end="")
print("world", end="")

# Helloworld
```

### 配列を展開して要素を出力

```python
list = [1,2,3,4,5]

print(list)
# [1, 2, 3, 4, 5]

print(*list) # 空白スペースあり
# 1 2 3 4 5
```

### 空白スペース無しで出力

```python
list = [1,2,3,4,5]

print(*list) # 空白スペースあり
# 1 2 3 4 5

print(*list, sep='')
# 12345
```


## 配列

### 指定の値で埋めた1次元配列の作成

```python
data = [1] * 10

print(data)
# [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
```

### 指定の値で埋めた2次元配列の作成

- 隣接リスト

```python
data = [[] * 3 for i in range(5)]

print(data)
# [[], [], [], [], []]
```

- 隣接行列

```python
data = [[10] * 3 for i in range(5)]

print(data)
# [[10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10]]
```

### indexの指定で，配列から要素を削除（抽出）

```python
list = ['test', 'user', 'password']
pop_word = list.pop(0) # 0: 先頭, -1: 末尾

print(pop_word)
# test

print(list)
# ['user', 'password']
```

### max(), min() *配列以外も可

```python
print(max([10, 20, 30, 20, 50, 30])) # 配列
# 50
print(max(100, 20)) # カンマ区切り
# 100
print(max('A', 'B', 'C', 'D', 'E', 'F')) # 文字列
# F

print(min([10, 20, 30, 20, 50, 30]))
# 10
print(min(100, 20))
# 20
print(min('A', 'B', 'C', 'D', 'E', 'F'))
# A
```

### リスト内を昇順

```python
list = [3, 1, 4, 5, 2]
list.sort() # sort()は返り値=None

print(list)
# [1, 2, 3, 4, 5]
```

### リスト内を降順

```python
list = [3, 1, 4, 5, 2]
list.sort(reverse=True)

print(list)
# [5, 4, 3, 2, 1]
```

- https://maku77.github.io/python/list/overlapped.html

### 多次元配列をソートする（複数キー可能）

```python
data = [['きゅうり',1,4],['いちご',2,6],['にんじん',2,1],['とうふ',1,0]]

sorted_data = sorted(data, key=lambda x:(x[1], x[2])) # 昇順
print(sorted_data)
# [['とうふ', 1, 0], ['きゅうり', 1, 4], ['にんじん', 2, 1], ['いちご', 2, 6]]

sorted_data = sorted(data, key=lambda x:(x[1], x[2]), reverse=True) # 降順
print(sorted_data)
# [['いちご', 2, 6], ['にんじん', 2, 1], ['きゅうり', 1, 4], ['とうふ', 1, 0]]
```

- https://qiita.com/t_kanno/items/13dd226e70d080159d97

### 2つのリストに重複する要素を抽出

```python
l1 = [1, 2, 3, 4]
l2 = [3, 4, 5, 6]
s1 = set(l1) # &はリスト・タプルに実装されていないため，setオブジェクトに一度変換する
s2 = set(l2)
print(s1 & s2)  #=> {3, 4}
```

## 文字列

### 特定の文字列の出現回数を数える

- count()より，Counterの方が高速

```python
from collections import Counter

test = "test user, test password"
counter = Counter(test)

print(counter)
# Counter({'s': 5, 't': 4, 'e': 3, ' ': 3, 'r': 2, 'u': 1, ',': 1, 'p': 1, 'a': 1, 'w': 1, 'o': 1, 'd': 1})

print(counter["t"])
# 4
```

```python
s = 'aAaAAbAccdd'

print(s.count('A'))
# 4

print(s.count('Ac'))
# 1
```

### 任意の文字列を含むか確認

```python
test = "test user"

print("te" in test)
# True

print("password" in test)
# False
```

## 整数

### 桁数を確認する

```python
n = 100
print(len(str(n))) # strに変換する必要あり
# 3
```

### 素因数分解

```python
def prime_decomposition(n):
  i = 2
  table = []
  while i * i <= n: # 探索範囲はルートnまでで十分
    while n % i == 0:
      n //= i
      table.append(i)
    i += 1
  if n > 1:
    table.append(n)
  return table
```

### 約数列挙

```python
def divisor(n):
  i = 1
  table = []
  while i * i <= n:
    if n % i == 0:
      table.append(i)
      table.append(n//i)
    i += 1
  table = list(set(table)) # set(): 重複取り除き，set(集合) に変換
  table.sort()
  return table
```

## ビット演算

### サンプルコード

```python
# ビット探索のサンプルコード: https://amateur-engineer-blog.com/bit-search/
n = 3
patterns = []
for i in range(2**n):
  p = [0] * n
  for j in range(n):
    print(i, j)
    print(i >> j) # j=1の場合i/2，j=2の場合，i/2*2
    if i >> j & 1:
      p[j] = 1
  patterns.append(p)

print(patterns)
# [[0, 0, 0], [1, 0, 0], [0, 1, 0], [1, 1, 0], [0, 0, 1], [1, 0, 1], [0, 1, 1], [1, 1, 1]]
```