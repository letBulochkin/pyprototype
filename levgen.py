#=========================
#
#=========================


from random import *

class MyMap:

#координатная ось карты перевернута, ось Х направлена вправо (как обычно), ось У - вниз.

	def __init__(self):
		self.roomList=[]
		self.isRoomExist=False #ни одной команты нет
		
	def makeMap(self,w,h): #получаем  ширину startx и высоту starty
		
		self.MapArr = [] #массив карты, здесь хранится карта
		
		for y in range(h): #заполняем массив карты сплошными стенами, перебираем строки по Y... 
			temp = []
			for x in range(w): #...внутри перебираем символы в строке по Х
				temp.append(2)
			self.MapArr.append(temp)
		
		if len(self.roomList)==0: 
			rw,rh = self.makeRoom(1);			
			x=randrange(w-2-rw)+1	#выбираем позицию для комнаты, 2 - границы комнаты
			y=randrange(h-2-rh)+1
			self.roomList.append(self.placeRoom(x,y,rw,rh))
		#else
			
			
		
			
	def makeRoom(self,rtype):
		if rtype==1:				#1 - комната
			rwide=randrange(5,10) #задаем произвольные размеры комнаты от 5 до 12
			rhigh=randrange(5,10)
		#elif rtype==2:				#2 - rj
			return rwide,rhigh 
	

	def placeRoom(self,position_x,position_y,room_wid,room_hei):
		
		########################################
		#print('=',room_wid,room_hei,'=') #убрть!
		#print('=',position_x,position_y,'=')
		########################################
		
		for l in range(position_y,position_y+room_hei): 
			for k in range(position_x,position_x+room_wid):
				#print(k,l)
				self.MapArr[l][k]=1
		room = [position_x,position_y,position_x+room_wid,position_y+room_hei]
		return room
		


			
startx=40   # map width - задаем ширину карты
starty=20   # map height- задаем длину карты

#координатная ось карты перевернута, ось Х направлена вправо (как обычно), ось У - вниз.

themap = MyMap()
themap.makeMap(startx,starty)
 
for y in range(starty): #идем по строкам карты, перебираем координаты по У
        line = ""
        for x in range(startx): #идем по каждому символу в строке, перебираем координаты Х
                if themap.MapArr[y][x]==0:
                        line += " "
                if themap.MapArr[y][x]==1:
                        line += "."
                if themap.MapArr[y][x]==2:
                        line += "#"
                if themap.MapArr[y][x]==3 or themap.MapArr[y][x]==4 or themap.MapArr[y][x]==5:
                        line += "+"
        print(line)
		
print (themap.roomList)
input();
