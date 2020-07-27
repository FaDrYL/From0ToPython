# 运算符
![https://img.shields.io/badge/From%200%20To-Python-blue?style=for-the-badge&logo=Python&logoColor=FFD43B&logoWidth=15&labelColor=566163&color=3776AB](https://img.shields.io/badge/From%200%20To-Python-blue?style=for-the-badge&logo=Python&logoColor=FFD43B&logoWidth=15&labelColor=566163&color=3776AB) 

![Github link](https://img.shields.io/badge/FaDrYL--blue?style=social&logo=Github&logoWidth=15&link=https://github.com/FaDrYL)
![Website link](https://img.shields.io/badge/FaDr-YL-blue?style=flat&color=009f9f&link=https://www.fadryl.com/&link=https://www.fadryl.com/)

<br/>

[[代码示例]](Operators_sample.py)

<br/>

Python 有这些类型的运算符：
- [算术运算符](#arithmetic-operators)
- [赋值运算符](#assignment-operators)
- [位运算符](#bitwise-operators)
- [比较运算符](#comparison-operators)
- [身份运算符](#identity-operators)
- [逻辑运算符](#logical-operators)
- [成员运算符](#membership-operators)

同时, [运算符优先级](#operator-precedence) 也很重要.

<br/>

## Arithmetic Operators
**算术运算符**

假设 `x = 10` 和 `y = 3`:

| 运算符 | 简述 | 例子 |
|:-----:|:---:|:---:|
| `+` | 加 | `x + y` -> 13 |
| `-` | 减 | `x - y` -> 7 |
| `*` | 乘 | `x * y` -> 30 |
| `/` | 除 | `x / y` -> 3.333... |
| `%` | 取模 | `x % y` -> 1 |
| `//` | 整除 | `x // y` -> 3 |
| `**` | 指数 | `x ** y` -> 1000 |

<br/>

## Assignment Operators
**赋值运算符**

| 运算符 | 例子 | 长版本 |
|:-----:|:---:|:-----:|
| `=` | `x = 1` | `x = 1` |
| `+=` | `x += 2`| `x = x + 2` |
| `-=` | `x -= 3` | `x = x - 3` |
| `*=` | `x *= 4` | `x = x * 4` |
| `/=` | `x /= 5` | `x = x / 5` |
| `%=` | `x %= 6` | `x = x % 6` |
| `//=` | `x //= 7` | `x = x // 7` |
| `**=` | `x **= 8` | `x = x ** 8` |
| `&=` | `x &= 1` | `x = x & 1` |
| <code>&#124;=</code> | <code>x &#124;= 2</code> | <code>x = x &#124; 2</code>|
| `^=` | `x ^= 3` | `x = x ^ 3` |
| `>>=` | `x >>= 4` | `x = x >> 4` |
| `<<=` | `x <<= 5` | `x = x << 5` |
| `:=` (Python3.8+) | `x := 2` | `x = 2` and return x |

<br/>

## Bitwise Operators
**位运算符**

位运算符会将数字看作为二进制。
```Python
    |   数字   |    二进制
 a  |    1    |   0000 0001
 b  |    7    |   0000 0111
```

| 运算符 | 简述 | 例子 |
|:-----:|:---:|:---:|
| `&` | 与 | `a & b` -> `1` (`0000 0001`) |
| <code>&#124;</code> | 或 | <code>a &#124; b</code> -> `7` (`0000 0111`) |
| `^` | 异或 | `a ^ b` -> `6` (`0000 0110`) |
| `~` | 非 (-x-1) | `~a` -> `-2` (`1111 1110`) |
| `<<` | 左移 | `a << 2` -> `4` (`0000 0100`) |
| `>>` | 右移 | `b >> 1` -> `3` (`0000 0011`) |

<br/>

## Comparison Operators
**比较运算符**

比较运算符会在比较后返回一个布尔值（`True`、`False`）

假设 `a = 5` 和 `b = 8`:

| 运算符 | 简述 | 例子 |
|:--------:|:-----------:|:-------:|
| `==` | 等于 | `a == b` -> `False` |
| `!=` | 不等于 | `a != b` -> `True` |
| `>` | 大于 | `a > b` -> `False` |
| `<` | 小于 | `a < b` -> `True` |
| `>=` | 大于或等于 | `a >= b` -> `False` |
| `<=` | 小于或等于 | `a <= b` -> `True` |
 
<br/>
 
## Identity Operators
**身份运算符**

身份运算符通常用于比较两个对象和它们在内存中的位置是否相同。（是否是同一个对象）

返回一个布尔值（`True`、`False`）。

| 运算符 | 简述 | 例子 |
|:--------:|:-----------:|:-------:|
| `is` | 是同一个对象 | `a is b` |
| `is not` | 不是同一个对象 | `a is not b` |

<br/>

## Logical Operators
**逻辑运算符**

逻辑运算符用于将条件语句结合。

假设 `a = 2`:

| 运算符 | 简述 | 例子 |
|:--------:|:-----------:|:-------:|
| `and` | 与， 如果两边都是 `True` ，则返回 `True` | `(a > 0) and (a < 3)` -> `True` |
| `or` | 或，如果两边至少有一个是 `True`，则返回 `True` | `(a < 0) or (a > 3)` -> `False` |
| `not` | 非，如果是 `True`，就返回 `False`，反之亦然 | `not (a > 0)` -> `False`|

<br/>

## Membership Operators
**成员运算符**

成员运算符用于查看一个特定的元素是否存在在一个序列（列表，字符串，集合，元组，字典 ...）中。

| 运算符 | 简述 | 例子 |
|:--------:|:-----------:|:-------:|
| `in` | `True`， 如果存在 | `"o" in "a book"` -> `True` |
| `not in` | `True`，如果不存在 | `1 not in [2, 3, 4]` -> `True` |

<br/>

## Operator Precedence
**运算符优先级**

运算符们都有不同的优先级

就像数学中的 `×÷+-`。

下面的列表，展示了从高到低的优先级：

| 运算符 |
|:--------:|
| `**` |
| `~` |
| `*` `/` `%` `//` |
| `+` `-` |
| `>>` `<<` |
| `&` |
| `^` |
| <code>&#124;</code> |
| `in` `not in` `is` `is not` `<` `<=` `>` `>=` `!=` `==` |
| `not` |
| `and` |
| `or` |

[了解更多](https://docs.python.org/3/reference/expressions.html#operator-precedence)

