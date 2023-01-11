import math

class Cone:
    def __init__(self, height, origin_radius, density) -> None:
        self.height = height #mm
        self.r1 = origin_radius #mm
        self.density = density #g/mm3

    def volume(self): #CAD verified
        return (1/3)*(math.pi)*(self.r1**2)*self.height

    def mass(self): #CAD verified
        return self.volume() * self.density

    def centre_of_mass(self): #CAD verified
        '''distance above the centre of the base plate'''
        return self.height/4

    def moment_of_inertia_1(self): #CAD verified
        '''about the origin point on the base'''
        return self.density*self.volume()*(((3/20)*(self.r1**2))+((1/10)*(self.height**2)))

    def moment_of_inertia_CoM(self): #CAD verified
        '''about its centre of mass'''
        return self.mass() * (((3/20)*(self.r1**2))+((3/80)*(self.height**2)))
    
class Cuboid:
    def __init__(self, height, length, width, density) -> None:
        self.height = height #mm
        self.length = length #mm
        self.width = width #mm
        self.density = density #g/mm3

    def volume(self):
        return self.height * self.length * self.width

    def mass(self): #CAD confirmed
        return self.volume() * self.density

    def centre_of_mass(self): 
        return self.length/2 

    def moment_of_inertia_1(self): #CAD confirmed 
        '''rotation about length, at the centre of the width-length face'''        
        # ______¦______
        #|      ¦      |
        #|      ¦      | length
        #|______¦______|
        #   <-width->  
        
        return self.mass() * (0.25*(self.height**2) + (1/12)*((self.width**2) + (self.height**2))) #CAD confirmed

    def moment_of_inertia_2(self): #CAD confirmed
        ''' rotation about length, at the edge of the width-length face'''
        # ____________¦
        #|            ¦
        #|            ¦ length
        #|____________¦
        #   <-width-> ¦
        
        return self.mass() * ((1/3)*((self.width**2) + (self.height**2)))

    def moment_of_inertia_CoM(self): #CAD confirmed
        '''about the centre of mass passing through the centre of the width and height planes'''
        # ______¦______
        #|      ¦      |
        #|      ¦      | length
        #|______¦______|
        #   <-width->  
        
        return self.mass() * (1/12) * ((self.width**2)+(self.height**2)) 

class Triangular_prism__right_angled:
    '''
       |\
       | \       ^
       |  \   height
       |___\     v
       length  
    '''

    def __init__(self, height, length, width, density):
        self.height = height
        self.length = length
        self.width = width
        self.density = density

    def volume(self):
        return 0.5*self.height*self.length*self.width

    def mass(self): #CAD confirmed
        return self.density*self.volume()

    def centre_of_mass(self): #have a think about how this could be most useful
        '''From the right angled edge on the middle plane'''
        return (((self.length/3)**2) + ((self.height/3)**2))**0.5

    def moment_of_inertia_1(self): #CAD confirmed
        '''Rotating about the right angled edge'''
        return self.mass()*(1/6)*((self.length**2)+(self.height**2))

    def moment_of_inertia_CoM(self): #CAD confirmed
        '''Rotating about the centre of mass - right angled edge direction'''
        return self.mass()*(1/18)*((self.length**2)+(self.height**2))

class Cylinder:
    def __init__(self, diameter, length, density) -> None:
        self.diameter = diameter #mm
        self.length = length #mm
        self.density = density #g/mm3
        self.radius = diameter/2 #mm

    def volume(self):
        return math.pi * (self.radius**2) * self.length

    def mass(self): #CAD confirmed
        return self.volume() * self.density

    def centre_of_mass(self): #CAD confirmed
        '''from the base'''
        return self.length/2

    def moment_of_inertia_CoM(self): #CAD confirmed
        '''rotating along one of its cross-sectional axes at the centre of mass'''
        return self.mass() * (1/12) * ((3*(self.radius**2))+(self.length**2))


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

    def area(self):
        return (self.l1 + self.l2) * (self.height / 2)

    def volume(self):
        return (self.l1 + self.l2) * (self.height / 2) * self.depth

    def mass(self):
        return self.volume() * self.density

    def centre_of_mass(self): # centre of the depth plane
        return self.height*((self.l1**2)+(2*self.l1*self.l2)+(3*(self.l2**2))) / \
            4*((self.l1**2)+(self.l1*self.l2)+(self.l2**2))

    def moment_of_inertia_centre_face(self):
        return ((self.depth * self.density) / 12) * \
            (self.height * ((((self.l2 - self.l1)**3)/4) + ((self.l2 - self.l1)**2) + ((3/2)*(self.l1**2)*(self.l2)) - ((self.l1**3)/2)) + \
                (self.height ** 3)*((3 * self.l2) + (self.l1)))
