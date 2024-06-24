import game_modules.maps.block as m_block
import game_modules.maps.list_maps as list_maps

def create_map_level():
    x_screen = 0
    y_screen = 0
    for min_list in list_maps.list_position_level_1:
        for str_number in min_list:
            if str_number == ' ':
                pass
            elif str_number == '1':
                block = m_block.Block(child_x= x_screen, child_y= y_screen, child_width= 50, child_height= 50, child_name_image= 'map/level_1/1.png')
                list_maps.list_level_1.append(block)
            elif str_number == '2':
                block = m_block.Block(child_x= x_screen, child_y= y_screen, child_width= 50, child_height= 50, child_name_image= 'map/level_1/2.png')
                list_maps.list_level_1.append(block)
            elif str_number == '3':
                block = m_block.Block(child_x= x_screen, child_y= y_screen, child_width= 50, child_height= 50, child_name_image= 'map/level_1/3.png')
                list_maps.list_level_1.append(block)
            elif str_number == "4":
                block = m_block.Block(child_x= x_screen, child_y= y_screen, child_width= 50, child_height= 50, child_name_image= 'map/level_1/4.png')
                list_maps.list_level_1.append(block)
            elif str_number == "5":
                block = m_block.Block(child_x= x_screen, child_y= y_screen, child_width= 50, child_height= 50, child_name_image= 'map/level_1/5.png')
                list_maps.list_level_1.append(block)
            elif str_number == "6":
                block = m_block.Block(child_x= x_screen, child_y= y_screen, child_width= 50, child_height= 50, child_name_image= 'map/level_1/6.png')
                list_maps.list_level_1.append(block)
            elif str_number == "7":
                block = m_block.Block(child_x= x_screen, child_y= y_screen, child_width= 50, child_height= 50, child_name_image= 'map/level_1/7.png')
                list_maps.list_level_1.append(block)
            elif str_number == "8":
                block = m_block.Block(child_x= x_screen, child_y= y_screen, child_width= 50, child_height= 50, child_name_image= 'map/level_1/8.png')
                list_maps.list_level_1.append(block)
            elif str_number == "9":
                block = m_block.Block(child_x= x_screen, child_y= y_screen, child_width= 50, child_height= 50, child_name_image= 'map/level_1/9.png')
                list_maps.list_level_1.append(block)
            elif str_number == "п":
                block = m_block.Block(child_x= x_screen, child_y= y_screen, child_width= 50, child_height= 50, child_name_image= 'map/level_1/п.png')
                list_maps.list_level_1.append(block)
            elif str_number == "д":
                block = m_block.Block(child_x= x_screen, child_y= y_screen, child_width= 50, child_height= 50, child_name_image= 'map/level_1/д.png')
                list_maps.list_level_1.append(block)
            elif str_number == "т":
                block = m_block.Block(child_x= x_screen, child_y= y_screen, child_width= 50, child_height= 50, child_name_image= 'map/level_1/т.png')
                list_maps.list_level_1.append(block)
            x_screen += 50
        y_screen += 50
        x_screen = 0

create_map_level()