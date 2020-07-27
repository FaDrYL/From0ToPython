# 变量 & 数据类型
![https://img.shields.io/badge/From%200%20To-Python-blue?style=for-the-badge&logo=Python&logoColor=FFD43B&logoWidth=15&labelColor=566163&color=3776AB](https://img.shields.io/badge/From%200%20To-Python-blue?style=for-the-badge&logo=Python&logoColor=FFD43B&logoWidth=15&labelColor=566163&color=3776AB)

![Github link](https://img.shields.io/badge/FaDrYL--blue?style=social&logo=Github&logoWidth=15&link=https://github.com/FaDrYL)
![Website link](https://img.shields.io/badge/FaDr-YL-blue?style=flat&color=009f9f&link=https://www.fadryl.com/&link=https://www.fadryl.com/)

<br/>

**变量** 用于储存数据.

**数据类型** 是变量的类型.

[[代码示例]](Variables_Data_Types_sample.py)

<br/>

## 变量
在 Python 中，你可以不用提前声明，来创建一个变量。

你只要给一个变量赋值就已经创建了它。

<br/>

### 变量名

Python 有一些命名变量的规则：

- 变量名只能以 字符、数字 或 下划线_ 开头：
  - `variable_name`
  - `_variableName`
  - `variable2`
  - `variable3_`
- 变量名是分大小写的：
  - `variableName` 和 `variablename` 是两个不同的变量.

<br/>

规范:

- 容易阅读:
  - `variable_name`
- 描述性的名字:
  - `x_axis`
  - `website_link`

<br/>

两种变量类型:
- 全局变量
  - 在函数外创建. (我们会在之后讲"函数")
- 局部变量
  - 在函数内创建
  - 不能再函数外访问

<br/>

### 为变量赋值

用等于号 `=` 来为变量赋值。

- `=`的左边：变量名
- `=`的右边：赋值的值

比如:

```Python
#  变量名  |    值
item_name = "the item"   # 字符串
item_price = 9.95        # 数 (浮点数)
item_stock = 10          # 数 (整数)
```

<br/>

#### 多值赋值
##### 1 到 多
Python 允许使用一个值来同时给多个变量赋值

在这个例子里，`var_one`, `var_two` 和 `var_three` 都是 `0`：

```Python
var_one = var_two = var_three = 0
```

<br/>

##### 多 到 多
你可以在一个语句里，同时为多个变量赋值。

使用逗号 `,` 来分割它们：

```Python
var_one, var_two, var_three = 1, 2, "3rd variable"

print(var_one)
print(var_two)
print(var_three)
```

运行上面的代码后的输出：

```
1
2
3rd variable
```

<br/>

## 数据类型
Python 有一些主要的内置数据类型：
- [Number 数](#number)
- [Boolean 布尔值](#boolean)
- [String 字符串](#string)
- [Tuple 元组](#tuple)
- [List 列表](#list)
- [Set 集合](#set)
- [Dictionary 字典](#dictionary)

<br/>


Immutable data 不可变: Number, Boolean, String, Tuple.

Mutable data 可变: List, Set, Dictionary.

<br/>

> 我们可以使用 `type()` 函数来查看这个变量的类型.
> ```Python
> >>> x = 1
> >>> print(type(x))
> <class 'int'>
> ```
> `

<br/>

### Number
Python 有 `int`、 `float` 和 `complex` 类，用于表示数字。（“类”将在后面的章节介绍）

```Python
>>> a_int, a_float, a_complex, second_complex = 100, 5.2, 1+3j, complex(2, 1)
>>> print(type(a_int))
<class 'int'>
>>> print(type(a_float))
<class 'float'>
>>> print(type(a_complex))
<class 'complex'>
>>> print(type(second_complex))
<class 'complex'>
```

> 我们可以使用 `del` 来删除对象（变量）. ("对象"将在后面的章节介绍)
> 删除单个对象: `del var_one`
> 删除多个对象: `del a_int, a_float`

<br/>

### Boolean
布尔值的类是 `bool`.

两个关键字:
- True
- False

```Python
>>> isEnd = False
>>> print(type(isEnd))
<class 'bool'>
>>> print(isEnd)
False
```

<br/>

### String
字符串的类是 `str`.

Python中，字符串使用单引号 `'` 或双引号 `"` 来定义。

```Python
>>> a_string = "String one"
>>> single_quote_string = 'String two'
>>> print(type(a_string))
<class 'str'>
>>> print(type(single_quote_string))
<class 'str'>
```

<br/>

#### Escape Character 转义字符
我们需要使用转义字符来表示一些特殊的字符。（如：单双引号）

使用 `\ ` 加字符来使用转义字符。

```Python
>>> a_string = "\"string\"有双引号."
>>> print(a_strig)
"string"有双引号.
```

转义字符表：

| Escape Sequence | Meaning                        | Notes |
|-----------------|--------------------------------|-------|
| \newline        | Backslash and newline ignored  |       |
| \\              | Backslash (\)                  |       |
| \'              | Single quote (')               |       |
| \"              | Double quote (")               |       |
| \a              | ASCII Bell (BEL)               |       |
| \b              | ASCII Backspace (BS)           |       |
| \f              | ASCII Formfeed (FF)            |       |
| \n              | ASCII Linefeed (LF) (New line) |       |
| \r              | ASCII Carriage Return (CR)     |       |
| \t              | ASCII Horizontal Tab (TAB)     |       |
| \v              | ASCII Vertical Tab (VT)        |       |
| \ooo            | Character with octal value ooo | (1,3) |
| \xhh            | Character with hex value hh    | (2,3) |

来自： [https://docs.python.org/3/reference/lexical_analysis.html#string-and-bytes-literals](https://docs.python.org/3/reference/lexical_analysis.html#string-and-bytes-literals)

<br/>

#### String Slicing
字符串的本质是一组 unicode 字符 （在 Python 里，一个字符是一个长度为 1 的字符串）

所以，你可以在字符串后使用方括号 `[]` 以及 索引 来得到这个字符串中相对应的字符。

索引以 `0` 开始。

同时，我们可以用负数来表示从后往前的索引，如 倒数第一个是 `-1`。

```Python
a_string = "this is a string"
first_char = a_string[0]
last_char = a_string[-1]
print("第一个字符： \'" + first_char + "\', 最后一个字符： \'" + last_char + "\'.")
```

输出:

```
第一个字符： 't', 最后一个字符： 'g'.
```

<br/>

##### 切片
使用 `[]` 加上 开始的索引（包括）、结束的索引（不包括）、以及用 `:` 分开它们 来获得字符串中的部分字符。

```Python
a_string = "Hello, world!"
first_word = a_string[0:5]          # 或 a_string[:5]
remaining_part = a_string[5:]       # 或 a_string[:len(a_string)]
print("a_string 的长度: " + len(a_string))
print("前面的部分: " + first_word)
print("后面的部分: " + remaining_part)
```

输出：

```
a_string 的长度: 13
前面的部分: Hello
后面的部分: , world!
```

<br/>

#### 字符串的内置函数
一些字符串中的内置函数：

使用例子：`a_string = a_string.capitalize()`

带等号 `=` 的参数可以忽略，比如 `string.endswith(".txt")` 等于 `string.endswith(".txt", 0, len(str))`。

| 函数 | 简述 |
|:---:|:----|
| capitalize() | 转换单词首字母为大写 |
| center(width, fillchar) | 返回长度为 *width* 的居中字符串，并以 *fillchar* 填充开头和结尾 |
| encode(encoding="UTF-8", errors="strict") | 返回编码后的字符串 |
| endswith(suffix, beg=0, end=len(string)) | 如果字符串以 *suffix* 结尾，就返回 `True`. 如果 *beg* 或 *end* 有值, 那么只会在这个范围内检查. |
| expandtabs(tabsize=8) | 转换 tab 为长度为 *tabsize* 的空格 (默认是 8) |
| find(str, beg=0, end=len(string)) | 返回字符串从 *beg* 到 *end* 的范围中 *str* 的索引，如果没找到就返回 `-1` |
| format(str1, str2 ...) | 返回根据 (*str1*, *str2*, ...) 格式化后的字符串 |
| index(str, beg=0, end=len(string)) | 跟 find(str) 一样. 但是，如果没有找到，就会抛出异常 |
| isalnum() | 返回 `True`， 如果字符串是以 字母 或 数字 组成 |
| isalpha() | 返回 `True`， 如果字符串是以 字母 组成 |
| isdecimal() | 返回 `True`， 如果字符串是以 数字 组成 (包括 unicode 里的数字字符, 如平方号) |
| isdigit() | 返回 `True`， 如果字符串是以 数字 组成 |
| isidentifier() | 返回 `True`， 如果字符串是一个合规的变量、函数名 |
| islower() | 返回 `True`， 如果字符串都是小写 |
| isnumeric() | 返回 `True`， 如果字符串是以 数字 组成 (包括中文数字) |
| isprintable() | 返回 `True`， 如果字符串是可打印的 |
| isspace() | 返回 `True`， 如果字符串是以 空格 组成 |
| istitle() | 返回 `True`， 如果字符串是标题格式的 (每个单词都以大写开头，其它字母都是小写) |
| isupper() | 返回 `True`， 如果字符串都是大写 |
| join(iterable) | 将 *iterable* 里的元素都加在字符串的后面 |
| ljust(width, fillchar=" ") | 将字符串向左对齐，剩下的部分以 *fillchar* 填充 |
| lower() | 返回全部小写化的字符串 |
| lstrip(char=" ") | 移除开头的 *char* |
| maketrans(intab, outtab) | 返回一个翻译表 （*intab* 中的字母会相对应的变成 *outtab* 中的字母）|
| partition(pivot) | 返回一个根据 *pivot* 分割的长度为 3 的元组 (pivot前, pivot, pivot后) |
| replace(old, new, max=null) | 替换字符串中的 *old* 为 *new*，只会替换 *max* 次 (默认是全部的 *old* 都会被替换掉) |
| rfind(...) | 跟 find() 一样, 但是从右边开始 |
| rindex(...) | 跟 index() 一样, 但是从右边开始 |
| rjust(...) | 跟 ljust() 一样, 但是从右边开始 |
| rpartition(...) | 跟 partition() 一样, 但是从右边开始 |
| rsplit(...) | 跟 split() 一样, 但是从右边开始 |
| rstrip(...) | 跟 strip() 一样, 但是从右边开始 |
| split(str="", num=string.count(str)) | 将字符串以 *str* 分割为列表, 分割 *num* 次 （默认分割全部） |
| splitlines(keepends=False) | 根据行分割为列表. keepends: 保持行分割符？ (默认移除) |
| startswith(prefix, beg=0, end=len(string)) | 返回 `True`， 如果字符串范围 *beg* 到 *end* 间是以 *prefix* 开头 |
| strip(char="") | lstrip(char) 和 rstrip(char) 的结合 |
| swapcase() | 将字符串大小写转换 |
| title() | 转换字符串中所有的单词首字母为大写，剩下的为小写 |
| translate(trans_table, delete="") | 返回根据 *trans_table* 翻译后的字符串，并移除 *delete* 中包含的字符 |
| upper() | 返回大写化的字符串 |
| zfill(width) | 向右对其，并将左边以 `0` 填充 |

[了解更多](https://docs.python.org/3/library/stdtypes.html#string-methods)

<br/>

### Tuple
元组在创建后*不可*更改
- 不可更改 (immutable 不可变的)

元素在 `()` 中， 并以 `,` 分割。

```Python
a_tuple = ("item_1", "item_2")
diff_type_tuple = ("item_1", 100, 1.2)
```

<br/>

#### Tuple Item Accessing
元组可以切片和使用索引访问元素，跟 [String](#string-slicing) 一样。

```Python
a_tuple = ("item_1", "item_2", "3", "4", "5")
print(a_tuple[0])
print(a_tuple[-2])
print(a_tuple[2:4])
```

输出:

```
item_1
4
("3", "4")
```

<br/>

> 我们不能使用 `del item` 来删除元组中的元素。

<br/>

#### 特殊的创建例子
空元组: `tuple_0 = ()`

只有一个元素的元组: `tuple_1 = (100, )`

> 单元素时，不要忘了逗号 `,`!

<br/>

### List
列表是一个重要的数据类型

我们可以在创建后改变它
- 可改变 (mutable 可变的)

可以使用索引来访问
- 有序序列

元素以 `[]` 包裹，并以 `,` 分割。

```Python
a_list = [1, 2, 3, 4, 5]
diff_type_list = [0, "1", 2.0, True]
express_list = [x for x in range(3)]        # [0, 1, 2]
```

<br/>

#### 访问和改变列表中的元素
与 [Tuple](#tuple-item-accessing) 和 [String](#string-slicing) 一样, 元素可以切片和使用索引访问。


**获取元素和切片**
```Python
>>> a_list = [0, 1, 2, 3, 4, 5]
>>> print(a_list[0])
0
>>> print(a_list[-3])
3
>>> print(a_list[1:4])
[1, 2, 3]
>>> print(a_list[::2])    # 第三个参数是步长
[0, 2, 4]
```

<br/>

**改变元素**: 对列表中对应的元素重新赋值。
```Python
>>> a_list = [0, 1, 2, 3]
>>> a_list[1] = 100
>>> print(a_list)
[0, 100, 2, 3]
```

<br/>

**添加元素**:
- `append(item)`, 将 item 添加至末尾.
- `insert(index, item)`, 将 item 插入至指定的位置 index.
```Python
>>> a_list = [0, 1, 2, 3]
>>> a_list.append(4)
>>> print(a_list)
[0, 1, 2, 3, 4]
>>> a_list.insert(0, -1)
>>> print(a_list)
[-1, 0, 1, 2, 3, 4]
```

<br/>

**移除元素**
- `remove(item)`, 移除一个指定的 item。
- `del list[index]`, 将 index 位置的元素删除。
- `pop(index=len(list)-1)`, 将指定位置的元素移除并返回这个元素 (默认是最后一个)。
- `clear()`, 清空这个列表。
```Python
>>> a_list = [0, 1, 2, 3]
>>> a_list.remove(2)
>>> print(a_list)
[0, 1, 3]
>>> a_list.pop()
>>> print(a_list)
[0, 1]
>>> del a_list[0]
>>> print(a_list)
[1]
>>> a_list.clear()
>>> print(a_list)
[]
```

<br/>

**元素位置交换**
```Python
>>> a_list = [0, 1, 2, 3]
>>> a_list[0], a_list[2] = a_list[2], a_list[0]
>>> print(a_list)
[2, 1, 0, 3]
```

<br/>

#### List Methods
一些内置的函数:

| 函数 | 简述 |
|:---:|:----|
| append(item) | 将 *item* 添加至末尾 |
| clear() | 清空列表 |
| copy() | 返回一个复制的列表 |
| count(item) | 然后 *item* 的个数 |
| extend(new_list) | 将整个列表 *new_list* 中的元素添加到末尾 |
| index(item) | 返回 *item* 所在的索引 |
| insert(index, item) | 插入 *item* 到指定位置 *index* |
| pop(index=len(list)-1) | 将指定位置的元素移除并返回这个元素 (默认是最后一个) |
| remove(item) | 移除指定元素 *item* |
| reverse() | 倒置列表 |
| sort(reverse=False, key=myFunc) | 排序列表 |

<br/>

### Set
集合是一组不包含重复元素的序列。

它会自动的移除重复的元素。

可以使用 `{}` 或 `set(iterable)` 创建集合. （空集只能使用 `set()` 创建, 而不是 `{}`）

```Python
>>> a_set = {'1', '2', '3', '4', '1', '2'}
>>> print(a_set)
{'1', '2', '3', '4'}
>>> a_set = set([1, 2, 3, 1])
>>> print(a_set)
{1, 2, 3}
```

<br/>

### Dictionary
字典是一个**无序合集**。

换句话说，元素使用**键值**来访问，而不是索引。

使用 `{}` 来创建字典, 其中为 `键值: 值` 的合集.

**Key 键值** 是字典中元素的标识. 它是唯一且不可变的.

使用相同的键值会覆盖和更新老的值。

```
>>> a_dict = {'name': "the_item", 'price': 9.95, 'stock': 10}       # 创建一个字典
>>> print(a_dict["name"])                 # 访问一个元素
the_item
>>> a_dict["desc"] = "just an item"     # 添加一个元素
>>> a_dict['price'] = 8.5               # 更新一个元素
>>> print(a_dict)
{'name': "the_item", 'price': 8.5, 'stock': 10, 'desc': "just an item"}
>>> print(a_dict.keys())                # 展示所有的键值
dict_keys(['name', 'price', 'stock', 'desc'])
>>> print(a_dict.values())              # 展示所有的值
dict_values(['the_item', 8.5, 10, "just an item"])
>>> dict_2 = {x: x+2 for x in range(3)} # 简便创建
>>> print(dict_2)
{0: 2, 1: 3, 2: 4}
```

<br/>

### 数据类型转换
转换 `x` 为其它类型:

| 函数 | 简述 |
|:---:|:----|
| int(x) | 转换 *x* 为整数 |
| float(x) | 转换 *x* 为浮点数 |
| complex(real, imag) | 创建一个复数 |
| str(x) | 转换 *x* 为字符串 |
| repr(x) | 转换 *x* 为可打印的字符串 |
| tuple(s) | 转换一个序列 (iterable) *s* 为元组 |
| list(s) | 转换一个序列 (iterable) *s* 为列表 |
| set(s) | 转换一个序列 (iterable) *s* 为集合 |
| dict(t) | 转换 `(key, value)` 元组 *t* 为字典 |
| frozenset(s) | 转换一个序列 (iterable) *s* 为不可变集合 |
| char(int) | 转换整数 *int* 为字符 |
| ord(char) | 转换字符 *char* 为整数 |
| hex(x) | 转换整数 *x* 为16进制 |
| oct(x) | 转换整数 *x* 为8进制 |



