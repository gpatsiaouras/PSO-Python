import numpy as np
from particle import Particle
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


class PSO:
    def __init__(self, number_of_particles, iterations, lower_bound, upper_bound):

        # Initialize coefficients and constants
        self.iterations = iterations

        # Variables about gbest
        self.evaluation_of_global_position = float('inf')
        self.global_position = np.array([np.random.random() * 50, np.random.random() * 50])

        # Bounds
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound

        # Initialize particles
        self.particles = [Particle(self.lower_bound, self.upper_bound) for n in range(number_of_particles)]
        for particle in self.particles:
            if particle.evaluation_of_best_position() < self.evaluation_of_global_position:
                self.global_position = particle.best_position
                self.evaluation_of_global_position = particle.evaluation_of_best_position()
            particle.initialize_velocity()

    def run(self):
        # Plot Interactive mode on
        plt.ion()
        # Initiate the figure and add subplot
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        for iteration in range(self.iterations):
            X = []
            Y = []
            Z = []
            for particle in self.particles:
                # For the plot
                X.append(particle.position[0])
                Y.append(particle.position[1])
                Z.append(particle.evaluation_of_current_position())

                particle.update_velocity(self.global_position)
                particle.move_to_new_position()
                if particle.evaluation_of_current_position() < particle.evaluation_of_best_position():
                    particle.best_position = particle.position
                    if particle.evaluation_of_best_position() < self.evaluation_of_global_position:
                        self.evaluation_of_global_position = particle.evaluation_of_best_position()
                        self.global_position = particle.best_position

            # Clean figure
            ax.cla()
            # Redeclare axes
            sc = ax.scatter(np.array(X), np.array(Y), np.array(Z))
            # Limit axis to the bounds and limit evaluation to 10
            ax.set_xlim([self.lower_bound, self.upper_bound])
            ax.set_ylim([self.lower_bound, self.upper_bound])
            ax.set_zlim([0, 10])
            # Redraw and pause
            fig.canvas.draw()
            plt.pause(0.01)

            if not iteration % 10:
                print("Iteration " + str(iteration))
        print("Best position is on [%f, %f] with value %f" % (self.global_position[0], self.global_position[1], self.evaluation_of_global_position))


if __name__ == '__main__':

    # Define variables of Particle Swarm Optimization
    number_of_particles = 10
    iterations = 100
    lower_bound = 0
    upper_bound = 4

    # Execute PSO
    pso = PSO(number_of_particles, iterations, lower_bound, upper_bound)
    pso.run()
