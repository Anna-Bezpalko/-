import pygame 
import game_modules.__settings__ as m_settings
import game_modules.create_screen.create_screen as m_screen
import game_modules.game_player.main_player_hero as m_player

list_cherry = []

class Bot(m_settings.Settings):
    def __init__(self, child_x: int, child_y: int, child_width: int, child_height: int, child_name_image: str):
        m_settings.Settings.__init__(self, x = child_x, y = child_y, width = child_width, height = child_height, name_image = child_name_image)
        self.LIST_CHERRY_IMAGES = []
        self.LIST_BOT_DEA = []
        # 
        self.SHOW = True 
        self.STOP_MOVE = 80
        self.SPEED_GRAVITY = 1

    #
    def animation_bot(self, name_folder: str, count_image: int, tick: int):
        self.animation(name_folders= name_folder, count_images= count_image, screen= m_screen.screen, tick= tick, list_images= self.LIST_CHERRY_IMAGES, flip_x= False)
    #
    def touch_with_bot(self, hero: m_player.Hero):
        # фіксація дотика героя до бота з правої сторони
        if self.X + self.WIDTH >= hero.X and self.X + self.WIDTH <= hero.X + hero.WIDTH:
            # для жовтої точки героя
            if self.Y < hero.Y and self.Y + self.HEIGHT > hero.Y:
                self.SHOW = False
            # для синьої точки героя
            if self.Y <= hero.Y + hero.HEIGHT // 2 and self.Y + self.HEIGHT >= hero.Y + hero.HEIGHT // 2:
                self.SHOW = False
            # для зеленої точки героя
            if self.Y + self.HEIGHT > hero.Y + hero.HEIGHT and self.Y < hero.Y + hero.HEIGHT:
                self.SHOW = False
        # фіксація дотика героя до бота з лівої сторони
        elif self.X <= hero.X + hero.WIDTH * 0.75 and self.X + self.WIDTH >= hero.X + hero.WIDTH * 0.75:
            # для жовтої точки героя
            if self.Y < hero.Y and self.Y + self.HEIGHT > hero.Y:
                self.SHOW = False
            # для синьої точки героя
            if self.Y <= hero.Y + hero.HEIGHT // 2 and self.Y + self.HEIGHT >= hero.Y + hero.HEIGHT // 2:
                self.SHOW = False
            # для зеленої точки героя
            if self.Y + self.HEIGHT > hero.Y + hero.HEIGHT and self.Y < hero.Y + hero.HEIGHT:
                self.SHOW = False
    #          
    def move_left_bot(self, screen: pygame.Surface):
        count = 12
        if self.STOP_MOVE <= count and self.TIME_JUMP == 0:
            self.animation(name_folders= 'enemy/jump/', count_images= 1, screen= screen, tick= count, list_images= self.LIST_IMAGES_RUN_LEFT, flip_x= False)
            self.GRAVITY = False
            self.Y -= 1
            self.X -= 1
        if self.STOP_MOVE >= count and self.STOP_MOVE <= count * 2 and self.TIME_JUMP == 0:
            self.GRAVITY = True
            self.X -= 1
        if self.STOP_MOVE >= count * 2 and self.STOP_MOVE < 300:
            self.animation(name_folders= 'enemy/idle/', count_images= 4, screen= screen, tick= 20, list_images= self.LIST_IMAGES_IDLE_L, flip_x= False)
        if self.STOP_MOVE >= 300:
            self.STOP_MOVE = 0
        if self.TIME_JUMP == 0:
            self.STOP_MOVE += 1
        # 
    def animation_death(self, screen: pygame.Surface):
        
        if self.COUNT_PICTURE == 5:
            del m_settings.list_bot[-1]
        self.animation(name_folders= "enemy-death/", count_images= 6, screen= screen, tick= 10, list_images= self.LIST_BOT_DEA, flip_x= False )
     
cherry_1 = Bot(child_x = 100, child_y = 0, child_width = 50, child_height = 50, child_name_image = "food/0.png")

cherry_2 = Bot(child_x = 300, child_y = 0, child_width = 50, child_height = 50, child_name_image = "food/0.png")

cherry_3 = Bot(child_x = 1000, child_y = 0, child_width = 50, child_height = 50, child_name_image = "food/0.png")

frog_1 = Bot(child_x= 400, child_y= 130, child_width= 75, child_height= 75, child_name_image= "enemy/idle/0.png")

m_settings.list_bot.extend([cherry_1, cherry_2, cherry_3, frog_1])