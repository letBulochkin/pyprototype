__author__ = 'Anton Firsov'

from random import *

''' Создание карты уровня. Карта уровня содержит:
1. список точек/позиций карты
2. список комнат

Алгоритм создания карты:
1. заполнить карту стенами
2. создать первую комнату
3. выбрать тип комнаты: комната/коридор
4. задать произвольные размеры в некоторых пределах
5. выбрать случайную точку
6. поместить комнату
7. пометить все граничные клетки
8. выбрать случайную граничую клетку
9. пункт 3. пункт 4.
10. проверить, помещается ли комната так, чтобы присоединиться к выбранной граничной клетке (чо?)
11. если да - пункт 6. если нет - пункт 8.
12. повторять с пункта 7 n раз.
13. вы великолепны! (на самом деле нет)'''


class MyMap:
    def __init__(self):
        self.MapArr = []  # массив карты
        self.RoomList = []  # список существу.щих комнат
        self.RoomTypeList = ['corridor', 'room']  # доступные типы комнат

    def makeMap(self, w, h):
        '''
        создает карту, основной метод класса
        :param w: ширина карты, кол-во клеток по х
        :param h: высота карты, кол-во ячеек по у
        :return:
        '''

        self.MapArr = []  # зачем снова, если конструктор уже так делает?

        self.mapWidth = w
        self.mapHeight = h

        for y in range(h):  # п.1 заполняем все стенами
            self.MapArr.append([])
            for x in range(w):
                self.MapArr[y].append(2)

        if len(self.RoomList) == 0:  # п.2 если комната первая
            room_w, room_h = self.makeRoom(rType='room')
            self.placeRoom(room_w, room_h, 0, 0)  # ???



    def pickWall(self):
        pass

    def makeRoom(self, rType=None):
        '''
        п.3 п.4
        :param rType: тип комнаты
        :return: размеры комнаты
        '''

        if rType is None:
            rType = randrange(self.RoomTypeList)

        if rType == 'room':
            w = randrange(5,11)
            h = randrange(5,11)
        elif rType == 'corridor':
            if randint(0,1) == 0:
                w = 3
                h = randrange(5,15)
            else:
                w = randrange(5,11)
                h = 3

        return w, h

    def checkSpace(self):
        pass


    def placeRoom(self, w, h, x_coord, y_coord):  # ???

        if x_coord == 0:
            x_coord = randrange(1,self.mapWidth-2-w)  # это не работает
        if y_coord == 0:
            y_coord = randrange(1,self.mapHeight-2-h)

        for k in range(w):
            for l in range(h):
                if self.MapArr[y_coord+l][x_coord+k] == 1:
                    return False
                else:
                    self.MapArr[y_coord+l][x_coord+k] = 1
                    # return True





''' задаем ширину и высоту карты '''

start_x = 30
start_y = 20

''' создаем экземпляр карты нужной ширины и высоты '''

themap = MyMap()
themap.makeMap(start_x, start_y)

''' выводим карту '''

for y in range(start_y - 1, -1, -1):
    line = ""
    for x in range(start_x):
        if themap.MapArr[y][x] == 0:
            line += " "
        if themap.MapArr[y][x] == 1:
            line += "."
        if themap.MapArr[y][x] == 2:
            line += "#"
    print(line)
