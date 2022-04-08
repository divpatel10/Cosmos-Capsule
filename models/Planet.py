from typing import Optional
from pydantic import BaseModel

class Planet(BaseModel):
    mass: Optional[float] = None
    diameter: Optional[float] = None 
    density: Optional[float] = None
    gravity: Optional[float] = None
    escapevelocity: Optional[float] = None
    rotationperiod: Optional[float] = None
    len_of_day: Optional[float] = None
    distance_from_sun: Optional[float] = None
    perihelion: Optional[float] = None
    aphelion: Optional[float] = None
    orbitalperiod: Optional[float] = None
    orbitalinclination: Optional[float] = None
    orbitaleccentricity: Optional[float] = None
    obliquity: Optional[str] = None
    meantemp: Optional[float] = None
    surfacepressure: Optional[str] = None
    numberofmoons: Optional[int] = None
    ringsystem: Optional[str] = None
    hasmagneticfield: Optional[str] = None
