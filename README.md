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
