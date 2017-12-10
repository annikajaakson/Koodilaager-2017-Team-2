from settings import*

class Map:
    def __init__(self):
        self.map_data = []

    def map(self):
        k = 0
        for i in range(GRIDHEIGHT):
            self.map_data.append([])

            for j in range(GRIDWIDTH):
                self.map_data[i].append(k)
            if k == 1:
                k = 0
            elif k == 0:
                k = 1
        return self.map_data