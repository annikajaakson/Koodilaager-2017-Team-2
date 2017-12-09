from settings import*

class Map:
    def __init__(self):
        self.map_data = []

    def map(self):
        for i in range(GRIDHEIGHT):
            self.map_data.append([])

            for j in range(GRIDWIDTH):
                self.map_data[i].append(0)
