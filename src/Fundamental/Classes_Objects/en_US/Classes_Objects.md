# Classes & Objects
![From 0 To Python](https://img.shields.io/badge/From%200%20To-Python-blue?style=for-the-badge&logo=Python&logoColor=FFD43B&logoWidth=15&labelColor=566163&color=3776AB) 

![Github link](https://img.shields.io/badge/FaDrYL--blue?style=social&logo=Github&logoWidth=15&link=https://github.com/FaDrYL)
![Website link](https://img.shields.io/badge/FaDr-YL-blue?style=flat&color=009f9f&link=https://www.fadryl.com/&link=https://www.fadryl.com/)

Python is an object-oriented language which everything is an object in Python.

You can make your own objects.



## Classes & Objects
Class is the skeleton of objects. It defines what the object is and how it looks like.

You can create some objects of one class. 

for example: 

Objects `Earth`, `Mars` are created from a class `Planet`.



### Create A Class
Using `class` keyword to create a class:

```Python
class OneClass:
    pass
```



Using built-in function `__init__()` to initialize an object and get some arguments from creation.

```Python
class OneClass:
    def __init__(self, x):
        pass
```



### Create An Object
To create an object, we just need to use the class name w/ or w/o arguments.

```Python
# Create a class without '__init__()'
class OneClass:
    pass


# Class with '__init__()'
class SecondClass:
    def __init__(self, x):
        pass


# Create a object of OneClass.
oneObject = OneClass()

# Create a object of SecondClass.
secondObject = SecondClass(10)      # ignore the 'self', and passing a value for 'x'.
```



### Variables In Class
Variables in class have two types:
- Class Variable
- Object Variable

You can directly access it by dot `.`.



#### Class Variable
Class variable is shared value within all objects of this class.

If change value of a class variable of an object, it will become object variable of this object

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

# change type for mars
mars.type = "Planet (Mars)"
print("Earth: " + earth.type)
print("Mars: " + mars.type)
```

output:

```
Planet
Planet
---
Earth: Planet
Mars: Planet (Mars)
```



#### Object Variable
The object variable is belong to the object itself.

Object variables are started with `self` (the first argument of a function) which is a reference to current instance of the class.

```Python
def Planet:
    def __init__(self, name):
        self.name = name


earth = Planet("Earth")
mars = Planet("Mars")
print(earth.name)
print(mars.name)
```

output:

```
Earth
Mars
```



### Functions In Class
Defined functions in the class allow objects of this class to use those functions.

To define functions, it is same as [before](../../Functions_Lambda/en_US/Functions_Lambda.md#creating-functions).

But, arguments of functions in class **must** start with `self`.

The first argument is a reference to the current instance (object) of this class which generally is `self`, you can change to other word you want.

At meanwhile, to call those functions we should ignore the argument `self`.



To access other functions in the class, you should call with `self.`.



```Python
class Planet:
    def __init__(self, name):
        self.name = name
        self.count = 0
    
    def increment_count(self):
        self.count += 1

    def get_name(self):
        self.increment_count()
        return "Name of this planet is: " + self.name


earth = Planet("Earth")
name_earth = earth.get_name()
print(name_earth)
```

output:

```
Name of this planet is: Earth
```



### Make Variables And Functions Private
Generally, variables and functions can be directly accessed by dot `.` from outside.

We can use double underscore `__` to make functions and variables private (hide them) which only can be accessed in this class.

for example: make `count` and `increment_count()` private:

```Python
class Planet:
    def __init__(self, name):
        self.name = name
        self.__count = 0

    def __increment_count():
        self.__count += 1

    def get_name():
        self.increment_count()
        return "This Planet is " + self.name
```



### Class Inheritance
A class can inherit from other class (parent class, base class).

This class will be a child class of the parent class.

To do that, add a parentheses `()` with name parent class, after the class name.

```Python
class child_class(parent_class):
```

for example: "Panda" is one of "Mammal", "Mammal" is a kind of "Animal".

```Python
class Animal:
    pass


class Mammal(Animal):
    pass


class Panda(Mammal):
    pass
```


#### Calling Function From Object.
Calling a function in an object will search the class of this object first. 

If is not be found (not be override in child class), It will find it in parents class.

```Python
class Animal:
    def get_animal_class(self):
        return "Animal" 
    
    def get_class_pos(self):
        return 0


class Mammal(Animal):
    # Override
    def get_class_pos(self):
        # found the function and return.
        return 1


class Panda(Mammal):
    # functions not found, go to parent class.
    pass


a_panda = Panda()
print(a_panda.get_animal_class())
print(a_panda.get_class_pos())
```

output:

```
Animal
1
```



##### Override A Function
To override a function, you just need to use a same function name and same arguments.

You can override a function to make the function more specifically for the child.

For example: "Penguin" is a "Bird". "Penguin" cannot fly.

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



### Using Classes From Other File
You need to `import` files or `from <fileName> import` classes to using them.

Separate above example to two files: *animal.py* and *penguin.py*

animal.py:

```Python
class Animal:
    pass


class Bird(Animal):
    def is_flyable(self):
        return True
```

penguin.py:

```Python
from animal import Bird     # -> From animal.py imports Bird class

class Penguin(Bird):
    # override parent's function.
    def is_flyable(self):
        # is not flyable
        return False
```



### Calling Parent Function In Child
To call parent function in the child, you can use `super().` with function name.

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
        # super().<function name>
        return super().get_animal_class() + " Panda"


a_panda = Panda()
print(a_panda.get_animal_class())
```

output:

```
Animal Panda
```



### Built-in Functions
To override those functions (most frequency to use) to get the result in different way.

Assume `obj` is the object name:

| Function name | Using it |
|:-------------:|:--------:|
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


