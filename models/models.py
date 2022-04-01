from typing import Optional
from pydantic import BaseModel


class Planet(BaseModel):
    mass: Optional[str] = None 
    diameter: Optional[str] = None 
    density: Optional[str] = None
    gravity: Optional[str] = None
    escapevelocity: Optional[str] = None
    rotationperiod: Optional[str] = None
    len_of_day: Optional[str] = None
    distance_from_sun: Optional[str] = None
    perihelion: Optional[str] = None
    aphelion: Optional[str] = None
    orbitalperiod: Optional[str] = None
    orbitalinclination: Optional[str] = None
    orbitaleccentricity: Optional[str] = None
    obliquity: Optional[str] = None
    meantemp: Optional[str] = None
    surfacepressure: Optional[str] = None
    numofmoons: Optional[str] = None
    hasrings: Optional[str] = None
    hasmagneticfield: Optional[str] = None
