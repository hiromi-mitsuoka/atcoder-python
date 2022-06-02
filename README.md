# atcoder-python

## 標準入力

### 半角スペース区切りに入力を配列に分解して格納


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

```python
data = [[10] * 3 for i in range(5)]

print(data)
# [[10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10]]
```
