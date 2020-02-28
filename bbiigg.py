import os
import sys

import pygame
import requests
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLineEdit


class Form(QMainWindow):
    def __init__(self):
        super().__init__()
        main_window = uic.loadUi('untitled.ui', self)
        self.pushButton.clicked.connect(self.go)

    def go(self):
        self.close()
        do()

def do():
    response = None
    ms = 0.002
    map_request = "http://static-maps.yandex.ru/1.x/?ll=37.530887,55.703118&spn={},{}&l=map".format(str(ms), str(ms))
    response = requests.get(map_request)


    if not response:
        print("Ошибка выполнения запроса:")
        print(map_request)
        print("Http статус:", response.status_code, "(", response.reason, ")")
        sys.exit(1)

    map_file = "map.png"
    with open(map_file, "wb") as file:
        file.write(response.content)

    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    screen.blit(pygame.image.load(map_file), (0, 0))
    pygame.display.flip()
    running = True
    while running:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                running = False
            '''elif i.type == pygame.MOUSEBUTTONDOWN and i.button == 4:
                ms += 0.001
                map_request = "http://static-maps.yandex.ru/1.x/?ll=37.530887,55.703118&spn={},{}&l=map".format(str(ms), str(ms))
                response = requests.get(map_request)
                map_file = "map.png"
                with open(map_file, "wb") as file:
                    file.write(response.content)
                screen.blit(pygame.image.load(map_file), (0, 0))
                pygame.display.flip()
            elif i.type == pygame.MOUSEBUTTONDOWN and i.button == 5:
                ms -= 0.001
                map_request = "http://static-maps.yandex.ru/1.x/?ll=37.530887,55.703118&spn={},{}&l=map".format(str(ms), str(ms))
                response = requests.get(map_request)
                map_file = "map.png"
                with open(map_file, "wb") as file:
                    file.write(response.content)
                screen.blit(pygame.image.load(map_file), (0, 0))
                pygame.display.flip()'''
    pygame.quit()

    os.remove(map_file)


app = QApplication(sys.argv)
ex = Form()
ex.show()
sys.exit(app.exec_())
