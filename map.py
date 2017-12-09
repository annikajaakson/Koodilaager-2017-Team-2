from settings import*
GRIDWIDTH = 20
GRIDHEIGHT = 30

map_data = []

class Map:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.speed = 0
        self.map_data = []
    def map(self):
        for i in range(GRIDHEIGHT):
            self.map_data.append([])

            for j in range(GRIDWIDTH):
                self.map_data[i].append(0)
                
print(map_data)