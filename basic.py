## 变量类型转换
# 1， integer to string
num = 10
num_str = str(num)
# 2， string to integer
num_str = '10'
num = int(num_str)
# 3, 大写字母转换成小写字母
num_str = 'ABC'
num_str.lower()
# 4，小写字母转换成大写字母
num_str = 'abc'
num_str.upper()

## 判断字符
# 1， 判断字符是否是数字
num_str.isdigit()
# 2， 判断字符是否是字母
num_str.isalpha()
# 3， 判断字符是否是大写字母
num_str.isupper()
# 4， 判断字符是否是小写字母
num_str.islower()


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

## array处理，string字符串处理方式和array一样
# 初始化
arr = 5 * [0]
arr = [1, 2, 3, 4, 5]
# 1， 遍历array
for i in arr:
    print(i)
# 2， array排序
arr.sort()
# 3, array取一位
arr[0]
# output: 1
# 4, array取多位
arr[0:2]
# output: [1, 2]
# 5, array取除了第一位的后面所有位
arr[1:]
# output: [2, 3, 4, 5]
# 6, array取除了最后一位的前面所有位
arr[:-1]
# output: [1, 2, 3, 4]

## string字符串的填充
str = 'abc'
str = str.ljust(5, '0')
# output: 'abc00'
str = str.rjust(5, '0')
# output: '00abc'
str = str.center(5, '0')
# output: '0abc0'
str = str[1:].zfill(9)
# output: '000000abc'

str = "Hello, World!"
str = str.fill('*', 6, 11)  # 将索引6到11之间的部分替换为星号
# output: "Hello, *****!"


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
# 2, 矩阵创建
matrix = [[0 for i in range(3)] for j in range(3)]
# output: [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# 3，矩阵填充
matrix = [[0 for i in range(3)] for j in range(3)]
for i in range(3):
    for j in range(3):
        matrix[i][j] = 1
# output: [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
# 4, 矩阵遍历
matrix = [[1, 2, 3], [4, 5, 6],[7, 8, 9]]
for row in matrix:
    for col in range(len(matrix[0])):
        print(row[col])
# output: 1, 2, 3, 4, 5, 6, 7, 8, 9








