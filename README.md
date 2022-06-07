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

### 2つのリストに重複する要素を抽出

```python
l1 = [1, 2, 3, 4]
l2 = [3, 4, 5, 6]
s1 = set(l1) # &はリスト・タプルに実装されていないため，setオブジェクトに一度変換する
s2 = set(l2)
print(s1 & s2)  #=> {3, 4}
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
