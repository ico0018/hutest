## 变量类型转换
# 1， integer to string
num = 10
num_str = str(num)
# 2， string to integer
num_str = '10'
num = int(num_str)

## 循环
# 1， for
for i in range(1, 10):
    print(i)
# output: 1, 2, 3, 4, 5, 6, 7, 8, 9

# 2， while
i = 0
while i < 10:
    print(i)
    i += 1
# output: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

## 判断
# 1， if
num = 5
if num == 1:
    print('num == 1')
elif num == 2:
    print('num == 2')
else:
    print('num != 1 and num != 2')
# output: num != 1 and num != 2

## array处理
# 1， 遍历array
arr = [1, 2, 3, 4, 5]
for i in arr:
    print(i)
# 2， array排序
arr = [1, 3, 2, 5, 4]
arr.sort()

## 字典处理
# 1， 遍历字典
dic = {'a': 1, 'b': 2, 'c': 3}
for key, value in dic.items():
    print(key, value)
# output: a 1, b 2, c 3
# 2， 字典排序
dic = {'a': 1, 'c': 3, 'b': 2}
sorted(dic.items(), key=lambda x: x[0])
# output: [('a', 1), ('b', 2), ('c', 3)]

## 矩阵处理
# 1， 矩阵转置
matrix = [[1, 2, 3], [4, 5, 6],[7, 8, 9]]
matrix_t = list(map(list, zip(*matrix)))
# output: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]






