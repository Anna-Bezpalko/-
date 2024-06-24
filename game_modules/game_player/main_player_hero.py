import game_modules.__settings__ as m_settings
import pygame
# 
class Hero(m_settings.Settings):
    def __init__(self, child_x: int, child_y: int, child_width: int, child_height: int, child_name_image: str):
        m_settings.Settings.__init__(self, x= child_x, y= child_y, width= child_width, height= child_height, name_image= child_name_image) #

        self.LIST_IMAGE_JUMP_L = []
        self.LIST_IMAGE_JUMP_R = []
       
    #
    def gravity(self, screen: pygame.Surface, name_folder: str, list_images_L: list, list_images_R: str, bot: object | None = None):
        super().gravity(screen, name_folder, list_images_L, list_images_R, bot)  
        # Умова вбивства бота
        # перевірка що герой рухається зверху на бота
        if bot != None and self.TIME_JUMP != 0:
            if self.Y < bot.Y and self.Y + self.HEIGHT >= bot.Y:
                if self.X + self.WIDTH // 2 >= bot.X and self.X + self.WIDTH // 2 <= bot.X + bot.WIDTH:
                    bot.DEA = True 
    #
    def move_left(self, screen):
        event_pressed = pygame.key.get_pressed()
        if event_pressed[pygame.K_LEFT] == True and self.X > 0:
            self.X = self.X - 5
            self.FLIP_X = True
            self.collision_left()
            if self.TIME_JUMP == 0 and self.COUNT_GRAVITY <= 1:
                self.animation(name_folders= "player/run/", count_images= 6, screen= screen, tick= 10, list_images= self.LIST_IMAGES_RUN_LEFT, flip_x= True)    
        elif event_pressed[pygame.K_LEFT] == False and event_pressed[pygame.K_RIGHT] == False:
            self.stay(screen= screen)
    #
    def move_right(self, screen):
        event_pressed = pygame.key.get_pressed()
        if event_pressed[pygame.K_RIGHT] == True and self.X < m_settings.screen_width - self.WIDTH * 0.75:
            self.X = self.X + 5
            self.FLIP_X = False
            self.collision_right()
            if self.TIME_JUMP == 0 and self.COUNT_GRAVITY <= 1:
                self.animation(name_folders= "player/run/", count_images= 6, screen= screen, tick= 10, list_images= self.LIST_IMAGES_RUN_RIGHT)
        elif event_pressed[pygame.K_LEFT] == False and event_pressed[pygame.K_RIGHT] == False:
            self.stay(screen= screen) 
    #
    def stay(self, screen):
        if self.TIME_JUMP == 0 and self.COUNT_GRAVITY <= 1:
            if self.FLIP_X:
                self.animation(name_folders= "player/idle/", count_images= 4, screen= screen, tick= 35, list_images= self.LIST_IMAGES_IDLE_L, flip_x=   True)
            else:
                self.animation(name_folders= "player/idle/", count_images= 4, screen= screen, tick= 35, list_images= self.LIST_IMAGES_IDLE_R)
    # Метод що відповідає за стрибок персонажу
    def jump(self, screen: pygame.Surface):
        event_pressed = pygame.key.get_pressed()
        # Якщо кнопка пробіл або кнопка вверх натиснута 
        if event_pressed[pygame.K_SPACE] == True and self.TIME_JUMP == 0 or event_pressed[pygame.K_UP] == True and self.TIME_JUMP == 0:
            self.START_JUMP = True # Дозволяємо стрибок
            self.GRAVITY = False # Вимикаємо гравітацію під час стрибку 
        #
        if self.START_JUMP:
            self.Y -= 5
            self.TIME_JUMP += 1
            if self.FLIP_X:
                self.animation(name_folders= "player/jump/", count_images= 1, screen= screen, tick= 30, list_images= self.LIST_IMAGE_JUMP_L, flip_x= True)
            elif self.FLIP_X == False:
                self.animation(name_folders= "player/jump/", count_images= 1, screen= screen, tick= 30, list_images= self.LIST_IMAGE_JUMP_R, flip_x= False)
            self.collision_up()
        if self.TIME_JUMP >= 30:
            self.START_JUMP = False
            self.GRAVITY = True        
    #
hero = Hero(child_x= 100, child_y= 50, child_width= 100, child_height= 100, child_name_image= "player/gravity/0.png")
# 
