# Vi like key bindings for Linux and X11

Inspired by vi like editor keybindings, these [autokey](https://github.com/autokey/autokey) configurations have more or less saved my life, YMMV!

### Mappings

With **right shift** as modifier unless mentioned..

#### Movement/navigation

| From            | To                           |
| --------------- | ---------------------------- |
| h/j/k/l         | arrow keys                   |
| w/b             | word forward/back            |
| a/e             | home/end                     |
| p/;             | page up/down                 |
| u/o             | ctrl+shift+\[/] (tab switch) |
| +ctrl/shift/alt | send with any of above       |

#### Editing

| From             | To               |
| ---------------- | ---------------- |
| s/c/v/x/z/t/i    | send with ctrl   |
| m                | return           |
| f/d              | delete/backspace |
| space            | tab              |
| space+left shift | shift tab        |

#### Other

| From                        | To                         |
| --------------------------- | -------------------------- |
| y                           | ctrl+w (close)             |
| g                           | ctrl+l (focus address bar) |
| ctrl+space (no right_shift) | escape                     |
| ctrl+enter (no right_shift) | ctrl+space                 |

### Extras

Have included some extras scripts I find useful in `src/extras`, install using `--with-extras` below, some descriptions:

| From                    | To                              |
| ----------------------- | ------------------------------- |
| left_shift+double_quote | wrap selection in double quotes |
| q                       | single quote                    |
| i                       | ./                              |
| left_shift+i            | ../                             |
| \`                      | ~/                              |

### Installation

Install [autokey](https://github.com/autokey/autokey), then..

```bash
clone https://github.com/tom-power/right-shift-vi-like-autokey &&
cd ./right-shift-vi-like-autokey &&
./install.sh [--with-extras]
```

you should be able see new scripts in `autokey -> Show main window`
