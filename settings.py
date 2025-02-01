class Settings():
    """Класс настроек игры"""
    def __init__(self):
        """Инициализация параметров игры"""
        # Настройки экрана
        self.ship_speed_factor = 0.8
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (200, 200, 200)
