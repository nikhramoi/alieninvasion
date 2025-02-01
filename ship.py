import pygame


class Ship():
    """Класс управления кораблем"""

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        # Загружаем изображение корабля
        self.image = pygame.image.load('images/starship2.gif')
        self.react = self.image.get_rect()
        # Новые корабли у нижнего края экрана
        self.react.midbottom = self.screen_rect.midbottom

    def blitme(self):
        self.screen.blit(self.image, self.react)
