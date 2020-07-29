# 类 & 对象
[![Project link](https://img.shields.io/badge/From%200%20To-Python-blue?style=for-the-badge&logo=Python&logoColor=FFD43B&logoWidth=15&labelColor=566163&color=3776AB)](https://github.com/FaDrYL/From0ToPython) 

[![Github link](https://img.shields.io/badge/FaDrYL--blue?style=social&logo=Github&logoWidth=15)](https://github.com/FaDrYL)
[![Website link](https://img.shields.io/badge/FaDr-YL-blue?style=flat&color=009f9f)](https://www.fadryl.com/)

<br/>

Python 是个面向对象的语言，在 Python 里所有的数据类型都是对象。

你可以根据情况写个全新的类，然后创建对象。

[[代码示例]](Classes_Objects_sample.py)

<br/>

## 类与对象
**类** 是对象的骨架（框架），它负责定义这个对象以及它的外观。

你可以从一个类创建多个不同的对象（实例）。

举个例子: 

对象 `Earth`, `Mars` 都可以使用 `Planet` 类创建（各自有不同的参数）。

<br/>

### 创建一个类
使用关键字 `class` 来创建一个类：

```Python
class OneClass:
    pass
```

<br/>

使用内置函数 `__init__()` 来初始化一个对象，以及得到一些必要的参数。

```Python
class OneClass:
    def __init__(self, x):
        pass
```

<br/>

### 创建一个对象
我们只需要使用类的名字以及初始化所需要的参数，即可创建一个对象。

```Python
# 创建一个没有 __init__() 的类
class OneClass:
    pass


# 有 '__init__()' 的类
class SecondClass:
    def __init__(self, x):
        pass


# 创建一个 OneClass 的对象。
oneObject = OneClass()

# 创建一个 SecondClass 的对象。
secondObject = SecondClass(10)      # 忽略第一个参数 'self', 然后传递一个 'x'.
```

<br/>

### 类中的变量
类中的变量有两种类型：
- 类变量
- 对象变量（实例变量）

你可以直接使用点 `.` 来访问它们。

<br/>

#### 类变量
类变量会与当前类的所有对象共享。

如果改变了它的值，它会变成这个对象的对象变量。

```Python
class Planet:
    type = "Planet"
    
    def __init__(self):
        pass


earth = Planet()
mars = Planet()

print(earth.type)
print(mars.type)

print("---")

# 改变 mars 的 type
mars.type = "Planet (Mars)"
print("Earth: " + earth.type)
print("Mars: " + mars.type)
```

输出:

```
Planet
Planet
---
Earth: Planet
Mars: Planet (Mars)
```

<br/>

#### 对象变量
对象变量只属于当前对象。

对象变量以 `self`（这个函数的第一个参数） 开头。

```Python
class Planet:
    def __init__(self, name):
        self.name = name


earth = Planet("Earth")
mars = Planet("Mars")
print(earth.name)
print(mars.name)
```

输出:

```
Earth
Mars
```

<br/>

### 类中的函数
在类中定义函数，其允许这个类的所有对象使用它。

定义函数的方法与[之前](../Functions_Lambda/Functions_Lambda_en_US.md#creating-functions)（章节：类 & Lambda）相同。

但是，函数的参数**必须有**且**第一个**必须是 `self`（或随意名字，规范为 `self`）。

第一个参数是对该类当前对象（实例）的引用，通常是 `self`，您可以更改为任意的其它名字。

同时，在使用这个函数的时候应该忽略第一个参数 `self`。

<br/>

在类中使用当前类里的函数应该以 `self.` 开头来使用它。

<br/>

```Python
class Planet:
    def __init__(self, name):
        self.name = name
        self.count = 0
    
    def increment_count(self):
        self.count += 1

    def get_name(self):
        # 类中使用
        self.increment_count()
        return "Name of this planet is: " + self.name


earth = Planet("Earth")
# 类外使用
name_earth = earth.get_name()
print(name_earth)
```

输出:

```
Name of this planet is: Earth
```

<br/>

### 让变量与函数私有化
一般来说，变量和函数可以**直接**使用点 `.` 来从外部访问。

我们能在函数或变量名前加两个下划线 `__` 来使其私有、对外部隐藏它们（不能从外部“直接”访问）。

例如：使 `count` 和 `increment_count()` 私有化：

```Python
class Planet:
    def __init__(self, name):
        self.name = name
        self.__count = 0

    def __increment_count(self):
        self.__count += 1

    def get_name(self):
        self.increment_count()
        return "This Planet is " + self.name
```

<br/>

### 类的继承
一个类可以继承自其它的类（其 父类、基类）。

这个类就成为了其父类的一个子类。

去达成它，我们只需要在当前类名的后面加上括号 `()` 以及父类的名字。
语法：

```Python
class child_class(parent_class):
```

例如：以下的例子，"Panda" 是 "Mammal" 中的一种，"Mammal" 属于 "Animal"。

```Python
class Animal:
    pass


class Mammal(Animal):
    pass


class Panda(Mammal):
    pass
```

<br/>

#### 使用对象中的函数
当使用一个对象中的函数时，会先寻找当前的类。

如果当前类没有这个函数（没有被重载），它就会去父类进行寻找。

```Python
class Animal:
    def get_animal_class(self):
        return "Animal" 
    
    def get_class_pos(self):
        return 0


class Mammal(Animal):
    # 重载
    def get_class_pos(self):
        # 找到了对应的函数，运行并返回。
        return 1


class Panda(Mammal):
    # 没有找到函数，去父类寻找
    pass


a_panda = Panda()
print(a_panda.get_animal_class())
print(a_panda.get_class_pos())
```

输出:

```
Animal
1
```

<br/>

##### 函数重载
重载一个函数，我们只需在当前类定义一个函数，并使用相同于父类函数的函数名和相同的参数。

你可以使用重载，来使这个函数更加符合当前类的情境。

例如："Penguin" 是个 "Bird"，但是 "Penguin" 不会飞。

```Python
class Animal:
    pass


class Bird(Animal):
    def is_flyable(self):
        return True


class Penguin(Bird):
    # override parent's function.
    def is_flyable(self):
        # is not flyable
        return False
```

<br/>

### 使用其它py文件中的类
你需要导入 `import <文件名>` 或 `from <文件名> import <类>` 来使用它们。

将上面的类分为两个文件：*animal.py* 和 *penguin.py*。

animal.py:

```Python
class Animal:
    pass


class Bird(Animal):
    def is_flyable(self):
        # 鸟类会飞
        return True
```

penguin.py:

```Python
from animal import Bird     # -> 从 animal.py 导入 Bird 类

class Penguin(Bird):
    # 重载父类的方法
    def is_flyable(self):
        # 企鹅不会飞
        return False
```

<br/>

### 重载后使用父类的函数
在子类中使用父类的同一个函数，我们只需在函数名前加 `super().`。

```Python
class Animal:
    def get_animal_class(self):
        return "Animal" 
    
    def get_class_pos(self):
        return 0


class Mammal(Animal):
    def get_class_pos(self):
        return 1


class Panda(Mammal):
    def get_animal_class(self):
        # super().<函数名>
        return super().get_animal_class() + " Panda"


a_panda = Panda()
print(a_panda.get_animal_class())
```

输出:

```
Animal Panda
```

<br/>

### 特殊的内置函数
重载这些（常用的）函数来以不同的方式实现它们。

假设 `obj` 是这个对象的名字:

| 函数名 | 使用 |
|:-----:|:---:|
| `__len__(self)` | `len(obj)` |
| `__str__(self)` | `str(obj)` |
| `__int__(self)` | `int(obj)` |
| `__repr__(self)` | `repr(obj)` |
| `__eq__(self, other)` | `obj == other` |
| `__ne__(self, other)` | `obj != other` |
| `__gt__(self, other)` | `obj > other` |
| `__ge__(self, other)` | `obj >= other` |
| `__lt__(self, other)` | `obj < other` |
| `__le__(self, other)` | `obj <= other` |
| `__add__(self, other)` | `obj + other` |
| `__sub__(self, other)` | `obj - other` |
| `__mul__(self, other)` | `obj * other` |
| `__div__(self, other)` | `obj / other` |
| `__floordiv__(self, other)` | `obj // other` |
| `__mod__(self, other)` | `obj % other` |
| `__lshift__(self, other)` | `obj << other` |
| `__rshift__(self, other)` | `obj >> other` |
| `__and__(self, other)` | `obj & other` |
| `__or__(self, other)` | <code>obj &#124; other</code> |
| `__xor__(self, other)` | `obj ^ other` |
| `__abs__(self)` | `abs(self)` |
| `__contains__(self, item)` | `item in obj` |
| `__getitem__(self, key)` | `obj[key]` |
| `__setitem__(self, key, value)` | `obj[key] = value` |


