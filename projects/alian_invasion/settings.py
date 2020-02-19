# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 11:46:28 2019

@author: RickyLi
"""

class Settings():
    def __init__(self):
        self.screen_width = 1280
        self.screen_height = 720
        self.bg_color = (152,245,255)
        
        self.ship_speed_factor = 1.5
        self.ship_limit = 3
        
        self.bullet_speed_factor = 3
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullets_allowed = 10
        
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1 #大于零表示向右移动
        