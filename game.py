import sys, pygame
from settings import Settings
from ship import Ship


class AlienInvasion:
    """Класс инициализации игры"""

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        #pygame.display.set_caption('Alien Invasion')
        self.ship = Ship(self)

    def run_game(self):
        """Запускаем цикл игры"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()

    def _check_events(self):
        """Обрабатывает нажатия клавиш и события мыши."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False


    def _update_screen(self):
        # Назначаем цвет фона
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        # Последний прорисованный экран
        pygame.display.flip()

if __name__ == '__main__':
    # Создаем экземпляр класса
    ai = AlienInvasion()
    # Запускаем игру
    ai.run_game()
