__author__ = 'Anton Firsov'

from random import *

''' Создание карты уровня. Карта уровня содержит:
1. список точек/позиций карты
2. список комнат'''


class MyMap:
    def __init__(self):
        '''
        Конструктор класса
        '''

        self.MapArr = []  # массив карты
        self.RoomList = []  # список существующих комнат
        self.RoomTypeList = ['corridor', 'room']  # доступные типы комнат
        self.Walls = []  # список доступных стен
        self.RoomSize = 0  # что это вообще?

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

        for y in range(h):  # заполняем карту пустотой
            self.MapArr.append([])
            for x in range(w):
                self.MapArr[y].append(2)

        if len(self.RoomList) == 0:  # если список комнат пуст, надо создать первую
            room_w, room_h = self.makeRoom(rType='room')  # создаем комнату типа "комната", получаем ее размеры
            self.placeRoom(room_w, room_h, 0, 0)  # помещаем комнату с заданными размерами

        errCount = 0

        '''while True:
            room_w, room_h = self.makeRoom(rType='room')
            if self.placeRoom(room_w, room_h, 0, 0) == False:
                errCount = errCount + 1
            if errCount > 15:
                break'''

        # while len(self.RoomList) < 6:
        # while self.RoomSize < (self.mapWidth*self.mapHeight)*0.7:
        while True:
            room_w, room_h = self.makeRoom()
            room_y, room_x, direct = self.pickWall()
            intrsc_x = room_x
            intrsc_y = room_y
            if direct == 'bot':
                room_y -= room_h
            elif direct == 'top':
                room_y += 1
            elif direct == 'rig':
                room_x += 1
            elif direct == 'lef':
                room_x -= room_w
            # print(room_x,room_y)
            if self.placeRoom(room_w, room_h, room_x, room_y) == True:
                self.MapArr[intrsc_y][intrsc_x] = 1
            else:
                errCount = errCount + 1
            if errCount > 15:
                break
            # for i in range(len(self.RoomList)):
                # self.RoomSize = self.RoomSize + self.RoomList[i][2]*self.RoomList[i][3]

        '''while self.RoomSize < (self.mapWidth*self.mapHeight)*0.7:
            room_w, room_h = self.makeRoom(rType='room')
            self.placeRoom(room_w, room_h, 0, 0)
            self.RoomSize  = 0
            for i in range(len(self.RoomList)):
                self.RoomSize = self.RoomSize + self.RoomList[i][2]*self.RoomList[i][3]'''

    def pickWall(self):
        while True:
            x_wall = randrange(1, self.mapWidth-2)
            y_wall = randrange(1, self.mapHeight-2)
            if self.MapArr[y_wall][x_wall] == 2:
                if self.MapArr[y_wall-1][x_wall] == 1:
                    direct = 'top'
                    break
                elif self.MapArr[y_wall+1][x_wall] == 1:
                    direct = 'bot'
                    break
                elif self.MapArr[y_wall][x_wall-1] == 1:
                    direct = 'rig'
                    break
                elif self.MapArr[y_wall][x_wall+1] == 1:
                    direct = 'lef'
                    break
        return y_wall, x_wall, direct

    def makeRoom(self, rType=None):
        '''
        Задает размеры будущей комнаты
        :param rType: тип комнаты (None если задать произвольно)
        :return: размеры комнаты
        '''

        if rType is None:
            rType = choice(self.RoomTypeList)

        if rType == 'room':
            w = randrange(2,11)
            h = randrange(2,11)
        elif rType == 'corridor':
            if randint(0,1) == 0:
                w = 1
                h = randrange(5,11)
            else:
                w = randrange(5,11)
                h = 1

        return w, h

    def checkSpace(self, w, h, x_coord, y_coord):

        if x_coord < 1 or y_coord < 1:
            return False
        if x_coord + w > self.mapWidth - 2 or y_coord + h > self.mapHeight - 2:
            return False

        for k in range(w):
            for l in range(h):
                if self.MapArr[y_coord+l][x_coord+k] == 1:
                    return False
        return True

    def placeRoom(self, w, h, x_coord, y_coord):
        '''
        помещает комнату на карту
        :param w: длина комнаты
        :param h: ширина комнаты
        :param x_coord: координата (0 если задать случайно)
        :param y_coord: координата (0 если задать случайно)
        :return:
        '''

        if x_coord == 0:
            x_coord = randrange(1,self.mapWidth-2-w)
        if y_coord == 0:
            y_coord = randrange(1,self.mapHeight-2-h)

        if self.checkSpace(w, h, x_coord, y_coord) == True:
            for k in range(w):
                for l in range(h):
                    self.MapArr[y_coord+l][x_coord+k] = 1
        else:
            return False

        self.RoomList.append([x_coord, y_coord, w, h])
        return True


''' задаем ширину и высоту карты '''

start_x = 50
start_y = 30

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