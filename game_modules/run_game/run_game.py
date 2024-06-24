
'''
    Файл що запускає гру 
'''

import pygame
import game_modules.create_screen.create_screen as m_screen
import game_modules.download_media.load_image as m_image
import game_modules.game_player.main_player_hero as m_hero
import game_modules.__settings__ as m_settings
import game_modules.maps.creating_maps
import game_modules.maps.list_maps as list_maps
import game_modules.bot_cherry.bot as m_bot

#
def run_game():
    game = True

    while game:
        #
        m_settings.FPS.tick(60)
        # Задаємо відображення фону гри 
        m_screen.screen.blit(m_image.image_bg, (0, 0))
        #
        m_hero.hero.jump(screen= m_screen.screen)
        #
        m_hero.hero.gravity(screen= m_screen.screen, name_folder= "player/gravity/", list_images_L = m_hero.hero.LIST_IMAGE_GRAVITY_L, list_images_R= m_hero.hero.LIST_IMAGE_GRAVITY_R, bot= m_bot.frog_1)
        #
        for block in list_maps.list_level_1:
            block.draw_sprite(screen = m_screen.screen, images= block.IMAGE)
        #
        m_hero.hero.move_left(screen= m_screen.screen)
        m_hero.hero.move_right(screen= m_screen.screen)
      
        #
        if m_bot.cherry_1.SHOW:
            m_bot.cherry_1.animation_bot(name_folder= 'food/', count_image= 7, tick= 10)
            m_bot.cherry_1.gravity(screen= m_screen.screen, name_folder= "food/", list_images_L= m_bot.cherry_1.LIST_CHERRY_IMAGES, list_images_R= m_bot.cherry_1.LIST_CHERRY_IMAGES)
            m_bot.cherry_1.touch_with_bot(hero= m_hero.hero)

        #
        if m_bot.cherry_2.SHOW:
            m_bot.cherry_2.animation_bot(name_folder= 'food/', count_image= 7, tick= 10)
            m_bot.cherry_2.gravity(screen= m_screen.screen, name_folder= "food/", list_images_L= m_bot.cherry_2.LIST_CHERRY_IMAGES, list_images_R= m_bot.cherry_2.LIST_CHERRY_IMAGES)
            m_bot.cherry_2.touch_with_bot(hero= m_hero.hero)

        #
        if m_bot.cherry_3.SHOW:
            m_bot.cherry_3.animation_bot(name_folder= 'food/', count_image= 7, tick= 10)
            m_bot.cherry_3.gravity(screen= m_screen.screen, name_folder= "food/", list_images_L= m_bot.cherry_3.LIST_CHERRY_IMAGES, list_images_R= m_bot.cherry_3.LIST_CHERRY_IMAGES) 
            m_bot.cherry_3.touch_with_bot(hero= m_hero.hero)

        # Frog play
        if m_bot.frog_1 in m_settings.list_bot:
            if m_bot.frog_1.DEA == False:
                m_bot.frog_1.gravity(screen= m_screen.screen, name_folder= "enemy/gravity/", list_images_L= m_bot.frog_1.LIST_CHERRY_IMAGES, list_images_R= m_bot.frog_1.LIST_CHERRY_IMAGES)
                m_bot.frog_1.move_left_bot(screen= m_screen.screen)
            if m_bot.frog_1.DEA == True:
                m_bot.frog_1.animation_death(screen= m_screen.screen)
#   
        # Перевіряємо подію завершення гри
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False # Завершуємо гру
            
        # Оновлюємо екран гри в кінці кожного повторення циклу
        pygame.display.flip()