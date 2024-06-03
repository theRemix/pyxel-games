import pyxel
from random import choice, randrange

game_width = 260
game_height = 200
background_color = 7

pyxel_keys = {
    "a": pyxel.KEY_A,
    "s": pyxel.KEY_S,
    "d": pyxel.KEY_D,
    "f": pyxel.KEY_F,
    "g": pyxel.KEY_G,
    "h": pyxel.KEY_H,
    "j": pyxel.KEY_J,
    "k": pyxel.KEY_K,
    "l": pyxel.KEY_L,
}


class Letter:
    def random_letter(self):
        return choice(list(pyxel_keys.keys()))

    def __init__(self):
        self.color = 1
        self.fall_speed = 0.5
        self.y = 0
        self.x = randrange(1, game_width - 1)
        self.letter = self.random_letter()

    def update(self):
        self.y = (self.y + self.fall_speed) % pyxel.height

    def draw(self):
        pyxel.text(self.x, self.y, self.letter, self.color)


class App:
    def __init__(self):

        pyxel.init(game_width, game_height)

        self.cur_letter = Letter()

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnr(pyxel_keys[self.cur_letter.letter]):
            self.cur_letter = Letter()

        self.cur_letter.update()

    def draw(self):
        pyxel.cls(background_color)
        self.cur_letter.draw()


App()
