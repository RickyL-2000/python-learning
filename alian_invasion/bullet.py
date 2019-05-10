# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 10:25:32 2019

@author: RickyLi
"""

import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    
    def __init__(self,ai_settings,screen,ship):
        super().__init__()
        self.screen = screen
        
        #在（0,0)处创建一个表示子弹的矩形，再移到正确的位置
        self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        
        #存储用小数表示的子弹位置
        self.y = float(self.rect.y)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
        
    def update(self):
        #向上移动子弹，更新并表示子弹位置的小数值’
        self.y -= self.speed_factor
        self.rect.y = self.y
        
    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)