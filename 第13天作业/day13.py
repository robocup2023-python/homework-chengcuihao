import numpy as np
import time

class Universe:
    dx = (1,1,1,0,0,-1,-1,-1)
    dy = (1,0,-1,1,-1,1,0,-1)
    def __init__(self, length=80, width=15):
        self.length = length
        self.width = width
        self.map = np.zeros((width+2,length+2),dtype=bool)

    def Show(self):
        for i in range(1,self.width+1):
            for j in range(1,self.length+1):
                print('*' if self.map[i,j] else ' ',end='')
            print()
    
    def Seed(self, ratio=0.25):
        arr = np.random.rand(self.width,self.length)
        mask = arr<ratio
        self.map[1:-1,1:-1] = mask

    def Next(self):
        mask = np.zeros((self.width,self.length),dtype=bool)
        for i in range(self.width):
            for j in range(self.length):
                mask[i,j] = self._Alive(i+1,j+1)
        self.map[1:-1,1:-1] = mask
        return np.any(mask)

    def _Alive(self, row, col):
        alive = self._Neighbour(row,col)
        if self.map[row,col]:
            return True if alive in (2,3) else False
        else:
            return True if alive == 3 else False

    def _Neighbour(self, row, col):
        alive = 0
        for i in range(8):
            newr,newc = row+Universe.dx[i], col+Universe.dy[i]
            alive += self.map[newr,newc]
        return alive  


class Conway:

    def __init__(self, length=80,width=15,ratio=0.25):
        self.universe = Universe(length, width)
        self.ratio = ratio

    def start(self):
        self.universe.Seed(self.ratio)
        self.Show()
        while self.universe.Next():
            self.Show()
            time.sleep(0.2)
        print("No life is alive. Game over.")

    def Show(self):
        print('\033[2J\033[0;0H')
        self.universe.Show()

c = Conway()
c.start()

        
