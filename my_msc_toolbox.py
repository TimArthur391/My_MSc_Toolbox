import math
class Frustum:
    def __init__(self, height, origin_radius, tip_radius, density) -> None:
        self.height = height #mm
        self.r1 = origin_radius #mm
        self.r2 = tip_radius #mm
        self.desnity = density #g/mm3

    def volume(self):
        return (self.height*(math.pi)/3)*((self.r1**2)+(self.r1*self.r2)+(self.r2**2))

    def mass(self):
        return self.volume() * self.desnity

    def centre_of_mass(self):
        return self.height*((self.r1**2)+(2*self.r1*self.r2)+(3*(self.r2**2))) / \
            4*((self.r1**2)+(self.r1*self.r2)+(self.r2**2))

    def moment_of_interia(self): #about the origin point on the base
        return (1/20)*self.desnity*(math.pi)* \
        ((self.height) * \
            ((self.r2**4)+((self.r2**3)*(self.r1))+((self.r2**2)*(self.r1**2))+((self.r2)*(self.r1**3))+(self.r1**4)) + \
                (self.height**3) * \
                    (((4)*(self.r2**2))+((2)*(self.r2*self.r1))+((2/3)*(self.r1**2))))

class Cone:
    def __init__(self, height, origin_radius, density) -> None:
        self.height = height #mm
        self.r1 = origin_radius #mm
        self.desnity = density #g/mm3

    def volume(self):
        return (1/3)*(math.pi)*(self.r1**2)*self.height

    def mass(self):
        return self.volume() * self.desnity

    def centre_of_mass(self):
        return self.height/4

    def moment_of_interia(self): #about the origin point on the base
        return self.desnity*self.volume()*(((3/20)*(self.r1**2))+((1/10)*(self.height**2)))
    
class Cuboid:
    def __init__(self, height, length, width) -> None:
        self.height = height #mm
        self.length = length #mm
        self.width = width #g/mm3

class Trapezoidal_Prism:
    pass

class Cylinder:
    pass