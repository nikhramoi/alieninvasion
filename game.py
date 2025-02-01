import sys, pygame
from settings import Settings


class AlienInvasion:
    """Класс инициализации игры"""

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

    def run_game(self):
        """Запускаем цикл игры"""
        while True:
            # Следим за клавой и мышкой
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # Назначаем цвет фона
            self.screen.fill(self.settings.bg_color)
            # Последний прорисованный экран
            pygame.display.flip()


if __name__ == '__main__':
    # Создаем экземпляр класса
    ai = AlienInvasion()
    # Запускаем игру
    ai.run_game()
