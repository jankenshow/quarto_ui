## 環境
- Mac
- pyenv >= 1.2.10
- python == 3.8.5

## インストール
```
$ brew install tcl-tk

$ export PATH="/usr/local/opt/tcl-tk/bin:$PATH"
$ export LDFLAGS="-L/usr/local/opt/tcl-tk/lib"
$ export CPPFLAGS="-I/usr/local/opt/tcl-tk/include"
$ export PKG_CONFIG_PATH="/usr/local/opt/tcl-tk/lib/pkgconfig"
$ export PYTHON_CONFIGURE_OPTS="--with-tcltk-includes='-I/usr/local/opt/tcl-tk/include' --with-tcltk-libs='-L/usr/local/opt/tcl-tk/lib -ltcl8.6 -ltk8.6'"

$ pyenv install 3.8.5

$ pip install pysimplegui
```