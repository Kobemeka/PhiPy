import numpy as np
import math 

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
class Vector:
    """Create a Vector

    Create a Vector in 3-D. 

    Attributes
    ----------
    x: int
        x component of the vector
    y: int 
        y compononet of the vector
    z: int
        z component of the vector
    magnitude: int
        magnitude of the vector
    components: tuple
        components of the vector
    numpy_array: list
        components of the vector in a numpy array
    """
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
        self.magnitude = np.sqrt((self.x**2)+(self.y**2)+(self.z**2))
        self.components = x,y,z
        self.numpy_array = np.array([self.x,self.y,self.z])
        #self.unit_vector = self.numpy_array/self.magnitude

    def xyz(self):
        """Return numpy array of x, y and z component of the vector """
        return np.array([self.x,self.y,self.z])
    def unitVector(self):
        """A Vector. Return unit vector of the vector."""
        return List2Vector(self.numpy_array/self.magnitude)
    def sum_(self):
        return sum(self.components)
    def multip(self):
        return self.x*self.y*self.z
    def show(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.quiver(0,0,0,self.x,self.y,self.z) 
        ax.set_xlim3d(-self.x,self.x)
        ax.set_ylim3d(-self.y,self.y)
        ax.set_zlim3d(-self.z,self.z)
        plt.show() 

def VectorAddition(v,u):
    """Add two vectors each other.

    Returns a Vector 
    
    Attributes
    ----------
    v: Vector
        First vector for addition
    u: Vector
        Second vector for addition
    """
    return List2Vector(u.numpy_array+v.numpy_array)
def RelativeVector(v,u):
    """Return a Vector which vector u relative to vector v (u-x)

    Attrributes
    -----------
    v: Vector
        First vector 
    u: Vector
        Second vector 
    """
    return List2Vector(u.numpy_array-v.numpy_array)
def MultiVectorAddition(VectorList):
    """Sum all vectors in a list and return a vector

    Attrributes
    -----------
    VectorList: list
        A list that contains Vectors
    """
    m = []
    for mva in range(len(VectorList)):
        m.append(VectorList[mva].numpy_array)
    m = sum(m)
    return Vector(m[0],m[1],m[2])
def List2Vector(VectorList):
    """Convert numpy array that contains 3 int elements  to Vector
    
    Attributes
    ----------
    VectorList: numpy array
        numpy array which has 3 int elements.
    """ 
    return Vector(VectorList[0],VectorList[1],VectorList[2])
def Angle(v,u):
    """Find an angle between two Vectors.

    Attributes
    ----------
    u: Vector
        First Vector
    v: Vector
        Second Vector
    """
    return math.acos((v.x*u.x + v.y*u.y + v.z*u.z)/(v.magnitude*u.magnitude))
def DotProduct(v,u):
    """Dot product of two vectors

    Returns int

    Attributes
    ----------
    v: Vector
        First Vector
    u: Vector
        Second Vector
    """
    return v.x*u.x + v.y*u.y + v.z*u.z
def CrossProduct(v,u):
    """Cross product of two vectors

    Returns Vector

    Attributes
    ----------
    v: Vector
        First Vector
    u: Vector
        Second Vector
    """
    x = v.y*u.z - v.z*u.y
    y = -v.x*u.z + v.z*u.x
    z = v.x*u.y - v.y*u.x
    return Vector(x,y,z)
def Projection(v,u):
    """Projection of first vector to second vector

    Returns Vector

    Attributes
    ----------
    v: Vector
        First Vector
    u: Vector
        Second Vector
    """
    s = DotProduct(v,u)/(u.magnitude**2)
    return Vector(u.x*s,u.y*s,u.z*s)
def Volume(v,u,w):
    """Calculate volume of solid created by three vectors.

    Returns int

    Attributes
    ----------
    v: Vector
        First Vector
    u: Vector
        Second Vector
    w: Vector
        Third Vector
    """
    return abs(DotProduct(CrossProduct(v,u), w))