"""
ASTR 598 HW 1
Brett Morris
"""

from particle import Particle, Position, Velocity
import astropy.units as u

# Define properties of first particle
position1 = Position(1*u.m, 0*u.m, 0*u.m)
velocity1 = Velocity(0.1*u.m/u.s, 0*u.m/u.s, 0*u.m/u.s)
particle1 = Particle(10*u.kg, position1, velocity1)

# Define properties of second particle
position2 = Position(-1*u.m, 0*u.m, 0*u.m)
velocity2 = Velocity(-0.1*u.m/u.s, 0*u.m/u.s, 0*u.m/u.s)
particle2 = Particle(10*u.kg, position2, velocity2)

gravitational_force = Particle.force(particle1, particle2)

print("Gravitational force between particles: {0}".format(gravitational_force))
