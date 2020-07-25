# 安装 & 配置
[![Project link](https://img.shields.io/badge/From%200%20To-Python-blue?style=for-the-badge&logo=Python&logoColor=FFD43B&logoWidth=15&labelColor=566163&color=3776AB)](https://github.com/FaDrYL/From0ToPython) 

[![Github link](https://img.shields.io/badge/FaDrYL--blue?style=social&logo=Github&logoWidth=15&link=https://github.com/FaDrYL)](https://github.com/FaDrYL)
[![Website link](https://img.shields.io/badge/FaDr-YL-blue?style=flat&color=009f9f&link=https://www.fadryl.com/&link=https://www.fadryl.com/)](https://www.fadryl.com/)

<br/>

在本章，我们会安装 Python 和配置环境变量。

<br/>

## 安装
### 0. 检查是否已有 Python 及其版本
打开命令行，输入 `python -V`. 

如果已经有 Python 了， 它会显示版本号，比如：

```
> python -V
Python 3.8.2
```

如果显示的版本是 3.x （大版本为 3 和任意的小版本，如这个 3.8.2），你就可以跳过这章了。

反之，就继续往下看吧。

<br/>

### 1. 安装 Python
> Windows

打开链接: [https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/)

选择一个版本，下载其 **executable installer**。

(32 位的机器是 x86; 64 位的机器是 x86-64)

然后，双击安装即可。

**！ 不要忘记勾选 "Add Python to PATH"。**

<br/>

> Unix & Linux

1.下载及构建

打开链接: https://www.python.org/downloads/source/

选择一个版本，然后下载 **Gzipped source tarball**.

解压 *Python-3.x.x.tgz* (*3.x.x* 是版本号) 然后构建它：

```
$ tar -zxvf Python-3.8.3.tgz
$ cd Python-3.8.3
$ ./configure
$ make && make install
```

*或者*

2.使用包管理器

使用你的发行版的包管理器。例如安装 Python 3.8：

Ubuntu:

```
$ sudo apt-get update
$ sudo apt-get install 3.8
```

Fedora:

```
$ sudo dnf install python38
```

<br/>

> MAC OS X

打开链接: https://www.python.org/downloads/mac-osx/

选择一个版本，并下载 **macOS 64-bit installer**.

<br/>

### 2. 检查安装是否成功

安装完后，在命令行中输入 ``python -V``.

如果没有看到版本号，就继续往下看。

<br/>

## 配置
### 配置环境变量
> Windows

1.使用命令行 (如 cmd):

```
> path=%path%;Python安装的位置
```

将“Python安装的位置”替换为想对应的位置路径。


*或者*


2.手动配置

右键“我的电脑”，选择“属性”，

点击 “高级系统设置” -> “环境变量...”，

在“系统变量”下，找到 “Path” 并双击，

在“变量值”的最后加上 Python 的安装路径（用 **;** 来分隔新加的路径与之前的内容，如：`path1;path2;path3;Python路径`），

之后确认保存即可。

<br/>

> Unix & Linux

```
$ export PATH="$PATH:/usr/local/bin/python" 
```

"/usr/local/bin/python" 是 Python 安装的位置路径

