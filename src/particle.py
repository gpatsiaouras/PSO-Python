import numpy as np
import math

# Constants
a = 0.4
b = 2.0
c = 2.0


class Particle:
    def __init__(self, lower_bound, upper_bound):
        # Assign local variables
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound

        # Initialize the particle's position with a uniformly distributed random vector
        self.position = np.random.uniform(lower_bound, upper_bound, 2)  # assign random possition

        # Initialize the particle's best known position to its initial position
        self.best_position = self.position
        self.velocity = np.array([0, 0])

    def rosenbrock(self, x, y):
        return (1 - x) ** 2 + 100 * ((y - x ** 2)) ** 2

    def rastrigin(self, x, y):
        return 0 - (10 * 2 + (x ** 2 - (10 * np.cos(2 * np.pi * x))) + (y ** 2 - (10 * np.cos(2 * np.pi * y))))

    def evaluation_of_current_position(self):
        return self.rosenbrock(self.position[0], self.position[1])
        # return self.rastrigin(self.position[0], self.position[1])

    def evaluation_of_best_position(self):
        return self.rosenbrock(self.best_position[0], self.best_position[1])
        # return self.rastrigin(self.position[0], self.position[1])

    def move_to_new_position(self):
        self.position = self.position + self.velocity

        # new_position = self.position + self.velocity
        # if self.lower_bound <= new_position[0] <= self.upper_bound \
        #         and self.lower_bound <= new_position[1] <= self.upper_bound:
        #     self.position = new_position

    def update_velocity(self, global_best_position):
        global a
        global b
        global c

        # calculate new velocity
        self.velocity = a * self.velocity + (b * np.random.uniform(0, 1)) * (
                    self.best_position - self.position) + (c * np.random.uniform(0, 1)) * (
                                       global_best_position - self.position)

    def initialize_velocity(self):
        abs_diff = np.fabs(self.lower_bound - self.upper_bound)
        self.velocity = np.random.uniform(-abs_diff, abs_diff, 2)
