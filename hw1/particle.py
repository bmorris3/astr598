"""
ASTR 598 HW 1
Brett Morris
"""

import astropy.units as u
from astropy.constants import G
import numpy as np


class Position(object):
    @u.quantity_input(x=u.m, y=u.m, z=u.m)
    def __init__(self, x, y, z):
        """
        Position of a particle

        Parameters
        ----------
        x : `astropy.units.Quantity`
            X position in meters

        y : `astropy.units.Quantity`
            Y position in meters

        z : `astropy.units.Quantity`
            Z position in meters
        """
        self.x = x
        self.y = y
        self.z = z


class Velocity(object):
    @u.quantity_input(vx=u.m/u.s, vy=u.m/u.s, vz=u.m/u.s)
    def __init__(self, vx, vy, vz):
        """
        Velocity of a particle.

        Parameters
        ----------
        vx : `astropy.units.Quantity`
            X velocity in meters/sec

        vy : `astropy.units.Quantity`
            Y velocity in meters/sec

        vz : `astropy.units.Quantity`
            Z velocity in meters/sec
        """
        self.vx = vx
        self.vy = vy
        self.vz = vz


class Particle(object):
    @u.quantity_input(mass=u.kg)
    def __init__(self, mass, position, velocity):
        """
        Define a particle with a mass, position, velocity.

        Parameters
        ----------
        mass : `astropy.units.Quantity`
            Mass of the particle

        position : `Position`
            Position object for the particle

        velocity : `Velocity`
            Velocity object for the particle
        """
        self.mass = mass
        self.position = position
        self.velocity = velocity

    @staticmethod
    def force(particle1, particle2):
        """
        Calculate the gravitational force between two particles.

        Parameters
        ----------
        particle1 : `Particle`
            A particle

        particle2 : `Particle`
            Another particle

        Returns
        -------
        force : `astropy.units.Quantity`
            Grativational force between the two particles.
        """
        position1 = particle1.position
        position2 = particle2.position

        distance_12 = np.sqrt((position1.x - position2.x)**2 +
                              (position1.y - position2.y)**2 +
                              (position1.z - position2.z)**2)

        return G*particle1.mass*particle2.mass/distance_12**2
