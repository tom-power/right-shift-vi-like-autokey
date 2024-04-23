# Vi like key bindings for Linux and X11

Inspired by vi like editor keybindings, these [autokey](https://github.com/autokey/autokey) scripts have more or less saved my life, YMMV!

![demo](https://github.com/tom-power/right-shift-vi-like-autokey/blob/main/assets/demo.gif)

### Mappings

With **right shift/hyper** as modifier, can be combined with other modifiers:

#### Movement

| From    | To                |
| ------- | ----------------- |
| h/j/k/l | arrow keys        |
| w/b     | word forward/back |
| a/e     | home/end          |
| p/;     | page up/down      |

#### Editing

| From          | To               |
| ------------- | ---------------- |
| s/c/v/x/z/t/i | send with ctrl   |
| m             | return           |
| f/d           | delete/backspace |
| space         | tab              |

#### Other

| From       | To                           |
| ---------- | ---------------------------- |
| ctrl+space | escape                       |
| y          | ctrl+w (close tab)           |
| u/o        | ctrl+shift+\[/] (switch tab) |
| g          | ctrl+l (focus address bar)   |

#### Extras

| From          | To                          |
| ------------- | --------------------------- |
| \"+left_shift | double quote wrap selection |
| q+left_shift  | single quote                |
| q             | single quote wrap selection |
| i             | ./                          |
| i+left_shift  | ../                         |
| \`            | ~/                          |

### Installation

##### keyboard

The scripts use hyper as modifier, so you need to map right shift (or whatever you prefer) to use them. The following works for me as mod3 is empty, use `xmodmap` to confirm then:

```shell
xmodmap -e "remove shift = Shift_R" &&
xmodmap -e "remove mod4 = Hyper_L" &&
xmodmap -e "keysym Shift_R = Hyper_L" &&
xmodmap -e "add mod3 = Hyper_L"
```

##### autokey

Install [autokey](https://github.com/autokey/autokey), then:

```bash
clone https://github.com/tom-power/right-shift-vi-like-autokey &&
cd ./right-shift-vi-like-autokey &&
./install.sh
```

review in `autokey -> Show main window`

##### Notes

run `setxkbmap -option ctrl:nocaps` before `xmodmap` to map capslock to control
