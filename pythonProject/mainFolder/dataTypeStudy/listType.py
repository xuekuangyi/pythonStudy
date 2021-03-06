# 字符串和元组是不可变的（常量），而列表list是可变（mutable）的，可以对它进行随意修改。
# 我们还可以将字符串和元组转换成一个列表，只需使用 list 函数来实现该类型转换
str_study = 'hello'  # 字符串类型
tuple_type = ('a', 'b', 'c', 'd')  # 元组类型
list_type = list(str_study)  # 列表类型，强制类型转换
numbers = [1, 2, 3, 4, 5, 5, 7, 8]
def convert_type():
    print(list_type)                                                        # 展示列表内容
    print(type(list(str_study)), str_study, type(list_type), list_type)     # list()方法可以将字符串转为列表
    print(tuple_type, '>>>', list(tuple_type))                              # list()方法可以将元组转为列表

# 常用方法：
# index 方法用于从列表中找出某个元素的位置，如果有多个相同的元素，则返回第一个元素的位置
def index_method():
    elementLookingFor = 5
    print(f'元素5在list{elementLookingFor}中出现的位置是:' + str(numbers.index(elementLookingFor) + 1))  # 返回索引位置编号，从0开始


# count 方法用于统计某个元素在列表中出现的次数。

def counter_appear_times():
    counter = 5
    print(f'元素{counter}在{numbers}共有', numbers.count(counter))  # 对元素出现此次数记数
    print(type(numbers.count(counter)))  # 查看返回的类型是否为int


# app
numbers.append(111)
print(convert_type())
