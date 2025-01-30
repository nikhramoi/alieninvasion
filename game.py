import sys
import pygame

class AlienInvasion:
    """Класс инициализации игры"""
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption('Alien Invasion')

    def run_game(self):
        """Запускаем цикл игры"""
        while True:
            #Следим за клавой и мышкой
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            pygame.display.flip()

if __name__ == '__main__':
    #Создаем экземпляр класса
    ai = AlienInvasion()
    #Запускаем игру
    ai.run_game()