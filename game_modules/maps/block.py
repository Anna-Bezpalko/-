import game_modules.__settings__ as m_settings

class Block(m_settings.Settings):
    def __init__(self, child_x: int, child_y: int, child_width: int, child_height: int, child_name_image: str):
        m_settings.Settings.__init__(self, x= child_x, y= child_y, width= child_width, height= child_height, name_image= child_name_image)