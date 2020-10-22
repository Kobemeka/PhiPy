def convert_units(typ,constant,f,t):
    """Converts units

    type should be one of them
    'metric','time'

    f and t should be one of them:
    
    'pico','nano','micro','mili','centi','deci','base','deca','hecta','kilo','mega','giga','tera'

    Attributes
    ----------
    constant: int
        constant number
    f: str
        converting unit
    t: str
        converted unit
    """
    
    units = {'pico':1e-12,'nano':1e-9,'micro':1e-6,'mili': 1e-3,'centi':1e-2,'deci':1e-1,
            'base':1,
            'deca':1e1,'hecta':1e2,'kilo':1e3,'mega':1e6,'giga':1e9,'tera':1e12}
    return constant*units.get(f)/units.get(t)