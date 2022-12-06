import arcade

my_window = arcade.open_window(1000, 900, "SpaceBattle")
arcade.set_background_color(arcade.color.BLACK)

arcade.start_render()
for xloc in range(50, 1000, 80):
    arcade.draw_line(xloc, 50, xloc, 800, arcade.color.CEDAR_CHEST, 5)
for yloc in range(50, 900, 80):
    arcade.draw_line(50, yloc, 1000, yloc, arcade.color.ELECTRIC_INDIGO, 5)





arcade.finish_render()

arcade.run()