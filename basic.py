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
# 1 - 1, 字典创建
dic1 = {}
keys = ['a', 'c', 'b']
values = [1, 3, 2]

for i in range(len(keys)):
    dic1[keys[i]] = values[i]

# 遍历 1- 1：
for k, v in dic1.items():
    print(k, v)
# output: a 1, c 3, b 2

# 根据key值排列 1 - 1
dic1_sorted = sorted(dic1.items(), key=lambda x: x[0])
# print dic1_sorted 后的key，value值
for sk, v in dic1_sorted:
    print(sk, v)
# output: a 1, b 2, c 3

# 根据value值排列 1 - 1
dic1_sorted = sorted(dic1.items(), key=lambda x: x[1])
# print dic1_sorted 后的key，value值
for k, sv in dic1_sorted:
    print(k, sv)
# output: a 1, b 2, c 3

# 1 - 2, 字典创建 - value为list
dic2 = {}
keys = ['a', 'b', 'c']
value_1 = [1, 2, 3]
value_2 = [-1, -2, -3]

for i in range(len(keys)):
    dic2[keys[i]] = [value_1[i], value_2[i]]

# 遍历 1 - 2：
for k, v in dic2.items():
    print(k, v[0], v[1])
# output: a 1 -1, b 2 -2, c 3 -3

# 根据key值排列 1 - 2
dic2_sorted = sorted(dic2.items(), key=lambda x: x[0])
# 根据value[0]的值排列 1 - 2
dic2_sorted = sorted(dic2.items(), key=lambda x: x[1][0])
# 根据value[1]的值排列 1 - 2
dic2_sorted = sorted(dic2.items(), key=lambda x: x[1][1])
# 优先根据value[0]值排列，value[0]相同的情况下，根据value[1]值排列 1 - 2
dic2_sorted = sorted(dic2.items(), key=lambda x: (x[1][0], x[1][1]))

# 1 - 3, 字典创建 - value为结构体
dic3 = {}
keys = ['a', 'b', 'c']
value_1 = [1, 2, 3]
value_2 = [-1, -2, -3]

for i in range(len(keys)):
    dic3[keys[i]] = {'value_1': value_1[i], 'value_2': value_2[i]}

# 遍历 1 - 3：
for k, v in dic3.items():
    print(k, v['value_1'], v['value_2'])
# output: a 1 -1, b 2 -2, c 3 -3

# 根据key值排列 1 - 3
dic3_sorted = sorted(dic3.items(), key=lambda x: x[0])
# 根据value['value_1']的值排列 1 - 3
dic3_sorted = sorted(dic3.items(), key=lambda x: x[1]['value_1'])
# 根据value['value_2']的值排列 1 - 3
dic3_sorted = sorted(dic3.items(), key=lambda x: x[1]['value_2'])
# 优先根据value['value_1']值排列，value['value_1']相同的情况下，根据value['value_2']值排列 1 - 3
dic3_sorted = sorted(dic3.items(), key=lambda x: (x[1]['value_1'], x[1]['value_2']))

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








