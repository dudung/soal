---
layout: post
author: viridi
title: install python notebook
mathjax: true
ptext: false
x3dom: false
threejs: false
oo: false
category: code
tags: ["python", "install", "notebook", ""]
date: 2021-02-04 05:55:00 +07
permalink: /code/py/install-python-notebook
---
Unsuccessfull installation of Python package, including notebook, through pip [[1](#ref1)] in Cygwin version 2.873 [[2](#ref2)] on Windows 10 Home the day before yesterday forces me to install Python 3.9.1 [[3](#ref3)].

## log
```
[20210202]
1927 Try https://www.python.org/downloads/windows/
1928 https://www.python.org/downloads/release/python-391/
1929 Downloading. https://www.python.org/ftp/python/3.9.1/python-3.9.1-amd64.exe
1937 Finish download. Copy to I:\Python folder.
1938 Installing Python 3.9.1 Test Suite (54 bit) and others.
1941 Finish install.
1943 Call cmd.exe and py ok.
2004 Read https://stackoverflow.com/a/46086745 and https://stackoverflow.com/a/6832544 for next steps.
2010 Read https://pypi.org/project/opencv-python/ and choose Option 1, not yet performed.
2014 Try python -m pip install --upgrade pip
201X OpenCV fails
2018 Try again and then it works.
```

## installation
1. Download the `python-3.9.1-amd64.exe` file, save it to your Python installer folder, click it, and follow the instruction.
2. After installation and get such messages
```
WARNING: The scripts *.exe, *.exe and *.exe are installed in 'C:\Users\[User Name]\AppData\Local\Programs\Python\Python39\Scripts' which is not on PATH.
Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
```
modify the path according to [[4](#ref4)].
```
L:\home\butiran.github.io\src\py>set path=%path%;"C:\Users\[User Name]\AppData\Local\Programs\Python\Python39"
```
Change `[User Name]` wity your Windows user name, e.g `Albert Einstein` if you are Albert Einstein [[5](#ref5)].
3. In order to install `notebook` I follow the steps sugggested related to the use Cywin [[6](#ref6)], but it works for me.
```
python -m pip install scipy
python -m pip install scikit-learn
python -m pip install sklearn
python -m pip install pandas
python -m pip install matplotlib
python -m pip install jupyter
```
And when there are some errors, repeat the step and it works.
4. Add `OpenCV` [[7](#ref5)] using the same way.
```
python -m pip install jupyter
```


## console output
The lines in the console are
```
L:\home\butiran.github.io\src\py>python -m pip install scipy
Collecting scipy
  Downloading scipy-1.6.0-cp39-cp39-win_amd64.whl (32.7 MB)
     |████████████████████████████████| 32.7 MB 42 kB/s
Requirement already satisfied: numpy>=1.16.5 in c:\users\[user name]\appdata\local\programs\python\python39\lib\site-packages (from scipy) (1.20.0)
Installing collected packages: scipy
Successfully installed scipy-1.6.0

L:\home\butiran.github.io\src\py>python -m pip install scikit-learn
Collecting scikit-learn
  Downloading scikit_learn-0.24.1-cp39-cp39-win_amd64.whl (6.9 MB)
     |████████████████████████████████| 6.9 MB 171 kB/s
Requirement already satisfied: numpy>=1.13.3 in c:\users\[user name]\appdata\local\programs\python\python39\lib\site-packages (from scikit-learn) (1.20.0)
Requirement already satisfied: scipy>=0.19.1 in c:\users\[user name]\appdata\local\programs\python\python39\lib\site-packages (from scikit-learn) (1.6.0)
Collecting joblib>=0.11
  Downloading joblib-1.0.0-py3-none-any.whl (302 kB)
     |████████████████████████████████| 302 kB 384 kB/s
Collecting threadpoolctl>=2.0.0
  Downloading threadpoolctl-2.1.0-py3-none-any.whl (12 kB)
Installing collected packages: threadpoolctl, joblib, scikit-learn
Successfully installed joblib-1.0.0 scikit-learn-0.24.1 threadpoolctl-2.1.0

L:\home\butiran.github.io\src\py>python -m pip install sklearn
Collecting sklearn
  Downloading sklearn-0.0.tar.gz (1.1 kB)
Requirement already satisfied: scikit-learn in c:\users\[user name]\appdata\local\programs\python\python39\lib\site-packages (from sklearn) (0.24.1)
Requirement already satisfied: numpy>=1.13.3 in c:\users\[user name]\appdata\local\programs\python\python39\lib\site-packages (from scikit-learn->sklearn) (1.20.0)
Requirement already satisfied: threadpoolctl>=2.0.0 in c:\users\[user name]\appdata\local\programs\python\python39\lib\site-packages (from scikit-learn->sklearn) (2.1.0)
Requirement already satisfied: scipy>=0.19.1 in c:\users\[user name]\appdata\local\programs\python\python39\lib\site-packages (from scikit-learn->sklearn) (1.6.0)
Requirement already satisfied: joblib>=0.11 in c:\users\[user name]\appdata\local\programs\python\python39\lib\site-packages (from scikit-learn->sklearn) (1.0.0)
Using legacy 'setup.py install' for sklearn, since package 'wheel' is not installed.
Installing collected packages: sklearn
    Running setup.py install for sklearn ... done
Successfully installed sklearn-0.0

L:\home\butiran.github.io\src\py>python -m pip install pandas
Collecting pandas
  Downloading pandas-1.2.1-cp39-cp39-win_amd64.whl (9.3 MB)
     |████████████████████████████████| 9.3 MB 386 kB/s
Collecting python-dateutil>=2.7.3
  Downloading python_dateutil-2.8.1-py2.py3-none-any.whl (227 kB)
     |████████████████████████████████| 227 kB 148 kB/s
Collecting pytz>=2017.3
  Downloading pytz-2021.1-py2.py3-none-any.whl (510 kB)
     |████████████████████████████████| 510 kB 226 kB/s
Requirement already satisfied: numpy>=1.16.5 in c:\users\[user name]\appdata\local\programs\python\python39\lib\site-packages (from pandas) (1.20.0)
Collecting six>=1.5
  Downloading six-1.15.0-py2.py3-none-any.whl (10 kB)
Installing collected packages: six, pytz, python-dateutil, pandas
Successfully installed pandas-1.2.1 python-dateutil-2.8.1 pytz-2021.1 six-1.15.0

L:\home\butiran.github.io\src\py>python -m pip install matplotlib
Collecting matplotlib
  Downloading matplotlib-3.3.4-cp39-cp39-win_amd64.whl (8.5 MB)
     |████████████████████████████████| 8.5 MB 467 kB/s
Collecting kiwisolver>=1.0.1
  Downloading kiwisolver-1.3.1-cp39-cp39-win_amd64.whl (51 kB)
     |████████████████████████████████| 51 kB 46 kB/s
Requirement already satisfied: numpy>=1.15 in c:\users\[user name]\appdata\local\programs\python\python39\lib\site-packages (from matplotlib) (1.20.0)
Collecting cycler>=0.10
  Downloading cycler-0.10.0-py2.py3-none-any.whl (6.5 kB)
Requirement already satisfied: python-dateutil>=2.1 in c:\users\[user name]\appdata\local\programs\python\python39\lib\site-packages (from matplotlib) (2.8.1)
Collecting pillow>=6.2.0
  Downloading Pillow-8.1.0-cp39-cp39-win_amd64.whl (2.2 MB)
     |████████████████████████████████| 2.2 MB 328 kB/s
Collecting pyparsing!=2.0.4,!=2.1.2,!=2.1.6,>=2.0.3
  Downloading pyparsing-2.4.7-py2.py3-none-any.whl (67 kB)
     |████████████████████████████████| 67 kB 206 kB/s
Requirement already satisfied: six in c:\users\[user name]\appdata\local\programs\python\python39\lib\site-packages (from cycler>=0.10->matplotlib) (1.15.0)
Installing collected packages: pyparsing, pillow, kiwisolver, cycler, matplotlib
Successfully installed cycler-0.10.0 kiwisolver-1.3.1 matplotlib-3.3.4 pillow-8.1.0 pyparsing-2.4.7

L:\home\butiran.github.io\src\py>python -m pip install jupyter
Collecting jupyter
  Downloading jupyter-1.0.0-py2.py3-none-any.whl (2.7 kB)
Collecting qtconsole
  Downloading qtconsole-5.0.2-py3-none-any.whl (119 kB)
     |████████████████████████████████| 119 kB 504 kB/s
Collecting nbconvert
  Downloading nbconvert-6.0.7-py3-none-any.whl (552 kB)
     |████████████████████████████████| 552 kB 363 kB/s
Collecting ipywidgets
  Downloading ipywidgets-7.6.3-py2.py3-none-any.whl (121 kB)
     |████████████████████████████████| 121 kB 386 kB/s
Collecting ipykernel
  Downloading ipykernel-5.4.3-py3-none-any.whl (120 kB)
     |████████████████████████████████| 120 kB 252 kB/s
Collecting notebook
  Downloading notebook-6.2.0-py3-none-any.whl (9.5 MB)
     |████████████████████████████████| 9.5 MB 252 kB/s
Collecting jupyter-console
  Downloading jupyter_console-6.2.0-py3-none-any.whl (22 kB)
Collecting jupyter-client
  Downloading jupyter_client-6.1.11-py3-none-any.whl (108 kB)
     |████████████████████████████████| 108 kB 469 kB/s
Collecting traitlets>=4.1.0
  Downloading traitlets-5.0.5-py3-none-any.whl (100 kB)
     |████████████████████████████████| 100 kB 319 kB/s
Collecting tornado>=4.2
  Downloading tornado-6.1-cp39-cp39-win_amd64.whl (422 kB)
     |████████████████████████████████| 422 kB 409 kB/s
Collecting ipython>=5.0.0
  Downloading ipython-7.20.0-py3-none-any.whl (784 kB)
     |████████████████████████████████| 784 kB 598 kB/s
Collecting colorama
  Downloading colorama-0.4.4-py2.py3-none-any.whl (16 kB)
Collecting backcall
  Downloading backcall-0.2.0-py2.py3-none-any.whl (11 kB)
Requirement already satisfied: setuptools>=18.5 in c:\users\[user name]\appdata\local\programs\python\python39\lib\site-packages (from ipython>=5.0.0->ipykernel->jupyter) (49.2.1)
Collecting pickleshare
  Downloading pickleshare-0.7.5-py2.py3-none-any.whl (6.9 kB)
Collecting decorator
  Downloading decorator-4.4.2-py2.py3-none-any.whl (9.2 kB)
Collecting prompt-toolkit!=3.0.0,!=3.0.1,<3.1.0,>=2.0.0
  Downloading prompt_toolkit-3.0.14-py3-none-any.whl (359 kB)
     |████████████████████████████████| 359 kB 327 kB/s
Collecting pygments
  Downloading Pygments-2.7.4-py3-none-any.whl (950 kB)
     |████████████████████████████████| 950 kB 656 kB/s
Collecting jedi>=0.16
  Downloading jedi-0.18.0-py2.py3-none-any.whl (1.4 MB)
     |████████████████████████████████| 1.4 MB 467 kB/s
Collecting parso<0.9.0,>=0.8.0
  Downloading parso-0.8.1-py2.py3-none-any.whl (93 kB)
     |████████████████████████████████| 93 kB 125 kB/s
Collecting wcwidth
  Downloading wcwidth-0.2.5-py2.py3-none-any.whl (30 kB)
Collecting ipython-genutils
  Downloading ipython_genutils-0.2.0-py2.py3-none-any.whl (26 kB)
Collecting widgetsnbextension~=3.5.0
  Downloading widgetsnbextension-3.5.1-py2.py3-none-any.whl (2.2 MB)
     |████████████████████████████████| 2.2 MB 252 kB/s
Collecting nbformat>=4.2.0
  Downloading nbformat-5.1.2-py3-none-any.whl (113 kB)
     |████████████████████████████████| 113 kB 327 kB/s
Collecting jupyterlab-widgets>=1.0.0
  Downloading jupyterlab_widgets-1.0.0-py3-none-any.whl (243 kB)
     |████████████████████████████████| 243 kB 435 kB/s
Collecting jupyter-core
  Downloading jupyter_core-4.7.1-py3-none-any.whl (82 kB)
     |████████████████████████████████| 82 kB 39 kB/s
Collecting jsonschema!=2.5.0,>=2.4
  Downloading jsonschema-3.2.0-py2.py3-none-any.whl (56 kB)
     |████████████████████████████████| 56 kB 230 kB/s
Requirement already satisfied: six>=1.11.0 in c:\users\[user name]\appdata\local\programs\python\python39\lib\site-packages (from jsonschema!=2.5.0,>=2.4->nbformat>=4.2.0->ipywidgets->jupyter) (1.15.0)
Collecting attrs>=17.4.0
  Downloading attrs-20.3.0-py2.py3-none-any.whl (49 kB)
     |████████████████████████████████| 49 kB 106 kB/s
Collecting pyrsistent>=0.14.0
  Downloading pyrsistent-0.17.3.tar.gz (106 kB)
     |████████████████████████████████| 106 kB 242 kB/s
Collecting prometheus-client
  Downloading prometheus_client-0.9.0-py2.py3-none-any.whl (53 kB)
     |████████████████████████████████| 53 kB 128 kB/s
Collecting terminado>=0.8.3
  Downloading terminado-0.9.2-py3-none-any.whl (14 kB)
Collecting pyzmq>=17
  Downloading pyzmq-22.0.2-cp39-cp39-win_amd64.whl (1.2 MB)
     |████████████████████████████████| 1.2 MB 1.3 MB/s
Collecting jinja2
  Downloading Jinja2-2.11.3-py2.py3-none-any.whl (125 kB)
     |████████████████████████████████| 125 kB 204 kB/s
Collecting Send2Trash>=1.5.0
  Downloading Send2Trash-1.5.0-py3-none-any.whl (12 kB)
Collecting argon2-cffi
  Downloading argon2_cffi-20.1.0-cp39-cp39-win_amd64.whl (42 kB)
     |████████████████████████████████| 42 kB 65 kB/s
Requirement already satisfied: python-dateutil>=2.1 in c:\users\[user name]\appdata\local\programs\python\python39\lib\site-packages (from jupyter-client->ipykernel->jupyter) (2.8.1)
Collecting pywin32>=1.0
  Downloading pywin32-300-cp39-cp39-win_amd64.whl (9.2 MB)
     |████████████████████████████████| 9.2 MB 504 kB/s
Collecting pywinpty>=0.5
  Downloading pywinpty-0.5.7.tar.gz (49 kB)
     |████████████████████████████████| 49 kB 226 kB/s
Collecting cffi>=1.0.0
  Downloading cffi-1.14.4-cp39-cp39-win_amd64.whl (179 kB)
     |████████████████████████████████| 179 kB 327 kB/s
Collecting pycparser
  Downloading pycparser-2.20-py2.py3-none-any.whl (112 kB)
     |████████████████████████████████| 112 kB 297 kB/s
Collecting MarkupSafe>=0.23
  Downloading MarkupSafe-1.1.1-cp39-cp39-win_amd64.whl (16 kB)
Collecting pandocfilters>=1.4.1
  Downloading pandocfilters-1.4.3.tar.gz (16 kB)
Collecting entrypoints>=0.2.2
  Downloading entrypoints-0.3-py2.py3-none-any.whl (11 kB)
Collecting bleach
  Downloading bleach-3.3.0-py2.py3-none-any.whl (283 kB)
     |████████████████████████████████| 283 kB 504 kB/s
Collecting mistune<2,>=0.8.1
  Downloading mistune-0.8.4-py2.py3-none-any.whl (16 kB)
Collecting jupyterlab-pygments
  Downloading jupyterlab_pygments-0.1.2-py2.py3-none-any.whl (4.6 kB)
Collecting testpath
  Downloading testpath-0.4.4-py2.py3-none-any.whl (163 kB)
     |████████████████████████████████| 163 kB 344 kB/s
Collecting nbclient<0.6.0,>=0.5.0
  Downloading nbclient-0.5.1-py3-none-any.whl (65 kB)
     |████████████████████████████████| 65 kB 201 kB/s
Collecting defusedxml
  Downloading defusedxml-0.6.0-py2.py3-none-any.whl (23 kB)
Collecting async-generator
  Downloading async_generator-1.10-py3-none-any.whl (18 kB)
Collecting nest-asyncio
  Downloading nest_asyncio-1.5.1-py3-none-any.whl (5.0 kB)
Collecting webencodings
  Downloading webencodings-0.5.1-py2.py3-none-any.whl (11 kB)
Collecting packaging
  Downloading packaging-20.9-py2.py3-none-any.whl (40 kB)
     |████████████████████████████████| 40 kB 153 kB/s
Requirement already satisfied: pyparsing>=2.0.2 in c:\users\[user name]\appdata\local\programs\python\python39\lib\site-packages (from packaging->bleach->nbconvert->jupyter) (2.4.7)
Collecting qtpy
  Downloading QtPy-1.9.0-py2.py3-none-any.whl (54 kB)
     |████████████████████████████████| 54 kB 78 kB/s
Using legacy 'setup.py install' for pyrsistent, since package 'wheel' is not installed.
Using legacy 'setup.py install' for pywinpty, since package 'wheel' is not installed.
Using legacy 'setup.py install' for pandocfilters, since package 'wheel' is not installed.
Installing collected packages: ipython-genutils, traitlets, pywin32, pyrsistent, attrs, wcwidth, tornado, pyzmq, parso, jupyter-core, jsonschema, webencodings, pygments, pycparser, prompt-toolkit, pickleshare, packaging, nest-asyncio, nbformat, MarkupSafe, jupyter-client, jedi, decorator, colorama, backcall, async-generator, testpath, pywinpty, pandocfilters, nbclient, mistune, jupyterlab-pygments, jinja2, ipython, entrypoints, defusedxml, cffi, bleach, terminado, Send2Trash, prometheus-client, nbconvert, ipykernel, argon2-cffi, notebook, widgetsnbextension, qtpy, jupyterlab-widgets, qtconsole, jupyter-console, ipywidgets, jupyter
    Running setup.py install for pyrsistent ... done
  WARNING: The scripts jupyter-migrate.exe, jupyter-troubleshoot.exe and jupyter.exe are installed in 'C:\Users\[User Name]\AppData\Local\Programs\Python\Python39\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The script jsonschema.exe is installed in 'C:\Users\[User Name]\AppData\Local\Programs\Python\Python39\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The script pygmentize.exe is installed in 'C:\Users\[User Name]\AppData\Local\Programs\Python\Python39\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The script jupyter-trust.exe is installed in 'C:\Users\[User Name]\AppData\Local\Programs\Python\Python39\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The scripts jupyter-kernel.exe, jupyter-kernelspec.exe and jupyter-run.exe are installed in 'C:\Users\[User Name]\AppData\Local\Programs\Python\Python39\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
    Running setup.py install for pywinpty ... done
    Running setup.py install for pandocfilters ... done
  WARNING: The scripts iptest.exe, iptest3.exe, ipython.exe and ipython3.exe are installed in 'C:\Users\[User Name]\AppData\Local\Programs\Python\Python39\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The script jupyter-nbconvert.exe is installed in 'C:\Users\[User Name]\AppData\Local\Programs\Python\Python39\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
	
	Successfully installed MarkupSafe-1.1.1 Send2Trash-1.5.0 argon2-cffi-20.1.0 async-generator-1.10 attrs-20.3.0 backcall-0.2.0 bleach-3.3.0 cffi-1.14.4 colorama-0.4.4 decorator-4.4.2 defusedxml-0.6.0 entrypoints-0.3 ipykernel-5.4.3 ipython-7.20.0 ipython-genutils-0.2.0 ipywidgets-7.6.3 jedi-0.18.0 jinja2-2.11.3 jsonschema-3.2.0 jupyter-1.0.0 jupyter-client-6.1.11 jupyter-console-6.2.0 jupyter-core-4.7.1 jupyterlab-pygments-0.1.2 jupyterlab-widgets-1.0.0 mistune-0.8.4 nbclient-0.5.1 nbconvert-6.0.7 nbformat-5.1.2 nest-asyncio-1.5.1 notebook-6.2.0 packaging-20.9 pandocfilters-1.4.3 parso-0.8.1 pickleshare-0.7.5 prometheus-client-0.9.0 prompt-toolkit-3.0.14 pycparser-2.20 pygments-2.7.4 pyrsistent-0.17.3 pywin32-300 pywinpty-0.5.7 pyzmq-22.0.2 qtconsole-5.0.2 qtpy-1.9.0 terminado-0.9.2 testpath-0.4.4 tornado-6.1 traitlets-5.0.5 wcwidth-0.2.5 webencodings-0.5.1 widgetsnbextension-3.5.1
		
	L:\home\butiran.github.io\src\py>python -m pip install opencv-python
Collecting opencv-python
  Downloading opencv_python-4.5.1.48-cp39-cp39-win_amd64.whl (34.9 MB)
     |████████████████████████████████| 34.9 MB 297 kB/s
Requirement already satisfied: numpy>=1.19.3 in c:\users\[user name]\appdata\local\programs\python\python39\lib\site-packages (from opencv-python) (1.20.0)
Installing collected packages: opencv-python
Successfully installed opencv-python-4.5.1.48
``` 


## references
1. <a name="ref1"></a>The pip developers, "pip 21.0.1", Python Software Foundation, 30 Jan 2021, url <https://pypi.org/project/pip/> [20210204].
2. <a name="ref2"></a>Cygwin authors, "Cygwin", url <https://www.cygwin.com/> [20210204].
3. <a name="ref3"></a>-, "Python 3.9.1", Python Software Foundation, 7 Dec 2020, url <https://www.python.org/downloads/release/python-391/> [20210204].
4. <a name="ref4"></a>Mat, fejese, "Answer to 'Command Prompt - How to add a set path only for that batch file executing?'", StackOverflow, 10 Dec 2014 1731, url <https://stackoverflow.com/a/6832544> [20210204].
5. <a name="ref5"></a>Wikipedia-Autoren, "Albert Einstein", Wikipedia, Die freie Enzyklopädie, 24. Dezember 2020 07:58 UTC, url <https://de.wikipedia.org/w/index.php?oldid=206842501> [20210204].
6. <a name="ref6"></a>John P, "Answer to'Running Jupyter via command line on Windows'", StackOverflow, 7 Sep 2017 01:59, url <https://stackoverflow.com/a/46086745> [20210204].
7. <a name="ref7"></a> asmorkalov, skvark, "opencv-python 4.5.1.48", Python Software Foundation, 2 Jan 2021, url <https://pypi.org/project/opencv-python/> [20210204].

{% comment %}
L:\home\butiran.github.io\src\py>set path=%path%;"C:\Users\Sparisoma Viridi\AppData\Local\Programs\Python\Python39"

L:\home\butiran.github.io\src\py>python -m pip install scipy
Collecting scipy
  Downloading scipy-1.6.0-cp39-cp39-win_amd64.whl (32.7 MB)
     |████████████████████████████████| 32.7 MB 42 kB/s
Requirement already satisfied: numpy>=1.16.5 in c:\users\sparisoma viridi\appdata\local\programs\python\python39\lib\site-packages (from scipy) (1.20.0)
Installing collected packages: scipy
Successfully installed scipy-1.6.0

L:\home\butiran.github.io\src\py>python -m pip install scikit-learn
Collecting scikit-learn
  Downloading scikit_learn-0.24.1-cp39-cp39-win_amd64.whl (6.9 MB)
     |████████████████████████████████| 6.9 MB 171 kB/s
Requirement already satisfied: numpy>=1.13.3 in c:\users\sparisoma viridi\appdata\local\programs\python\python39\lib\site-packages (from scikit-learn) (1.20.0)
Requirement already satisfied: scipy>=0.19.1 in c:\users\sparisoma viridi\appdata\local\programs\python\python39\lib\site-packages (from scikit-learn) (1.6.0)
Collecting joblib>=0.11
  Downloading joblib-1.0.0-py3-none-any.whl (302 kB)
     |████████████████████████████████| 302 kB 384 kB/s
Collecting threadpoolctl>=2.0.0
  Downloading threadpoolctl-2.1.0-py3-none-any.whl (12 kB)
Installing collected packages: threadpoolctl, joblib, scikit-learn
Successfully installed joblib-1.0.0 scikit-learn-0.24.1 threadpoolctl-2.1.0

L:\home\butiran.github.io\src\py>python -m pip install sklearn
Collecting sklearn
  Downloading sklearn-0.0.tar.gz (1.1 kB)
Requirement already satisfied: scikit-learn in c:\users\sparisoma viridi\appdata\local\programs\python\python39\lib\site-packages (from sklearn) (0.24.1)
Requirement already satisfied: numpy>=1.13.3 in c:\users\sparisoma viridi\appdata\local\programs\python\python39\lib\site-packages (from scikit-learn->sklearn) (1.20.0)
Requirement already satisfied: threadpoolctl>=2.0.0 in c:\users\sparisoma viridi\appdata\local\programs\python\python39\lib\site-packages (from scikit-learn->sklearn) (2.1.0)
Requirement already satisfied: scipy>=0.19.1 in c:\users\sparisoma viridi\appdata\local\programs\python\python39\lib\site-packages (from scikit-learn->sklearn) (1.6.0)
Requirement already satisfied: joblib>=0.11 in c:\users\sparisoma viridi\appdata\local\programs\python\python39\lib\site-packages (from scikit-learn->sklearn) (1.0.0)
Using legacy 'setup.py install' for sklearn, since package 'wheel' is not installed.
Installing collected packages: sklearn
    Running setup.py install for sklearn ... done
Successfully installed sklearn-0.0

L:\home\butiran.github.io\src\py>python -m pip install pandas
Collecting pandas
  Downloading pandas-1.2.1-cp39-cp39-win_amd64.whl (9.3 MB)
     |████████████████████████████████| 9.3 MB 386 kB/s
Collecting python-dateutil>=2.7.3
  Downloading python_dateutil-2.8.1-py2.py3-none-any.whl (227 kB)
     |████████████████████████████████| 227 kB 148 kB/s
Collecting pytz>=2017.3
  Downloading pytz-2021.1-py2.py3-none-any.whl (510 kB)
     |████████████████████████████████| 510 kB 226 kB/s
Requirement already satisfied: numpy>=1.16.5 in c:\users\sparisoma viridi\appdata\local\programs\python\python39\lib\site-packages (from pandas) (1.20.0)
Collecting six>=1.5
  Downloading six-1.15.0-py2.py3-none-any.whl (10 kB)
Installing collected packages: six, pytz, python-dateutil, pandas
Successfully installed pandas-1.2.1 python-dateutil-2.8.1 pytz-2021.1 six-1.15.0

L:\home\butiran.github.io\src\py>python -m pip install matplotlib
Collecting matplotlib
  Downloading matplotlib-3.3.4-cp39-cp39-win_amd64.whl (8.5 MB)
     |████████████████████████████████| 8.5 MB 467 kB/s
Collecting kiwisolver>=1.0.1
  Downloading kiwisolver-1.3.1-cp39-cp39-win_amd64.whl (51 kB)
     |████████████████████████████████| 51 kB 46 kB/s
Requirement already satisfied: numpy>=1.15 in c:\users\sparisoma viridi\appdata\local\programs\python\python39\lib\site-packages (from matplotlib) (1.20.0)
Collecting cycler>=0.10
  Downloading cycler-0.10.0-py2.py3-none-any.whl (6.5 kB)
Requirement already satisfied: python-dateutil>=2.1 in c:\users\sparisoma viridi\appdata\local\programs\python\python39\lib\site-packages (from matplotlib) (2.8.1)
Collecting pillow>=6.2.0
  Downloading Pillow-8.1.0-cp39-cp39-win_amd64.whl (2.2 MB)
     |████████████████████████████████| 2.2 MB 328 kB/s
Collecting pyparsing!=2.0.4,!=2.1.2,!=2.1.6,>=2.0.3
  Downloading pyparsing-2.4.7-py2.py3-none-any.whl (67 kB)
     |████████████████████████████████| 67 kB 206 kB/s
Requirement already satisfied: six in c:\users\sparisoma viridi\appdata\local\programs\python\python39\lib\site-packages (from cycler>=0.10->matplotlib) (1.15.0)
Installing collected packages: pyparsing, pillow, kiwisolver, cycler, matplotlib
Successfully installed cycler-0.10.0 kiwisolver-1.3.1 matplotlib-3.3.4 pillow-8.1.0 pyparsing-2.4.7

L:\home\butiran.github.io\src\py>python -m pip install jupyter
Collecting jupyter
  Downloading jupyter-1.0.0-py2.py3-none-any.whl (2.7 kB)
Collecting qtconsole
  Downloading qtconsole-5.0.2-py3-none-any.whl (119 kB)
     |████████████████████████████████| 119 kB 504 kB/s
Collecting nbconvert
  Downloading nbconvert-6.0.7-py3-none-any.whl (552 kB)
     |████████████████████████████████| 552 kB 363 kB/s
Collecting ipywidgets
  Downloading ipywidgets-7.6.3-py2.py3-none-any.whl (121 kB)
     |████████████████████████████████| 121 kB 386 kB/s
Collecting ipykernel
  Downloading ipykernel-5.4.3-py3-none-any.whl (120 kB)
     |████████████████████████████████| 120 kB 252 kB/s
Collecting notebook
  Downloading notebook-6.2.0-py3-none-any.whl (9.5 MB)
     |████████████████████████████████| 9.5 MB 252 kB/s
Collecting jupyter-console
  Downloading jupyter_console-6.2.0-py3-none-any.whl (22 kB)
Collecting jupyter-client
  Downloading jupyter_client-6.1.11-py3-none-any.whl (108 kB)
     |████████████████████████████████| 108 kB 469 kB/s
Collecting traitlets>=4.1.0
  Downloading traitlets-5.0.5-py3-none-any.whl (100 kB)
     |████████████████████████████████| 100 kB 319 kB/s
Collecting tornado>=4.2
  Downloading tornado-6.1-cp39-cp39-win_amd64.whl (422 kB)
     |████████████████████████████████| 422 kB 409 kB/s
Collecting ipython>=5.0.0
  Downloading ipython-7.20.0-py3-none-any.whl (784 kB)
     |████████████████████████████████| 784 kB 598 kB/s
Collecting colorama
  Downloading colorama-0.4.4-py2.py3-none-any.whl (16 kB)
Collecting backcall
  Downloading backcall-0.2.0-py2.py3-none-any.whl (11 kB)
Requirement already satisfied: setuptools>=18.5 in c:\users\sparisoma viridi\appdata\local\programs\python\python39\lib\site-packages (from ipython>=5.0.0->ipykernel->jupyter) (49.2.1)
Collecting pickleshare
  Downloading pickleshare-0.7.5-py2.py3-none-any.whl (6.9 kB)
Collecting decorator
  Downloading decorator-4.4.2-py2.py3-none-any.whl (9.2 kB)
Collecting prompt-toolkit!=3.0.0,!=3.0.1,<3.1.0,>=2.0.0
  Downloading prompt_toolkit-3.0.14-py3-none-any.whl (359 kB)
     |████████████████████████████████| 359 kB 327 kB/s
Collecting pygments
  Downloading Pygments-2.7.4-py3-none-any.whl (950 kB)
     |████████████████████████████████| 950 kB 656 kB/s
Collecting jedi>=0.16
  Downloading jedi-0.18.0-py2.py3-none-any.whl (1.4 MB)
     |████████████████████████████████| 1.4 MB 467 kB/s
Collecting parso<0.9.0,>=0.8.0
  Downloading parso-0.8.1-py2.py3-none-any.whl (93 kB)
     |████████████████████████████████| 93 kB 125 kB/s
Collecting wcwidth
  Downloading wcwidth-0.2.5-py2.py3-none-any.whl (30 kB)
Collecting ipython-genutils
  Downloading ipython_genutils-0.2.0-py2.py3-none-any.whl (26 kB)
Collecting widgetsnbextension~=3.5.0
  Downloading widgetsnbextension-3.5.1-py2.py3-none-any.whl (2.2 MB)
     |████████████████████████████████| 2.2 MB 252 kB/s
Collecting nbformat>=4.2.0
  Downloading nbformat-5.1.2-py3-none-any.whl (113 kB)
     |████████████████████████████████| 113 kB 327 kB/s
Collecting jupyterlab-widgets>=1.0.0
  Downloading jupyterlab_widgets-1.0.0-py3-none-any.whl (243 kB)
     |████████████████████████████████| 243 kB 435 kB/s
Collecting jupyter-core
  Downloading jupyter_core-4.7.1-py3-none-any.whl (82 kB)
     |████████████████████████████████| 82 kB 39 kB/s
Collecting jsonschema!=2.5.0,>=2.4
  Downloading jsonschema-3.2.0-py2.py3-none-any.whl (56 kB)
     |████████████████████████████████| 56 kB 230 kB/s
Requirement already satisfied: six>=1.11.0 in c:\users\sparisoma viridi\appdata\local\programs\python\python39\lib\site-packages (from jsonschema!=2.5.0,>=2.4->nbformat>=4.2.0->ipywidgets->jupyter) (1.15.0)
Collecting attrs>=17.4.0
  Downloading attrs-20.3.0-py2.py3-none-any.whl (49 kB)
     |████████████████████████████████| 49 kB 106 kB/s
Collecting pyrsistent>=0.14.0
  Downloading pyrsistent-0.17.3.tar.gz (106 kB)
     |████████████████████████████████| 106 kB 242 kB/s
Collecting prometheus-client
  Downloading prometheus_client-0.9.0-py2.py3-none-any.whl (53 kB)
     |████████████████████████████████| 53 kB 128 kB/s
Collecting terminado>=0.8.3
  Downloading terminado-0.9.2-py3-none-any.whl (14 kB)
Collecting pyzmq>=17
  Downloading pyzmq-22.0.2-cp39-cp39-win_amd64.whl (1.2 MB)
     |████████████████████████████████| 1.2 MB 1.3 MB/s
Collecting jinja2
  Downloading Jinja2-2.11.3-py2.py3-none-any.whl (125 kB)
     |████████████████████████████████| 125 kB 204 kB/s
Collecting Send2Trash>=1.5.0
  Downloading Send2Trash-1.5.0-py3-none-any.whl (12 kB)
Collecting argon2-cffi
  Downloading argon2_cffi-20.1.0-cp39-cp39-win_amd64.whl (42 kB)
     |████████████████████████████████| 42 kB 65 kB/s
Requirement already satisfied: python-dateutil>=2.1 in c:\users\sparisoma viridi\appdata\local\programs\python\python39\lib\site-packages (from jupyter-client->ipykernel->jupyter) (2.8.1)
Collecting pywin32>=1.0
  Downloading pywin32-300-cp39-cp39-win_amd64.whl (9.2 MB)
     |████████████████████████████████| 9.2 MB 504 kB/s
Collecting pywinpty>=0.5
  Downloading pywinpty-0.5.7.tar.gz (49 kB)
     |████████████████████████████████| 49 kB 226 kB/s
Collecting cffi>=1.0.0
  Downloading cffi-1.14.4-cp39-cp39-win_amd64.whl (179 kB)
     |████████████████████████████████| 179 kB 327 kB/s
Collecting pycparser
  Downloading pycparser-2.20-py2.py3-none-any.whl (112 kB)
     |████████████████████████████████| 112 kB 297 kB/s
Collecting MarkupSafe>=0.23
  Downloading MarkupSafe-1.1.1-cp39-cp39-win_amd64.whl (16 kB)
Collecting pandocfilters>=1.4.1
  Downloading pandocfilters-1.4.3.tar.gz (16 kB)
Collecting entrypoints>=0.2.2
  Downloading entrypoints-0.3-py2.py3-none-any.whl (11 kB)
Collecting bleach
  Downloading bleach-3.3.0-py2.py3-none-any.whl (283 kB)
     |████████████████████████████████| 283 kB 504 kB/s
Collecting mistune<2,>=0.8.1
  Downloading mistune-0.8.4-py2.py3-none-any.whl (16 kB)
Collecting jupyterlab-pygments
  Downloading jupyterlab_pygments-0.1.2-py2.py3-none-any.whl (4.6 kB)
Collecting testpath
  Downloading testpath-0.4.4-py2.py3-none-any.whl (163 kB)
     |████████████████████████████████| 163 kB 344 kB/s
Collecting nbclient<0.6.0,>=0.5.0
  Downloading nbclient-0.5.1-py3-none-any.whl (65 kB)
     |████████████████████████████████| 65 kB 201 kB/s
Collecting defusedxml
  Downloading defusedxml-0.6.0-py2.py3-none-any.whl (23 kB)
Collecting async-generator
  Downloading async_generator-1.10-py3-none-any.whl (18 kB)
Collecting nest-asyncio
  Downloading nest_asyncio-1.5.1-py3-none-any.whl (5.0 kB)
Collecting webencodings
  Downloading webencodings-0.5.1-py2.py3-none-any.whl (11 kB)
Collecting packaging
  Downloading packaging-20.9-py2.py3-none-any.whl (40 kB)
     |████████████████████████████████| 40 kB 153 kB/s
Requirement already satisfied: pyparsing>=2.0.2 in c:\users\sparisoma viridi\appdata\local\programs\python\python39\lib\site-packages (from packaging->bleach->nbconvert->jupyter) (2.4.7)
Collecting qtpy
  Downloading QtPy-1.9.0-py2.py3-none-any.whl (54 kB)
     |████████████████████████████████| 54 kB 78 kB/s
Using legacy 'setup.py install' for pyrsistent, since package 'wheel' is not installed.
Using legacy 'setup.py install' for pywinpty, since package 'wheel' is not installed.
Using legacy 'setup.py install' for pandocfilters, since package 'wheel' is not installed.
Installing collected packages: ipython-genutils, traitlets, pywin32, pyrsistent, attrs, wcwidth, tornado, pyzmq, parso, jupyter-core, jsonschema, webencodings, pygments, pycparser, prompt-toolkit, pickleshare, packaging, nest-asyncio, nbformat, MarkupSafe, jupyter-client, jedi, decorator, colorama, backcall, async-generator, testpath, pywinpty, pandocfilters, nbclient, mistune, jupyterlab-pygments, jinja2, ipython, entrypoints, defusedxml, cffi, bleach, terminado, Send2Trash, prometheus-client, nbconvert, ipykernel, argon2-cffi, notebook, widgetsnbextension, qtpy, jupyterlab-widgets, qtconsole, jupyter-console, ipywidgets, jupyter
    Running setup.py install for pyrsistent ... done
  WARNING: The scripts jupyter-migrate.exe, jupyter-troubleshoot.exe and jupyter.exe are installed in 'C:\Users\Sparisoma Viridi\AppData\Local\Programs\Python\Python39\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The script jsonschema.exe is installed in 'C:\Users\Sparisoma Viridi\AppData\Local\Programs\Python\Python39\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The script pygmentize.exe is installed in 'C:\Users\Sparisoma Viridi\AppData\Local\Programs\Python\Python39\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The script jupyter-trust.exe is installed in 'C:\Users\Sparisoma Viridi\AppData\Local\Programs\Python\Python39\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The scripts jupyter-kernel.exe, jupyter-kernelspec.exe and jupyter-run.exe are installed in 'C:\Users\Sparisoma Viridi\AppData\Local\Programs\Python\Python39\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
    Running setup.py install for pywinpty ... done
    Running setup.py install for pandocfilters ... done
  WARNING: The scripts iptest.exe, iptest3.exe, ipython.exe and ipython3.exe are installed in 'C:\Users\Sparisoma Viridi\AppData\Local\Programs\Python\Python39\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The script jupyter-nbconvert.exe is installed in 'C:\Users\Sparisoma Viridi\AppData\Local\Programs\Python\Python39\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
	
	Successfully installed MarkupSafe-1.1.1 Send2Trash-1.5.0 argon2-cffi-20.1.0 async-generator-1.10 attrs-20.3.0 backcall-0.2.0 bleach-3.3.0 cffi-1.14.4 colorama-0.4.4 decorator-4.4.2 defusedxml-0.6.0 entrypoints-0.3 ipykernel-5.4.3 ipython-7.20.0 ipython-genutils-0.2.0 ipywidgets-7.6.3 jedi-0.18.0 jinja2-2.11.3 jsonschema-3.2.0 jupyter-1.0.0 jupyter-client-6.1.11 jupyter-console-6.2.0 jupyter-core-4.7.1 jupyterlab-pygments-0.1.2 jupyterlab-widgets-1.0.0 mistune-0.8.4 nbclient-0.5.1 nbconvert-6.0.7 nbformat-5.1.2 nest-asyncio-1.5.1 notebook-6.2.0 packaging-20.9 pandocfilters-1.4.3 parso-0.8.1 pickleshare-0.7.5 prometheus-client-0.9.0 prompt-toolkit-3.0.14 pycparser-2.20 pygments-2.7.4 pyrsistent-0.17.3 pywin32-300 pywinpty-0.5.7 pyzmq-22.0.2 qtconsole-5.0.2 qtpy-1.9.0 terminado-0.9.2 testpath-0.4.4 tornado-6.1 traitlets-5.0.5 wcwidth-0.2.5 webencodings-0.5.1 widgetsnbextension-3.5.1
		
	L:\home\butiran.github.io\src\py>python -m pip install opencv-python
Collecting opencv-python
  Downloading opencv_python-4.5.1.48-cp39-cp39-win_amd64.whl (34.9 MB)
     |████████████████████████████████| 34.9 MB 297 kB/s
Requirement already satisfied: numpy>=1.19.3 in c:\users\sparisoma viridi\appdata\local\programs\python\python39\lib\site-packages (from opencv-python) (1.20.0)
Installing collected packages: opencv-python
Successfully installed opencv-python-4.5.1.48
{% endcomment %}
