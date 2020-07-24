# Operators
![https://img.shields.io/badge/From%200%20To-Python-blue?style=for-the-badge&logo=Python&logoColor=FFD43B&logoWidth=15&labelColor=566163&color=3776AB](https://img.shields.io/badge/From%200%20To-Python-blue?style=for-the-badge&logo=Python&logoColor=FFD43B&logoWidth=15&labelColor=566163&color=3776AB) 

![Github link](https://img.shields.io/badge/FaDrYL--blue?style=social&logo=Github&logoWidth=15&link=https://github.com/FaDrYL)
![Website link](https://img.shields.io/badge/FaDr-YL-blue?style=flat&color=009f9f&link=https://www.fadryl.com/&link=https://www.fadryl.com/)

<br/>

Python has some different type of operators:
- [Arithmetic Operators](#arithmetic-operators)
- [Assignment Operators](#assignment-operators)
- [Bitwise Operators](#bitwise-operators)
- [Comparison Operators](#comparison-operators)
- [Identity Operators](#identity-operators)
- [Logical Operators](#logical-operators)
- [Membership Operators](#membership-operators)

At meanwhile, [Operator Precedence](#operator-precedence) is important.

<br/>

## Arithmetic Operators
Assume `x = 10` and `y = 3`:

| Operator | Description | Example |
|:---------:|:-----------:|:-------:|
| `+` | Addition | `x + y` -> 13 |
| `-` | Subtraction | `x - y` -> 7 |
| `*` | Multiplication | `x * y` -> 30 |
| `/` | Division | `x / y` -> 3.333... |
| `%` | Modulus | `x % y` -> 1 |
| `//` | Integer division | `x // y` -> 3 |
| `**` | Exponentiation | `x ** y` -> 1000 |

<br/>

## Assignment Operators

| Operator | Example | Long Version |
|:--------:|:-------:|:------------:|
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
Bitwise operation will consider number as a binary.
```Python
    | number |    binary
 a  |   1    |   0000 0001
 b  |   7    |   0000 0111
```

| Operator | Description | Example |
|:--------:|:-----------:|:-------:|
| `&` | AND | `a & b` -> `1` (`0000 0001`) |
| <code>&#124;</code> | OR | <code>a &#124; b</code> -> `7` (`0000 0111`) |
| `^` | XOR | `a ^ b` -> `6` (`0000 0110`) |
| `~` | NOT (-x-1) | `~a` -> `-2` (`1111 1110`) |
| `<<` | Zero fill LEFT shift | `a << 2` -> `4` (`0000 0100`) |
| `>>` | Signed RIGHT shift | `b >> 1` -> `3` (`0000 0011`) |

<br/>

## Comparison Operators
Comparison operation will get boolean result of comparison.

Assume `a = 5` and `b = 8`:

| Operator | Description | Example |
|:--------:|:-----------:|:-------:|
| `==` | Equal | `a == b` -> `False` |
| `!=` | Not equal | `a != b` -> `True` |
| `>` | Greater than | `a > b` -> `False` |
| `<` | Less than | `a < b` -> `True` |
| `>=` | Greater than or Equal to | `a >= b` -> `False` |
| `<=` | Less than or Equal to | `a <= b` -> `True` |
 
<br/>
 
## Identity Operators
Identity operators are used to compare the objects and their memory location.

| Operator | Description | Example |
|:--------:|:-----------:|:-------:|
| `is` | Return `True`, if both of them are same object | `a is b` |
| `is not` | Return `True`, if they are not same object | `a is not b` |

<br/>

## Logical Operators
Logical Operators are used to combine conditional statements.

Assume `a = 2`:

| Operator | Description | Example |
|:--------:|:-----------:|:-------:|
| `and` | AND, return `True` if they both are true | `(a > 0) and (a < 3)` -> `True` |
| `or` | OR, return `True` if at least one of them is true | `(a < 0) or (a > 3)` -> `False` |
| `not` | NEGATION, return `True` if it is false | `not (a > 0)` -> `False`|

<br/>

## Membership Operators
Membership Operators are used to check if a specified item in a sequence (List, String, Set, Tuple, Dictionary ...).

| Operator | Description | Example |
|:--------:|:-----------:|:-------:|
| `in` | `True` if the item can be found | `"o" in "a book"` -> `True` |
| `not in` | `True` if the item cannot be found | `1 not in [2, 3, 4]` -> `True` |

<br/>

## Operator Precedence
Operators have different precedence.

like `×÷+-` in math.

The table shows the precedence from high to low priority.

| Operator |
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

[Find more](https://docs.python.org/3/reference/expressions.html#operator-precedence)

