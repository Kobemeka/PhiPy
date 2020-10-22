"""knopy module - physics calculation functions

Users can calculate basic classic mechanical and electromagnetism calculations
"""

import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import cn
import space
import veop 
import units

def DistanceB2Object(FirstObject,SecondObject):
    """Calculate distance between two objects.

    Position of second object - position of first object. Returns Vector.

    Attributes
    ----------
    FirstObject: Object
        First object
    SecondObject: Object
        Second object
    """
    return veop.List2Vector(SecondObject.Position.numpy_array-FirstObject.Position.numpy_array)   
def Work(ForceVector,DisplacementVector):
    """Calculate the work done by a force that displace the object a distance.

    Returns Vector

    Attributes
    ----------
    ForceVector: Vector
        Applied force on the object
    DisplacementVector: Vector
        Displacement of the object
    """
    return veop.DotProduct(ForceVector,DisplacementVector)
def GravitationalForce(FirstObject,SecondObject):
    """Calculate the gravitational force act on second object applied by first object

    Returns Vector

    Attributes
    ----------
    FirstObject: Object
        First object
    SecondObject: Object
        Second object
    """
    gF = cn.G.Value * FirstObject.Mass * SecondObject.Mass / (DistanceB2Object(FirstObject,SecondObject).magnitude)**2

    vector = veop.List2Vector(gF * DistanceB2Object(SecondObject,FirstObject).unitVector().numpy_array)

    return vector
def GravPotential(Object,Point):
    return Object.mass * veop.DotProduct(Object.Space.Gravity,veop.RelativeVector(Point,Object.Position))
class Collision:
    def __init__(self,Object1,Object2):
        self.Object1 = Object1
        self.Object2 = Object2

    def Elastic(self):
        """Calculate final velocities of two object after an elastic collision 
        
        Returns Vector,Vector

        Attributes
        ----------
        Object1: Object
            First object of an elactic collision
        Object2: Object
            Second object of an elastic collision
        """
        RlV = veop.List2Vector(veop.RelativeVector(self.Object2.Velocity,self.Object1.Velocity).numpy_array)
        IMom = veop.List2Vector(self.Object1.Momentum.numpy_array+self.Object2.Momentum.numpy_array)
        
        O2fV = veop.List2Vector(IMom.numpy_array+RlV.numpy_array*self.Object1.Mass/(self.Object1.Mass+self.Object2.Mass))
        O1fV = veop.List2Vector(O2fV.numpy_array-RlV.numpy_array)
        return O1fV,O2fV
def CoulombsLaw(charge1,charge2):
    """Calculate electric force act on second charge applied by first charge 
    
    Returns Vector

    Attributes
    ----------
    charge1: Charge
        First charge
    charge2: Charge
        Second Charge
    """
    F = cn.k.Value * charge1.charge * charge2.charge / veop.RelativeVector(charge1.position,charge2.position).magnitude**2
    vector = veop.List2Vector(F * veop.RelativeVector(charge2.position,charge1.position).unitVector().numpy_array)
    return vector
def EField(charge,point):
    """Calculate electric field caused by a charge at a point
    
    Returns Vector

    charge: Charge
        Charge that cause electric field
    point: Vector
        Point in a 3-D space to calculate electric field
    """
    E = cn.k.Value * charge.charge / veop.RelativeVector(charge.position,point).magnitude**2
    vector = veop.List2Vector(E*veop.RelativeVector(point,charge.position).unitVector().numpy_array)
    return vector
def DipoleMoment(NegativeCharge,PositiveCharge):
    """Calculate the dipole moment of two charges

    Returns Vector

    Attribute
    ---------
    NegativeCharge: Charge
        Negative charge
    PositiveCharge: Charge
        Positive charge
    """
    return veop.List2Vector(PositiveCharge.charge * veop.RelativeVector(PositiveCharge.position,NegativeCharge.position).numpy_array)
#def DipoleMomentEField(DipoleMoment,Point):
    #return cn.k.Value * -1 * DipoleMoment.numpy_array / RelativeVector(Point,DipoleMoment.position).magnitude**3
def DipoleMomentTorque(DipoleMoment,EField):
    """Calculates components of torque of an dipole in an electric field and return a vector.

    Attributes
    ----------
    DipoleMoment: Vector
        Dipole moment of an dipole
    EField: Vector
        External electric field
    """
    return veop.CrossProduct(DipoleMoment,EField)
def DipoleMomentPotential(DipoleMoment,EField):
    """Calculates dipole moment potential energy of an dipole in an electric field.

    Returns int

    Attributes
    ----------
    DipoleMoment: Vector
        Dipole moment of an dipole
    EField: Vector
        External electric field
    """
    return -1*veop.DotProduct(DipoleMoment,EField)
def EPotential(Charge,Point):
    """Calculates electric potential energy of an charge at a point.

    Returns int

    Attributes
    ----------
    Charge: Charge
        A charge
    Point: Vector
        Point in a 3-D space
    """
    return cn.k.Value * Charge.charge / veop.RelativeVector(Charge.position,Point).magnitude
def EPotential2Charge(Charge1,Charge2):
    """Calculate potential energy that created by two charges

    Returns int

    Attribute
    ---------
    Charge1: Charge
        First charge
    Charge2: Charge
        Second charge
    """
    return cn.k.Value * Charge1.charge * Charge2.charge/ veop.RelativeVector(Charge1.position,Charge2.position).magnitude
def CParallel(capacitor1,capacitor2):
    """Connect two capacitor in parallel

    Returns PPCapacitor

    Attributes
    ----------
    capacitor1: PPCapacitor
        First capacitor
    capacitor2: PPCapacitor
        Second capacitor
    """
    return PPCapacitor(capacitor1.capacitance+capacitor2.capacitance)
def CSeries(capacitor1,capacitor2):
    """Connect two capacitor in series

    Returns PPCapacitor

    Attributes
    ----------
    capacitor1: PPCapacitor
        First capacitor
    capacitor2: PPCapacitor
        Second capacitor
    """
    sc = (1/capacitor1.capacitance)+(1/capacitor2.capacitance)
    ceq = 1/sc
    return PPCapacitor(ceq)
def RParallel(resistor1,resistor2):
    """Connect two resistor in parallel

    Returns Resistor

    Attributes
    ----------
    resistor1: Resistor
        First resistor
    resistor1: Resistor
        Second resistor
    """
    sr = (1/resistor1.resistance)+(1/resistor2.resistance)
    req = 1/sr
    return Resistor(req)
def RSeries(resistor1,resistor2):
    """Connect two resistor in series

    Returns Resistor

    Attributes
    ----------
    resistor1: Resistor
        First resistor
    resistor2: Resistor
        Second resistor
    """
    return Resistor(resistor1.resistance+resistor2.resistance)
class Draw:
    def __init__(self,o):
        self.o = o 
    def Forces(self):
        """Draws force vectors act on the object

        Attributes
        ----------
        o: Object
            Object
        """
        f = self.o.Forces
        nf = self.o.NetForce.components
        p = self.o.Position.components

        x=[p[0]]
        y=[p[1]]
        z=[p[2]]
        
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(p[0],p[1],p[2],c='#CC0033',marker='o',label="Object") #draw object
        
        colors=[]

        for i in range(len(f)):
            fi = f[i].components
            x.append(p[0]+fi[0])
            y.append(p[1]+fi[1])
            z.append(p[2]+fi[2])
            
            col = 1/len(f)
            r = [0,0.5,col*i]
            colors.append(r)

            ax.quiver(p[0],p[1],p[2],fi[0],fi[1],fi[2],colors=colors[i])
        
        x.append(p[0]+nf[0])
        y.append(p[1]+nf[1])
        z.append(p[2]+nf[2])

        ax.quiver(p[0],p[1],p[2],nf[0],nf[1],nf[2],colors='k',label="Net Force")
        
        ax.set_xlim3d(min(x),max(x))
        ax.set_ylim3d(min(y),max(y))
        ax.set_zlim3d(min(z),max(z))
        
        ax.set_xlabel('X axis')
        ax.set_ylabel('Y axis')
        ax.set_zlabel('Z axis')
        plt.legend()
        plt.show()

    def Trajectory(self,t,plot="scatter",anim=False,show_forces=False,type_of_force='net'):
        """Draws trajectory of the object between 0-t seconds

        Attributes
        ----------
        o: Object
            Object
        t: int
            Time
        """
        
        time_mult = 1
        
        p = self.o.Position.components

        fig = plt.figure()
        plt.get_current_fig_manager().window.state('zoomed')
        ax = fig.add_subplot(111, projection='3d')
        
        ax.scatter(p[0],p[1],p[2],c='#CC0033',marker='o',s=120*2,label="Object")
        ax.set_title('Trajectory of the object')
        ax.set_xlabel('X axis')
        ax.set_ylabel('Y axis')
        ax.set_zlabel('Z axis')
        if plot=="scatter":
            tx = []
            ty = []
            tz = []

            x,y,z=np.array([p[0]]),np.array([p[1]]),np.array([p[2]])
            
            for tt in range(1,t*time_mult):
                
                tx.append(self.o.Future("position",tt/time_mult).x) 
                ty.append(self.o.Future("position",tt/time_mult).y)
                tz.append(self.o.Future("position",tt/time_mult).z)
                if anim==True:
                    scat =ax.scatter(tx,ty,tz,c='black',s=50)
                    plt.pause(0.000001)
            tx=np.array(tx)
            ty=np.array(ty)
            tz=np.array(tz)
            self.o.Position = veop.Vector(tx,ty,tz)
            spcnt = np.zeros([3,len(tx)])
            space_center = veop.Vector(spcnt[0],spcnt[1],spcnt[2])
            scat =ax.scatter(tx,ty,tz,c=1e-3*self.o.Mass * veop.DotProduct(self.o.Space.Gravity,veop.RelativeVector(space_center,self.o.Position)),s=60,label='Trajectory',cmap="winter",alpha=1)
            x,y,z=np.append(x,tx),np.append(y,ty),np.append(z,tz)
            cbar = fig.colorbar(scat)
            cbar.set_label('Gravity Potential Energy (kJ)') 
            
            
            if show_forces == True:
                force_mult = 10
                f=self.o.Forces
                
                if type_of_force=='net' or type_of_force == 'all':
                    x=np.append(x,tx+self.o.NetForce.x*force_mult)
                    y=np.append(y,ty+self.o.NetForce.y*force_mult)
                    z=np.append(z,tz+self.o.NetForce.z*force_mult)
                    ax.quiver(tx,ty,tz,self.o.NetForce.x*force_mult,self.o.NetForce.y*force_mult,self.o.NetForce.z*force_mult,colors='black',label='F_net = ({}i,{}j,{}k)'.format(self.o.NetForce.x,self.o.NetForce.y,self.o.NetForce.z))
                if type_of_force=='gravity':
                    x=np.append(x,tx+self.o.Space.Gravity.x*force_mult)
                    y=np.append(y,ty+self.o.Space.Gravity.y*force_mult)
                    z=np.append(z,tz+self.o.Space.Gravity.z*force_mult)
                    
                    ax.quiver(tx,ty,tz,self.o.Space.Gravity.x*force_mult,self.o.Space.Gravity.y*force_mult,self.o.Space.Gravity.z*force_mult,colors='red',label='Gravity = ({}i,{}j,{}k)'.format(self.o.Space.Gravity.x,self.o.Space.Gravity.y,self.o.Space.Gravity.z))
                    # ax.quiver(tx,ty,tz,1,1,1)
                
                if type_of_force=='diff' or type_of_force == 'all':
                    colors=[]
                    fx,fy,fz=[],[],[]
                    
                    for i in range(len(f)):
                        fi = f[i].components
                        

                        fx.append(fi[0])
                        fy.append(fi[1])
                        fz.append(fi[2])
                        
                        
                        col = 1/len(f)
                        r = [0,0.5,col*i]
                        colors.append(r)
                    fx=np.array(fx)
                    fy=np.array(fy)
                    fz=np.array(fz)
                    for q in range(len(f)):
                        x=np.append(x,tx+fx[q]*force_mult)
                        y=np.append(y,ty+fy[q]*force_mult)
                        z=np.append(z,tz+fz[q]*force_mult)
                        fmax = max([abs(fx[q]),abs(fy[q]),abs(fz[q])])
                        qui_col = [ abs(fx[q])/fmax , abs(fy[q])/fmax , abs(fz[q])/fmax]
                        qui_col = np.array(qui_col)
                        qui_col = qui_col/2
                        ax.quiver(tx,ty,tz,fx[q]*force_mult,fy[q]*force_mult,fz[q]*force_mult,colors=qui_col,label='force {} = ({}i,{}j,{}k)'.format(q,fx[q],fy[q],fz[q]))
                        
                # print(x)
                ax.set_xlim3d(min(x),max(x))
                ax.set_ylim3d(min(y),max(y))
                ax.set_zlim3d(min(z),max(z))
            
            plt.legend(loc=8,ncol=5)
            plt.show()
        if plot=="line":
            tx =[]
            ty=[]
            tz=[]
            
            
            for tt in range(1,t*10):

                # col = 1/t
                # r = [0,0,1-col*tt]
                # colors.append(r)

                tx.append(self.o.Future("position",tt*.1).components[0]) 
                ty.append(self.o.Future("position",tt*.1).components[1])
                tz.append(self.o.Future("position",tt*.1).components[2])
            ax.plot(tx,ty,tz,color="red",label='Trajectory',linewidth=5)
            
            plt.legend()
            plt.show()



class Space:
    """Create a Space

    Attributes
    ----------
    Gravity: Vector
        A vector. Gravity of the space.
    """
    def __init__(self,Gravity):
        self.Gravity = Gravity
        
class Object:
    """It creates an object.
    
    This class create an object in a space with mass and moment of inertia at a position. 
    . . .

    Attributes
    ----------
    Space: Space
        Space
    Mass: int
        Mass of the object
    MomentOfInertia: int
        Moment of inertia of the object
    Position: Vector
        Position of the object
    Radius: int
        Radius of the object.
    Forces: list
        All applied forces on the object. Initially the gravitational force is included.
    Velocity: Vector
        Initial velocity of the object
    AngularVelocity: Vector
        Angular velocity of the object
    GravityPotentialEnergy: int
        Gravitational Potential Energy of the object
    NetForce: Vector
        Net force that applied on the object
    Acceleration: Vector
        Acceleration of the object
    
    """
    def __init__(self,Space,Mass,MomentOfInertia,Position):
        self.Space = Space 
        self.Mass = Mass
        self.MomentOfInertia = MomentOfInertia
        self.Position = Position
        self.Radius = math.sqrt(self.MomentOfInertia / self.Mass)
        self.Forces = np.array([veop.List2Vector(self.Mass * self.Space.Gravity.numpy_array)])
        self.ForceDistances = []
        self.Torques = [veop.Vector(0,0,0)]
        self.Velocity = veop.Vector(0,0,0)
        self.AngularVelocity = veop.List2Vector(self.Radius * self.Velocity.numpy_array)
        self.Momentum = veop.List2Vector(self.Mass * self.Velocity.numpy_array)
        self.LinearKineticEnergy = 0.5 * self.Mass * self.Velocity.magnitude ** 2 
        self.AngularKineticEnergy = 0.5 * self.MomentOfInertia * self.AngularVelocity.magnitude
        self.GravityPotentialEnergy = self.Mass * veop.DotProduct(self.Space.Gravity,self.Position)
        self.NetForce = self.Space.Gravity
        self.NetTorque = veop.Vector(0,0,0)
        self.Acceleration = veop.List2Vector(self.NetForce.numpy_array/self.Mass)
        
    def Add(self,VectorType,Vector,DVector=None):
        """Add a Vector to the object.
        
        ...

        Attributes
        ----------
        VectorType: str
            Type of the adding Vector. 'force' or 'velocity'. 
        Vector: Vector
            A vector which will be added to the object
        DVector: Vector
            A vector which is the position vector of added force. (Default None)
        """
        if str(VectorType) == "force":
            self.Forces=np.append(self.Forces,Vector)
            self.ForceDistances=np.append(self.ForceDistances,DVector)
            self.Torques=np.append(self.Torques,veop.CrossProduct(DVector,Vector))
        elif str(VectorType) == "velocity":
            self.Velocity = Vector
        
        self.NetForce = veop.VectorAddition(self.NetForce,self.Forces[-1])
        self.Acceleration = veop.List2Vector(self.NetForce.numpy_array/self.Mass)
        self.NetTorque = veop.MultiVectorAddition(self.Torques)
        self.AngularVelocity = veop.List2Vector(self.Radius * self.Velocity.numpy_array)
        self.Momentum = veop.List2Vector(self.Mass * self.Velocity.numpy_array)
        self.LinearKineticEnergy = 0.5 * self.Mass * self.Velocity.magnitude
        self.AngularKineticEnergy = 0.5 * self.MomentOfInertia * self.AngularVelocity.magnitude

    def DeleteList(self,VectorList):
        """Delete all elements in a list of the object
            
        This function delete all elements in a list.

        ...

        Attributes
        ----------
        VectorList: list
            Only 'force'
        """
        if str(VectorList) == "force":
            self.Forces = np.delete(self.Forces,0,axis=0)
    def Future(self,Type,Time):
        """Calculate future attributes

        This function calculate future velocity or position of the object at a specific time.

        Attributes
        ----------
        Type: str
            'velocity' or 'position'
        Time: int
            Time that the function calculate velocity or position of the object, in second.
        """
        if str(Type) == "velocity":
            return veop.List2Vector(self.Velocity.numpy_array + self.Acceleration.numpy_array*Time)
        elif str(Type) == "position":
            return veop.List2Vector(self.Position.numpy_array + self.Velocity.numpy_array*Time + 0.5 * self.Acceleration.numpy_array * Time* Time)
class Charge:
    """Create a charge

    Attributes
    ----------
    charge: int
        charge value of the Charge
    position: Vector
        position of the charge
    """
    def __init__(self,charge,position):
        self.charge = charge
        self.position = position
# class Spring:
#     """Create a spring

#     A simple pendulum that have one or two objects (default 1 object)

#     Attributes
#     ----------
#     SpringConstant: int
#         spring constant of the spring (k)
#     FirstObject: Object
#         An object 
#     SecondObject: Object
#         default position (0,0,0)
#     """
#     def __init__(self,SpringConstant,FirstObject,SecondObject=Object(Space(veop.Vector(0,0,10)),1,1,veop.Vector(0,0,0))):
#         self.SpringConstant=SpringConstant
#         self.FirstObject = FirstObject
#         self.SecondObject = SecondObject
#         self.Potential = 0

#     def Compress(self,FirstObjectFinalPosition,SecondObjectFinalPosition=veop.Vector(0,0,0)):
#         """Compress spring

#         Returns int. Calculate the potential after compress.

#         Attributes
#         ----------
#         FirstObjectFinalPosition: Vector
#             Final position of the first object
#         SecondObjectFinalPosition: Vector
#             Final position of the first object (default (0,0,0))
#         """
#         self.Potential =  0.5 * self.SpringConstant * veop.List2Vector(veop.RelativeVector(FirstObjectFinalPosition,self.FirstObject.Position).numpy_array-veop.RelativeVector(SecondObjectFinalPosition,self.SecondObject.Position).numpy_array ).magnitude**2       
class Pendulum:
    """Create a pendulum

    Calculate Period

    Attributes
    ----------
    Object: Object
        An object
    RopeLength: int
        Length of the rope
    Period: int
        Period of the pendulum
    """
    def __init__(self,Object,RopeLength):
        self.Object = Object
        self.RopeLength = RopeLength
        self.Period = 2* math.pi * np.sqrt(self.RopeLength/self.Object.Space.Gravity.magnitude)
class ParallelPlate:
    """Create a parallel plate

    Calculate the capacitance

    Attributes
    ----------
    epsilon: int
        epsilon
    area: int
        area of the plates
    distance: int
        distance between the plates
    capacitance: int
        capacitance of the parallel plates
    """
    def __init__(self,epsilon,area,distance):
        self.epsilon = epsilon
        self.area = area
        self.distance = distance
        self.capacitance = self.epsilon * self.area / self.distance
class PPCapacitor:
    """Create a parallel plate capacitor

    Attributes
    ----------
    capacitance: int
        capacitance of the capacitor
    voltage: int
        voltage of the capacitor (default None)
    charge: int
        charges that passes on the capacitor (default None)
    """
    def __init__(self,capacitance,voltage=None,charge=None):
        self.capacitance = capacitance
        self.voltage = voltage
        self.charge = charge      
class Resistor:
    """Create a resistor

    Attributes
    ----------
    resistance: int
        resistance of the resitor
    voltage: int
        voltage of the resitor (default None)
    current: int
        current that passes on the resistor (default None)
    """
    def __init__(self,resistance,voltage=None,current=None):
        self.resistance = resistance
        self.voltage = voltage
        self.current = current