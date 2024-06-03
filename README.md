# Pyxel Games

Games for my kids made with Pyxel

## Setup

- have python3 installed
- install pyxel
    - `pip3 install -U pyxel`

### Recommended

To make it easier for kids to launch games

- add shortcuts from `bin/` to a directory in your `$PATH`
    - `ln -s $PWD/bin/play $HOME/local/bin/`
    - `ln -s $PWD/bin/games $HOME/local/bin/`

`play` aliases the `pyxel run` command

```sh
play letters
# is the same as
pyxel run letters.py
```

`games` lists all games that can be played from this repo

```sh
games
# is the same as
for file in *.py; do basename $file .py; done
```

