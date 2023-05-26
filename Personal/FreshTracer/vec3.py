from __future__ import annotations
#Vec3 class
#rewrite
#imports
import math
from typing import Callable


class vec3(object):
    def __init__(self, x:float, y:float, z:float):
        self.x = x
        self.y = y
        self.z = z

    def to_rgb(self) -> tuple[int,int,int]:
        return (self*255).apply(math.ceil).as_tuple()
    
    def apply(self,func:Callable) -> vec3:
        return vec3(func(self.x),func(self.y),func(self.z))

    def as_tuple(self) -> tuple[float,float,float]:
        return (self.x,self.y,self.z)

    @staticmethod
    def dot(v1:vec3, v2:vec3)-> float:
        return v1.x * v2.x + v1.y * v2.y + v1.z * v2.z

    @staticmethod
    def cross(v1:vec3, v2:vec3) -> vec3:
        x = v1.y * v2.z - v1.z * v2.y
        y = v1.x * v2.x - v1.x * v2.z
        z = v1.z * v2.y - v1.y * v2.x
        return vec3(x, y, z)

    @staticmethod
    def normalize(v:float)-> float:
        return v / v.norm()

    def norm(self)->float:
        return math.sqrt(vec3.dot(self, self))

    def __add__(self, v:vec3) -> vec3:
        return vec3(self.x + v.x, self.y + v.y, self.z + v.z)

    def __neg__(self) ->vec3:
        return vec3(-self.x, -self.y, -self.z)

    def __sub__(self, v:vec3) -> float:
        return self + (-v)

    def __mul__(self, v:vec3|float) -> vec3:
        if isinstance(v, vec3):
            return vec3(self.x * v.x, self.y * v.y, self.z * v.z)
        else:
            return vec3(self.x * v, self.y * v, self.z * v)

    def __rmul__(self, v:vec3) -> vec3:
        return self.__mul__(v)

    def __div__(self, v:vec3|float) -> vec3:
        if isinstance(v, vec3):
            return vec3(self.x / v.x, self.y / v.y, self.z / v.z)
        else:
            return vec3(self.x / v, self.y / v, self.z / v)

    def __str__(self):
        return '[ %.4f, %.4f, %.4f ]' % (self.x, self.y, self.z)



class color(vec3):
   pass