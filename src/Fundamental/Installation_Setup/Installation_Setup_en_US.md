# Installation & Setup
[![Project link](https://img.shields.io/badge/From%200%20To-Python-blue?style=for-the-badge&logo=Python&logoColor=FFD43B&logoWidth=15&labelColor=566163&color=3776AB)](https://github.com/FaDrYL/From0ToPython) 

[![Github link](https://img.shields.io/badge/FaDrYL--blue?style=social&logo=Github&logoWidth=15&link=https://github.com/FaDrYL)](https://github.com/FaDrYL)
[![Website link](https://img.shields.io/badge/FaDr-YL-blue?style=flat&color=009f9f&link=https://www.fadryl.com/&link=https://www.fadryl.com/)](https://www.fadryl.com/)

<br/>

Install Python and setup environment variable.

<br/>

## Installation
### 0. To check if have Python installed
Open terminal and enter `python -V`. 

If has Python installed, it will show the version. e.g.:

```
> python -V
Python 3.8.2
```

If the output like that (`Python 3.8.2`) and the version is 3.x, you can jump to the next chapter.

Otherwise, follow the instructions below.

<br/>

### 1. Install Python
> Windows

Open the link: https://www.python.org/downloads/windows/

Find a version, and download a **executable installer**.

(x86 for the 32-bit machine; x86-64 for the 64-bit machine)

Then, just double-click to install it.

**! Don't forget to tick the "Add Python to PATH".**

<br/>

> Unix & Linux

1.Download and build

Open the link: https://www.python.org/downloads/source/

Find a version, and download a **Gzipped source tarball**.

Decompress the package *Python-3.x.x.tgz* (*3.x.x* is the version) and build.

```
$ tar -zxvf Python-3.8.3.tgz
$ cd Python-3.8.3
$ ./configure
$ make && make install
```

*OR*

2.Package manager

Using your distribution's package manager. e.g. install Python 3.8:

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

Open the link: https://www.python.org/downloads/mac-osx/

Find a version, and download a **macOS 64-bit installer**.

<br/>

### 2. Check installation

After that, check installation with ``python -V``.

If it is not working, follow the last step below.

<br/>

## Setup
### Configure environment variable
> Windows

1.Using terminal (cmd):

```
> path=%path%;LocationOfPythonInstalled
```

"LocationOfPythonInstalled" is the location of Python installed.


*OR*


2.Manually

Right click "This PC", select "Properties".

Click "Advanced system settings" -> "Environment Variables...".

Under the "System variables", find and double-click "Path".

At end of "Variable value", add the path of Python (Use **;** to separate with others. e.g. ``path1;path2;path3;pythonPath``).

<br/>

> Unix & Linux

```
$ export PATH="$PATH:/usr/local/bin/python" 
```

"/usr/local/bin/python" is the location of Python installed.

