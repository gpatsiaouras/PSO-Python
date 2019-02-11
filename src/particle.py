import numpy as np

# Constants
w = 0.5
c1 = 0.5
c2 = 0.5

class Particle:
    def __init__(self, dimensions, lower_bound, upper_bound):
        # Initialize the particle's position with a uniformly distributed random vector
        self.position = np.random.uniform(lower_bound, upper_bound, dimensions)  # assign random possition
        # Initialize the particle's best known position to its initial position
        self.best_position = self.position
        self.velocity = np.array([0, 0])

    def rosenbrock(self, x, y):
        return (1 - x) ** 2 + 100 * ((y - x ** 2)) ** 2

    def evaluation_of_current_position(self):
        return self.rosenbrock(self.position[0], self.position[1])

    def evaluation_of_best_position(self):
        return self.rosenbrock(self.best_position[0], self.best_position[1])

    def move_to_new_position(self):
        global w
        global c1
        global c2
        # Get random numbers
        rx = np.random.uniform(0, 1)
        ry = np.random.uniform(0, 1)

        # calculate new velocity
        self.velocity = w * self.velocity + c1 * rx
        # TODO Do magic and move it to another position
        #       for each dimension d = 1, ..., n do
        #          Pick random numbers: rp, rg ~ U(0,1)
        #          Update the particle's velocity: vi,d ← ω vi,d + φp rp (pi,d-xi,d) + φg rg (gd-xi,d)
        #       Update the particle's position: xi ← xi + vi
        pass

    def update_velocity(self):
        pass

    def initialize_velocity(self):
        pass
