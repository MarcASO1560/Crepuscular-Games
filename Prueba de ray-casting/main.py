import pygame as pg
from pygame import *
from camera import Player
from ray_casting import VoxelRender

class App:
    def __init__(self):
        self.res = self.width, self.height = (1920, 1080)
        self.screen = pg.display.set_mode(self.res, pg.FULLSCREEN)
        self.clock = pg.time.Clock()
        self.player = Player()
        self.voxel_render = VoxelRender(self)

    def update(self):
        self.player.update()
        self.voxel_render.update()

    def draw(self):
        self.voxel_render.draw()
        pg.display.flip()

    def run(self):
        while True:
            self.update()
            self.draw()

            [exit() for i in pg.event.get() if i.type == pg.QUIT]
            self.clock.tick(60)
            pg.display.set_caption(f'FPS: {self.clock.get_fps()}')


if __name__ == '__main__':
    app = App()
    app.run()