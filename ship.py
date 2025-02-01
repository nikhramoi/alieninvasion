import pygame


class Ship():
    """Класс управления кораблем"""

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        # Загружаем изображение корабля
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        # Новые корабли у нижнего края экрана
        self.rect.midbottom = self.screen_rect.midbottom
        #флаг перемещения
        self.moving_right = False

    def update(self):
        #Обновляет позицию с учетом флага
        if self.moving_right:
            self.rect.x += 1

    def blitme(self):
        self.screen.blit(self.image, self.rect)
