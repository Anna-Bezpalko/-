'''
    Файл що відповідає за основні налаштування гри 
'''
import pygame
import game_modules.__search_abs_path__ as m_path
import game_modules.maps.list_maps as list_maps

# Завантажуємо налаштування pygame
pygame.init()

# Створюємо змінну що відповідає за розмір ширини екрану гри
screen_width = 1400
# Створюємо змінну що відповідає за розмір висоти екрану гри
screen_height = 800
# Створюємо змінну що відповідає за фоновий колір екрану гри
screen_color = (0, 255, 0) # tuple - кортеж
#
screen_bg = "screen/1.jpeg"
# screen_bg = "screen/2.png"
list_bot = []
# 
FPS = pygame.time.Clock()
#
class Settings:
    #
    def __init__(
            self, 
            x: int | None = None, 
            y: int | None = None, 
            width: int | None = None, 
            height: int | None = None, 
            color: tuple[int] | None = None, 
            name_image: str | None = None
        ):
        self.X = x
        self.Y = y
        self.WIDTH = width
        self.HEIGHT = height
        self.COLOR = color
        self.NAME_IMAGE = name_image
        self.IMAGE = self.load_image()
        # Задіюємо у функції анімації персонажів 
        self.COUNT_MAIN_WHILE = 0 # Рахуємо кількість повторень основного циклу гри 
        self.COUNT_PICTURE = 0 # Відповідає за індекс зображення у списку зоюражень персонажа 
        #
        self.GRAVITY = True
        #
        self.COUNT_GRAVITY = 0
        #
        self.SPEED_GRAVITY = 5
        #
        self.TIME_JUMP = 30
        #
        self.FLIP_X = False #
        #
        self.START_JUMP = False #
        #
        self.LIST_IMAGE_GRAVITY_L = []
        self.LIST_IMAGE_GRAVITY_R = []
        self.LIST_IMAGES_RUN_LEFT = [] #
        self.LIST_IMAGES_RUN_RIGHT = [] #
        self.LIST_IMAGES_IDLE_L = [] #
        self.LIST_IMAGES_IDLE_R = [] #

        self.DEA = False
    #
    def load_image(self, flip_h: bool = False):
        # Завантажуємо до змінної абсолютний шлях до зображення 
        image_abs_path = m_path.search_abs_path(file_name= self.NAME_IMAGE)
        # Завантажуємо зображення до змінної за допомогою отриманого абсолютного шляху
        image = pygame.image.load(image_abs_path)
        if flip_h:
            # Змінюємо зображення під розмір екрану гри
            image_right =  pygame.transform.scale(surface= image, size= (self.WIDTH, self.HEIGHT))
            return pygame.transform.flip(surface= image_right, flip_x= flip_h, flip_y= 0)
        else:
            return pygame.transform.scale(surface= image, size= (self.WIDTH, self.HEIGHT))
    #
    def load_all_images(self, name_folders: str, count_images: int, list_images: list, flip_x: bool):
        if len(list_images) == 0:
            for number in range(count_images):
                self.NAME_IMAGE = f"{name_folders}/{number}.png"
                list_images.append(self.load_image(flip_h= flip_x))
    #
    def draw_sprite(self, screen: pygame.Surface, images: pygame.Surface):
        screen.blit(images, (self.X, self.Y))

    # граиітація для всіх рухомих спрацтів
    def gravity(self, screen: pygame.Surface, name_folder: str, list_images_L: list, list_images_R: str, bot: object | None = None):
        if self.Y + self.HEIGHT < screen_height and self.GRAVITY:
            
            self.COUNT_GRAVITY += 1
            # Падіння вліво
            if self.FLIP_X and self.TIME_JUMP >= 30 or self.FLIP_X and self.COUNT_GRAVITY > 1:
            #
                self.animation(name_folders= name_folder, count_images= 1, screen= screen, tick= 30, list_images= list_images_L, flip_x= True)
            elif self.FLIP_X == False and self.TIME_JUMP >= 30 or self.FLIP_X == False and self.COUNT_GRAVITY > 1:
            # 
                self.animation(name_folders= name_folder, count_images= 1, screen= screen, tick= 30, list_images= list_images_R, flip_x= False)
            self.Y = self.Y + self.SPEED_GRAVITY
            self.collision_down()

    # анімація будь якого персонажу
    def animation(self, name_folders: str, count_images: int, screen: pygame.Surface, tick: int, list_images: list, flip_x: bool = False):
        self.load_all_images(name_folders= name_folders, count_images= count_images, list_images= list_images, flip_x= flip_x)
        if self.COUNT_MAIN_WHILE >= tick:
            self.COUNT_PICTURE += 1
            self.COUNT_MAIN_WHILE = 0
        if self.COUNT_PICTURE >= count_images:
            self.COUNT_PICTURE = 0
        self.draw_sprite(screen= screen, images= list_images[self.COUNT_PICTURE])
        self.COUNT_MAIN_WHILE = self.COUNT_MAIN_WHILE + 1 
    

    # collision down 
    def collision_down(self):
        if self.START_JUMP == False:
        #
            for block in list_maps.list_level_1:
                hero_y_1 = self.Y
                hero_y_2 = self.Y + self.HEIGHT
                #
                block_y_1 = block.Y
                block_y_2 = block.Y + block.HEIGHT
                #
                hero_x_1 = self.X + self.WIDTH * 0.25
                hero_x_2 = self.X + self.WIDTH * 0.75
                #
                block_x_1 = block.X
                block_x_2 = block.X + block.WIDTH
                #
                if hero_x_1 <= block_x_2 and hero_x_1 >= block_x_1 or hero_x_2 <= block_x_2 and hero_x_2 >= block_x_1:
                    if hero_y_1 - 4 < block_y_1 and hero_y_1 - 4 < block_y_2 and hero_y_2 - 4 >= block_y_1 and hero_y_2 - 4 <= block_y_2:
                        self.Y -= self.SPEED_GRAVITY
                        self.TIME_JUMP = 0
                        self.COUNT_GRAVITY = 0
                
    # collision right
    def collision_right(self):
        for block in list_maps.list_level_1:
            if self.X < block.X and self.X < block.X + block.WIDTH and self.X + self.WIDTH * 0.75 >= block.X and self.X + self.WIDTH * 0.75 < block.X + block.WIDTH:
                if self.Y >= block.Y and self.Y < block.Y + block.HEIGHT or self.Y + self.HEIGHT > block.Y and self.Y + self.HEIGHT <= block.Y + block.HEIGHT:
                    self.X -= 5
    # collision right
    def collision_left(self):
        for block in list_maps.list_level_1:
            if self.X > block.X and self.X + self.WIDTH * 0.25 <= block.X + block.WIDTH and self.X + self.WIDTH > block.X and self.X + self.WIDTH > block.X + block.WIDTH:
                if self.Y >= block.Y and self.Y < block.Y + block.HEIGHT or self.Y + self.HEIGHT > block.Y and self.Y + self.HEIGHT <= block.Y + block.HEIGHT:
                    self.X += 5
    # collision up
    def collision_up(self):
        for block in list_maps.list_level_1:
            # Умова руху по осі Х
            if self.X + self.WIDTH * 0.25 <= block.X + block.WIDTH and self.X + self.WIDTH * 0.25 >= block.X or self.X + self.WIDTH * 0.75 <= block.X + block.WIDTH and self.X + self.WIDTH * 0.75 >= block.X:
                # Умова руху по осі Y
                if self.Y + self.HEIGHT * 0.25 <= block.Y + block.HEIGHT and self.Y + self.HEIGHT * 0.25 > block.Y and self.Y + self.HEIGHT > block.Y + block.HEIGHT and self.Y + self.HEIGHT > block.Y:
                    self.START_JUMP = False
                    self.GRAVITY = True
            
    
    

                     
            

        
        
    
        



        


        
    
 
        
        
        
