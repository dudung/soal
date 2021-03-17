---
layout: post
author: viridi
title: online compiler
mathjax: true
ptext: false
x3dom: false
threejs: false
oo: false
category: physics
tags: ["fi3201", "online", "compiler"]
date: 2021-01-22 17:32:00 +07
permalink: /fi3201/online-compiler
---
As a light introduction to Computational Physics course the use of some online compilers and interpreters [[1](#ref1)], in executing a "Hello, World!" program [[2](#ref2)], are presented here.


## hello, world!
Output of a "Hello, World!" program is simply
```
Hello, world!
```
which is typically in a console. Here are some examples in various languages.

### quite basic
```batch
100 PRINT "Hello, world!"
```
You can test it online [[3](#ref3)].

### pascal
```pascal
Program hello;
begin
    writeln('Hello, World!');
end.
```
You can test it online [[4](#ref4)].

### gnu fortran
```fortran
program hello
   print *, "Hello, World!"
end program Hello
```
You can test it online [[5](#ref5)].

### c++
```cpp
#include <iostream>
#include <string>

using namespace std;

int main()
{
    cout << "Hello, World!" << endl;
    return 0;
}
```
You can test it online [[6](#ref6)].

### bash
```bash
echo "Hello, World!"
```
You can test it online [[7](#ref7)].

### javascript
```javascript
console.log('Hello, world!');
```
You can test it online [[8](#ref8)].

### python
```python
print("Hello, World!")
```
You can test it online [[9](#ref9)].


## note
In other future articles, examples will not be written in all mentioned languages, e.g. Quite BASIC, Pascal, GNU Fortran, C++, Bash, JavaScript, or Python, but only in some of them.


## references
1. <a name="ref1"></a>admin, "Best Compilers/Interpreters to Practise Programming Online", FreeVideoLectures, 18 May 2017, url <https://freevideolectures.com/blog/best-compilersinterpreters-to-practise-programming-online/> [20210122].
2. <a name="ref2"></a>Wikipedia-Autoren, "Hallo-Welt-Programm", Wikipedia, Die freie Enzyklopädie, 29 November 2020, 14:37 UTC, <https://de.wikipedia.org/w/index.php?oldid=206056790> [20210122].
3. <a name="ref3"></a>Nikko Strom, "Quite BASICS -- fun, learning and nostalgia", 2011, url <http://www.quitebasic.com/> [20210122].
4. <a name="ref4"></a>-, "Online Pascal Compiler IDE", JDoodle, url <https://www.jdoodle.com/execute-pascal-online/>  [20210122].
5. <a name="ref5"></a>-, "Compile and Execute FORTRAN-95 Online (GNU Fortran, GCC v7.1.1)", Tutorials Point, url <https://www.tutorialspoint.com/compile_fortran_online.php> [20210122].
6. <a name="ref6"></a>-, "Online C++ compiler", C++ shell, url <http://cpp.sh/> [20210122].
7. <a name="ref7"></a>-, "Bash", Try It Online, url <https://tio.run/#bash> [20210122].
8. <a name="ref8"></a>-, "Node.js online editor, IDE, compiler, interpreter, and REPL", Repl.it, url <https://repl.it/languages/javascript> [20210122].
9. <a name="ref9"></a>-, "Python Online Compiler", Programize, url <https://www.programiz.com/python-programming/online-compiler/> [20210122].

+ [Article history](https://github.com/butiran/butiran.github.io/commits/master/_posts/fi3201/2021-01-22-online-compiler.md)

