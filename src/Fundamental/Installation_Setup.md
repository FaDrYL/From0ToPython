# Installation & Setup

Install python and setup environment variable.



## Installation
### 0. To check if have python installed
Open terminal and enter ``python -V``. 
If has python installed, it will show the version. e.g.:

```
> python -V
Python 3.8.2

```
If the output like that and the version is 3.x, you can jump to the next chapter.
Otherwise, follow the instructions below.



### 1. Install python
> Windows

Open the link: https://www.python.org/downloads/windows/
Find a version, and download a **executable installer**.
(x86 for the 32-bit machine; x86-64 for the 64-bit machine)

Then, just double click to install it.
**! Don't forget to tick the "Add Python to PATH".**



> Unix & Linux

1.Download and build

Open the link: https://www.python.org/downloads/source/
Find a version, and download a **Gzipped source tarball**.
Decompress the package *Python-3.x.x.tgz* (*3.x.x* is the version) and build.

```
$ tar -zxvf Python-3.8.3.tgz
$ cd Python-3.8.3
$ ./configure
& make && make install
```
*OR*

2.Package manager

Using your distribution's package manager. e.g. install python 3.8:
Ubuntu:

```
$ sudo apt-get update
$ sudo apt-get install 3.8
```
Fedora:
```
$ sudo dnf install python38
```



> MAC OS X

Open the link: https://www.python.org/downloads/mac-osx/
Find a version, and download a **macOS 64-bit installer**.



### 2. Check installation

After that, check installation with ``python -V``.
If it is not working, follow the last step below.



## Setup
### Configure environment variable
> Windows

1.Using terminal (cmd):

```
> path=%path%;LocationOfPythonInstalled
```
"LocationOfPythonInstalled" is the location of python installed.

*OR*

2.Manually
Right click "This PC", select "Properties".
Click "Advanced system settings" -> "Environment Variables...".
Under the "System variables", find and double click "Path".
At end of "Variable value", add the path of python (Use **;** to separate with others. e.g. ``path1;path2;path3;pythonPath``).



> Unix & Linux
```
$ export PATH="$PATH:/usr/local/bin/python" 
```
"/usr/local/bin/python" is the location of python installed.

