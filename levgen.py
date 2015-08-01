__author__ = 'Anton Firsov'

from random import randrange, choice, randint
import locations


class MyMap:
    def __init__(self, level):
        '''
        Constructor
        '''

        self.map_arr = []  # list of the map
        self.room_list = []  # list of existing rooms
        self.map_level = level  # level the map belongs to

        self.__room_type_list = ['corridor', 'room']  # available types of rooms
        self.Walls = []
        self.__room_size = 0

    def make_map(self, w, h):
        '''
        creates the map, main methods of class
        :param w: map width, number of tiles by х
        :param h: map height, number of tiles by у
        :return:
        '''

        self.map_arr = []  # зачем снова, если конструктор уже так делает?

        self.__map_width = w
        self.__map_height = h

        for y in range(h):  # fill the map with walls
            self.map_arr.append([])
            for x in range(w):
                self.map_arr[y].append(2)

        if len(self.room_list) == 0:  # if there is no rooms, time to add first one
            if self.map_level == 0:  # if level is 0, time to add entrance hall
                room_space = locations.entranceHall()  # import location
                self.place_room(room_space, 5, 1)  # place location
            else:
                room_space = self.make_room(rType='room')
                self.place_room(room_space, 0, 0)

        err_count = 0

        '''while True:
            room_w, room_h = self.make_room(rType='room')
            if self.place_room(room_w, room_h, 0, 0) == False:
                err_count = err_count + 1
            if err_count > 15:
                break'''

        # while len(self.room_list) < 6:
        # while self.__room_size < (self.__map_width*self.__map_height)*0.7:
        while True:  # make and place rooms
            room_space = self.make_room()
            room_y, room_x, direct = self.__pick_wall()
            intrsc_x = room_x  # coords of tile that connects two rooms
            intrsc_y = room_y
            if direct == 'bot':  # now this thing is horrible
                room_y -= len(room_space)
            elif direct == 'top':
                room_y += 1
            elif direct == 'rig':
                room_x += 1
            elif direct == 'lef':
                room_x -= len(room_space[0])
            if self.place_room(room_space, room_x, room_y) == True:
                self.map_arr[intrsc_y][intrsc_x] = 1
            else:
                err_count = err_count + 1  # if it is impossible to place room, that is an error
            if err_count > 15:  # if 15 errors were made, in can not place rooms anymore
                break
            # for i in range(len(self.room_list)):
                # self.__room_size = self.__room_size + self.room_list[i][2]*self.room_list[i][3]

        '''while self.__room_size < (self.__map_width*self.__map_height)*0.7:
            room_w, room_h = self.make_room(rType='room')
            self.place_room(room_w, room_h, 0, 0)
            self.__room_size  = 0
            for i in range(len(self.room_list)):
                self.__room_size = self.__room_size + self.room_list[i][2]*self.room_list[i][3]'''

    def __pick_wall(self):
        '''
        picks a random wall attached to existing room
        :return: coords of tile, direction where new room should be placed
        '''
        while True:
            x_wall = randrange(1, self.__map_width-2)
            y_wall = randrange(1, self.__map_height-2)
            if self.map_arr[y_wall][x_wall] == 2:
                if self.map_arr[y_wall-1][x_wall] == 1:
                    direct = 'top'
                    break
                elif self.map_arr[y_wall+1][x_wall] == 1:
                    direct = 'bot'
                    break
                elif self.map_arr[y_wall][x_wall-1] == 1:
                    direct = 'rig'
                    break
                elif self.map_arr[y_wall][x_wall+1] == 1:
                    direct = 'lef'
                    break
        return y_wall, x_wall, direct

    def make_room(self, rType=None):
        '''
        makes new room
        :param rType: room type (None if choose randomly)
        :return: list of tile codes
        '''

        space = []

        if rType is None:
            rType = choice(self.__room_type_list)

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

        for k in range(h):
            space.append([])
            for l in range(w):
                space[k].append(1)

        return space

    def __check_space(self, w, h, x_coord, y_coord):
        '''
        checks if space for the new room is free
        '''

        if x_coord < 1 or y_coord < 1:
            return False
        if x_coord + w > self.__map_width - 2 or y_coord + h > self.__map_height - 2:
            return False

        for k in range(h):
            for l in range(w):
                if self.map_arr[y_coord+k][x_coord+l] == 1:
                    return False
        return True

    def place_room(self, space, x_coord, y_coord):
        '''
        places room on the map
        '''

        if x_coord == 0:
            x_coord = randrange(1,self.__map_width-2-len(space[0]))
        if y_coord == 0:
            y_coord = randrange(1,self.__map_height-2-len(space))

        if self.__check_space(len(space[0]), len(space), x_coord, y_coord) == True:  # исправить!
            space = list(reversed(space))
            for k in range(len(space)):
                for l in range(len(space[k])):
                    self.map_arr[y_coord+k][x_coord+l] = space[k][l]
        else:
            return False

        self.room_list.append([x_coord, y_coord, len(space[0]), len(space)])
        return True


''' map dimensions '''

start_x = 50
start_y = 30

''' create map  '''

themap = MyMap(0)  # making map of the first level
themap.make_map(start_x, start_y)

''' prints the map '''

for y in range(len(themap.map_arr)-1, -1, -1):
    line = ""
    for x in range(len(themap.map_arr[y])):
        if themap.map_arr[y][x] == 0:
            line += " "
        if themap.map_arr[y][x] == 1:
            line += "."
        if themap.map_arr[y][x] == 2:
            line += "#"
        if themap.map_arr[y][x] == 7:
            line += "P"
    print(line)