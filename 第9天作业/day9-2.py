import math
class Point:

    def __init__(self, x,y,z=0):
        self.x = x
        self.y = y
        self.z = z
        print("创建了",self)

    def __str__(self):
        return f"Point({self.x},{self.y},{self.z})"

    def __del__(self):
        print("销毁了",self)

    def __add__(self,other):
        if isinstance(other, Point):
            raise TypeError("Can't add two points")
        elif isinstance(other, Vector):
            return Point(self.x+other.x,self.y+other.y,self.z+other.z)
    
    def __sub__(self,other):
        if isinstance(other, Point):
            return Vector(self.x-other.x,self.y-other.y,self.z-other.z)
        elif isinstance(other, Vector):
            return Point(self.x-other.x,self.y-other.y,self.z-other.z)
    
    def __eq__(self, other):
        return (self.x,self.y,self.z) == (other.x,other.y,other.z)

    def __lt__(self,other):
        return self._len() < other._len()

    def _len(self):
        return (self.x**2+self.y**2+self.z**2)**.5
    
class Vector:

    def __init__(self, x,y,z=0):
        self.x = x
        self.y = y
        self.z = z
        self.deg = math.atan2(y,x)
        self.len = self._len()
        
    def __str__(self):
        return f"Vector({self.x},{self.y},{self.z})"
        
    def __add__(self,other):
        if isinstance(other, Vector):
            return Vector(self.x+other.x,self.y+other.y,self.z+other.z)
        elif isinstance(other, Point):
            return Point(self.x+other.x,self.y+other.y,self.z+other.z)
    
    def __sub__(self,other):
        if isinstance(other, Vector):
            return Vector(self.x-other.x,self.y-other.y,self.z-other.z)
        
    def __eq__(self, other):
        return (self.x,self.y,self.z) == (other.x,other.y,other.z)
    
    def __lt__(self,other):
        return self.len < other.len
    
    def _len(self):
        return (self.x**2+self.y**2+self.z**2)**.5
    
    def __mul__(self,x):
        assert self.z == 0
        new_deg = self.deg + math.radians(x)
        return Vector(self.len*math.cos(new_deg),self.len*math.sin(new_deg))
    
    def __truediv__(self,x):
        assert self.z == 0
        new_deg = self.deg - math.radians(x)
        return Vector(self.len*math.cos(new_deg),self.len*math.sin(new_deg))
    
