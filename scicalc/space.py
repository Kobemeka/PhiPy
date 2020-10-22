"""knopy module - some space objects

In this script, some of solar planets' characteristics are defined.
"""

class Planet:
    """Defines a planet.

    Attributes
    ----------
    Aphelion: int
        Aphelion distance of the planet
    Perihelion: int
        Perihelion dinstance of the planet
    SemiMajorAxis: int
        Semi major axis of the planet
    Eccentiricity: int
        Eccentiricity of the orbit
    OrbitalPeriod: int
        Period of the planet
    AverageOrbitalSpeed: int
        Average orbital speed of the planet
    MeanRadius: int
        Mean radius of the planet
    EquatorialRadius: int
        Equatorial radius of the planet
    PolarRadius: int
        Polar radius of the planet
    Circumference: int
        Circumference of the planet
    SurfaceArea: int
        Surface area of the planet
    Volume: int
        Volume of the planet
    Mass: int
        Mass of the planet
    SurfaceGravity: int
        Surface gravity of the planet
    EscapeVelocity: int
        Escape velocity of the planet
    """
    def __init__(self,Aphelion,Perihelion,SemiMajorAxis,Eccentricity,OrbitalPeriod,AverageOrbitalSpeed,MeanRadius,EquatorialRadius,PolarRadius,Circumference,SurfaceArea,Volume,Mass,SurfaceGravity,EscapeVelocity):
        self.Aphelion = Aphelion
        self.Perihelion = Perihelion
        self.SemiMajorAxis = SemiMajorAxis
        self.Eccentricity = Eccentricity
        self.OrbitalPeriod = OrbitalPeriod
        self.AverageOrbitalSpeed = AverageOrbitalSpeed
        self.MeanRadius = MeanRadius
        self.EquatorialRadius = EquatorialRadius
        self.PolarRadius = PolarRadius
        self.Circumference = Circumference
        self.SurfaceArea = SurfaceArea
        self.Volume = Volume
        self.Mass = Mass
        self.SurfaceGravity = SurfaceGravity
        self.EscapeVelocity = EscapeVelocity
class Star:
    """Defines a star.

    Attributes
    ----------
    EquatorialRadius: int
        Equatorial radius of the star
    Circumference: int
        Circumference of the star
    SurfaceArea: int
        Surface area of the star
    Volume: int
        Volume of the star
    Mass: int
        Mass of the star
    SurfaceGravity: int
        Surface gravity of the star
    EscapeVelocity: int
        Escape velocity of the star
    """
    def __init__(self,EquatorialRadius,Circumference,SurfaceArea,Volume,Mass,SurfaceGravity,EscapeVelocity):
        self.EquatorialRadius = EquatorialRadius
        
        self.Circumference = Circumference
        self.SurfaceArea = SurfaceArea
        self.Volume = Volume
        self.Mass = Mass
        self.SurfaceGravity = SurfaceGravity
        self.EscapeVelocity = EscapeVelocity

Earth = Planet(1.528E11,1.47095E11,1.49598023e11,0.0167086,31558149.7635,29780,6371e3,6378.1e3,6356.8e3,40075.017e3,510072000e6,1.08321E+21,5.97237e24,9.80665,11.186e3)
Sun = Star(695700e3,4.379e9,6.09e15,1.41e27,1.9884e30,274,617.7e3)