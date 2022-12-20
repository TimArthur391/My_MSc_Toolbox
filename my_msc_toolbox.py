import math

class Frustum:
#        tip_radius
#      ______________
#     /              \    ¦
#    /                \   ¦
#   /                  \  ¦ height
#  /____________________\ ¦
#       origin_radius

    def __init__(self, origin_radius, tip_radius, height, density) -> None:
        self.height = height #mm
        self.r1 = origin_radius #mm
        self.r2 = tip_radius #mm
        self.density = density #g/mm3

    def volume(self):
        return (self.height*(math.pi)/3)*((self.r1**2)+(self.r1*self.r2)+(self.r2**2))

    def mass(self):
        return self.volume() * self.density

    def centre_of_mass(self):
        return self.height*((self.r1**2)+(2*self.r1*self.r2)+(3*(self.r2**2))) / \
            4*((self.r1**2)+(self.r1*self.r2)+(self.r2**2))

    def moment_of_inertia(self): #about the origin point on the base
        return (1/20)*self.density*(math.pi)* \
        ((self.height) * \
            ((self.r2**4)+((self.r2**3)*(self.r1))+((self.r2**2)*(self.r1**2))+((self.r2)*(self.r1**3))+(self.r1**4)) + \
                (self.height**3) * \
                    (((4)*(self.r2**2))+((2)*(self.r2*self.r1))+((2/3)*(self.r1**2))))

class Hollow_Frustum:
    def __init__(self, origin_radius, tip_radius, height, density, wall_thickness) -> None:
        self.height = height #mm
        self.r1 = origin_radius #mm
        self.r2 = tip_radius #mm
        self.density = density #g/mm3
        self.thickness = wall_thickness #mm

class Cone:
    def __init__(self, height, origin_radius, density) -> None:
        self.height = height #mm
        self.r1 = origin_radius #mm
        self.density = density #g/mm3

    def volume(self):
        return (1/3)*(math.pi)*(self.r1**2)*self.height

    def mass(self):
        return self.volume() * self.density

    def centre_of_mass(self):
        return self.height/4

    def moment_of_inertia(self): #about the origin point on the base
        return self.density*self.volume()*(((3/20)*(self.r1**2))+((1/10)*(self.height**2)))
    
class Cuboid:
    def __init__(self, height, length, width, density) -> None:
        self.height = height #mm
        self.length = length #mm
        self.width = width #mm
        self.density = density #g/mm3

        # origin is at the centre of the base face

    def volume(self):
        return self.height * self.length * self.width

    def mass(self):
        return self.volume() * self.density

    def centre_of_mass(self):
        return self.length/2 

    def moment_of_inertia(self):
        pass

class Trapezoidal_Prism:
#        tip_length
#      ______________
#     /              \    ¦
#    /                \   ¦
#   /                  \  ¦ height
#  /____________________\ ¦
#       origin_length

    def __init__(self, origin_length, tip_length, height, depth, density) -> None:
        self.height = height #mm
        self.l1 = origin_length #mm
        self.l2 = tip_length #mm
        self.depth = depth #mm
        self.density = density #g/mm3

    def volume(self):
        pass

    def mass(self):
        return self.volume() * self.density

    def centre_of_mass(self):
        pass

    def moment_of_inertia(self):
        pass

class Cylinder:
    def __init__(self, diameter, length, density) -> None:
        self.diameter = diameter #mm
        self.length = length #mm
        self.density = density #g/mm3
        self.radius = diameter/2 #mm

    def volume(self):
        return math.pi * (self.radius**2) * self.length

    def mass(self):
        return self.volume() * self.density

    def centre_of_mass(self):
        return self.length/2

    def moment_of_inertia(self):
        pass

