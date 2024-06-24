
'''
    Файл що відповідає за пошук абсолютного шляху до файлу який вказано у параметрі file_name
'''

import os

print()
print(f"Абсолютний шлях до файлу в якому було викликано змінну __file__: {__file__}")
print()
print(f"Абсолютний шлях до папки pygame_one_lesson: {os.path.abspath(__file__ + '/../..')}")
print()
# функція пошуку абсолютного шляху
def search_abs_path(file_name: str):
    return os.path.abspath(__file__ + f"/../../images/{file_name}")


