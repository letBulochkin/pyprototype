__author__ = 'Anton Firsov'

from random import *

''' Создание карты уровня. Карта уровня содержит:
1. список точек/позиций карты
2. список комнат'''


class MyMap:
    def __init__(self):
        self.MapArr = []  # массив карты
        self.RoomList = []  # список существу.щих комнат
        self.RoomTypeList = ['corridor', 'room']  # доступные типы комнат
        self.RoomSize = 0

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

        errCount = 0

        '''while True:
            room_w, room_h = self.makeRoom(rType='room')
            if self.placeRoom(room_w, room_h, 0, 0) == False:
                errCount = errCount + 1
            if errCount > 15:
                break'''

        while len(self.RoomList) < 10:
            room_w, room_h = self.makeRoom(rType='room')
            self.placeRoom(room_w, room_h, 0, 0)

        '''while self.RoomSize < (self.mapWidth*self.mapHeight)*0.7:
            room_w, room_h = self.makeRoom(rType='room')
            self.placeRoom(room_w, room_h, 0, 0)
            self.RoomSize  = 0
            for i in range(len(self.RoomList)):
                self.RoomSize = self.RoomSize + self.RoomList[i][2]*self.RoomList[i][3]'''




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

    def __checkSpace(self, w, h, x_coord, y_coord):

        for k in range(w):
            for l in range(h):
                if self.MapArr[y_coord+l][x_coord+k] == 1:
                    return False
        return True


    def placeRoom(self, w, h, x_coord, y_coord):

        if x_coord == 0:
            x_coord = randrange(1,self.mapWidth-2-w)
        if y_coord == 0:
            y_coord = randrange(1,self.mapHeight-2-h)

        if self.__checkSpace(w, h, x_coord, y_coord) == True:
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
