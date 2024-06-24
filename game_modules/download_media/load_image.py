import pygame
import game_modules.__settings__ as m_settings
import game_modules.__search_abs_path__ as m_path
#
def load_image(filename: str):
    # Завантажуємо до змінної абсолютний шлях до зображення 
    screen_image_path = m_path.search_abs_path(file_name= filename)
    print(screen_image_path)
    # Завантажуємо зображення до змінної за допомогою отриманого абсолютного шляху
    screen_image = pygame.image.load(screen_image_path)
    # Змінюємо зображення під розмір екрану гри
    screen_image_tranform = pygame.transform.scale(surface= screen_image, size= (m_settings.screen_width, m_settings.screen_height))
    # Зберігаємо зображення в папці проекту гри, якщо є така необхідність
    # pygame.image.save(screen_image1, m_path.search_abs_path(file_name= '2.png'))
    return screen_image_tranform
#
image_bg = load_image(filename= m_settings.screen_bg)
    