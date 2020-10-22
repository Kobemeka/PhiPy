"""knopy module physics constants

In this script, some of most used physical constants' values, names and units are defined.
"""
import math

class Constant:
    """Physical Constants.

    This class defines a new constant with value, name and unit.

    Attributes
    ----------
    Value: int
        Value of the constant.
    Name: str
        Name of the constant.
    Unit: str
        Unit of the constant
    """
    def __init__(self, Value,Name,Unit):
        self.Value = Value
        self.Name = Name
        self.Unit = Unit


c = Constant(299792458,"speed of light in a vacuum","m/s")
G = Constant(6.67430E-11,"gravitational constant","N * m^2 / kg^2")
h = Constant(6.62607015E-34,"planck constant","J*s")
hc = Constant(1.986445857E-25,"hc","J*m")
hBar = Constant(1.054571817E34,"reduced planck constant/dirac constant","J*s")
e0 = Constant(8.8541878128E-12,"electric constant/permitivitty of free space/vacuum permitivitty","C^2 / N * m^2")
Na = Constant(6.02214076E23,"avogadro constant","1/mol")
me = Constant(9.1093837015E-31,"mass of electron","kg")
mp = Constant(1.67262192369E-27,"mass of proton","kg")
mn = Constant(1.67492749804E-27,"mass of neutron","kg")
g = Constant(9.80665,"standard gravity","m/s^2")


k = Constant(1/(4* e0.Value * math.pi),"coulomb's law constant","N * m^2 / C^2")