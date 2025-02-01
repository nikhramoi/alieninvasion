import pygame, settings


class Ship():
    """Класс управления кораблем"""

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        # Загружаем изображение корабля
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        # Новые корабли у нижнего края экрана
        self.rect.midbottom = self.screen_rect.midbottom
        # Сохранение вещественной координаты центра корабля
        self.x = float(self.rect.x)
        #флаг перемещения
        self.moving_right = False
        self.moving_left = False

    def update(self):
        #Обновляет позицию с учетом флага
        if self.moving_right:
            self.x += self.settings.ship_speed_factor
        if self.moving_left:
            self.x -= self.settings.ship_speed_factor
        #обновление позиции по x траектории
        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)
