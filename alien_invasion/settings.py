from tkinter import *
root = Tk()


class Settings():

    def __init__(self):
        self.screen_width = (root.winfo_screenwidth() - 10)
        self.screen_heigth = (root.winfo_screenheight() - 30)
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 1.5
        self.ship_limit = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_speed_factor = 2
        self.bullets_allowed = 3
        self.alien_speed_factor = 0.6
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 2
        self.alien_speed_factor = 0.6
        self.fleet_direction = 1
        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.score_scale * self.alien_points)
