import random

import arcade

class space_battle(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.score = 0
        self.player = None
        self.targets = arcade.SpriteList()
        self.sound = None
        self.player_dx =0
        self.player_dy = 0

    def on_update(self,delta_time):
        self.sound = arcade.load_sound("elec_lightning.wav")
        self.player = arcade.Sprite("f1-ship1-4.png")
        self.player.center_x = 100
        self.player.center_y = 500
        for number in range(5):
            self.target = arcade.Sprite("archer.png")
            self.target.center_x = random.randint(16, 1184)
            self.target.center_y = random.randint(16, 984)
            self.targets.append(self.target)

    def on_draw(self):
        arcade.start_render()
        self.player.draw()
        self.targets.draw()
        arcade.finish_render()

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.LEFT:
            self.player_dx = -3
        elif symbol == arcade.key.RIGHT:
            self.player_dx = 3
        elif symbol == arcade.key.UP:
            self.player_dy = 3

    def on_key_release(self, symbol, modifiers):
        if symbol == arcade.key.LEFT:
            self.player_dx = 0
        elif symbol == arcade.key.RIGHT:
            self.player_dx = 0
        elif symbol == arcade.key.UP:
            self.player_dy = 0

    def on_mouse_press(self, x: 100, y: 200, button: 1, modifiers:()
        if self.key == arcade.key.down


        
