import numpy
from particle import Particle


class PSO:
    def __init__(self, number_of_particles, dimensions, iterations):

        # Initialize coefficients and constants
        self.iterations = iterations
        self.dimensions = dimensions
        self.evaluation_of_global_position = float('inf')
        self.lower_bound = 0
        self.upper_bound = 4

        # TODO this is not yet implemented
        #  for each particle i = 1, ..., S do
        #    Initialize the particle's position with a uniformly distributed random vector: xi ~ U(blo, bup)
        #    Initialize the particle's best known position to its initial position: pi ← xi
        #    if f(pi) < f(g) then
        #        update the swarm's best known  position: g ← pi
        #    Initialize the particle's velocity: vi ~ U(-|bup-blo|, |bup-blo|)

        # Initialize particles
        self.particles = [Particle(dimensions, self.lower_bound, self.upper_bound) for n in range(number_of_particles)]
        for particle in self.particles:
            if particle.evaluation_of_best_position() < self.evaluation_of_global_position:
                self.global_position = particle.best_position
                self.evaluation_of_global_position = particle.evaluation_of_best_position()
            particle.initialize_velocity()

    def run(self):
        for iteration in self.iterations:
            for particle in self.particles:
                # more stuff
                particle.move_to_new_position()
                if particle.evaluation_of_current_position() < particle.evaluation_of_best_position():
                    particle.best_position = particle.position
                    if particle.evaluation_of_best_position() < self.evaluation_of_global_position:
                        self.evaluation_of_global_position = particle.evaluation_of_best_position()
                        self.global_position = particle.best_position


if __name__ == '__main__':

    # Define variables of Particle Swarm Optimization
    number_of_particles = 200
    dimensions = 2
    iterations = 1000

    # Execute PSO
    pso = PSO(number_of_particles, dimensions, iterations)
    pso.run()


# while a termination criterion is not met do:
#    for each particle i = 1, ..., S do
#       for each dimension d = 1, ..., n do
#          Pick random numbers: rp, rg ~ U(0,1)
#          Update the particle's velocity: vi,d ← ω vi,d + φp rp (pi,d-xi,d) + φg rg (gd-xi,d)
#       Update the particle's position: xi ← xi + vi
#       if f(xi) < f(pi) then
#          Update the particle's best known position: pi ← xi
#          if f(pi) < f(g) then
#             Update the swarm's best known position: g ← pi
