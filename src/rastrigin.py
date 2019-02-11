# From
# https://gist.github.com/miku/fca6afe05d65302f14c2b6f5242458d6

from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import math
import matplotlib.pyplot as plt
import numpy as np


class RastriginWrapper:
    def __init__(self, lower_bound, upper_bound, step):
        self.X = np.linspace(lower_bound, upper_bound, step)
        self.Y = np.linspace(lower_bound, upper_bound, step)

        self.X, self.Y = np.meshgrid(self.X, self.Y)

        self.Z = self.calc_z(self.X, self.Y, A=10)

    def calc_z(self, *X, **kwargs):
        A = kwargs.get('A', 10)
        return A + sum([(x ** 2 - A * np.cos(2 * math.pi * x)) for x in X])

    def plot(self):
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        ax.plot_surface(self.X, self.Y, self.Z, rstride=1, cstride=1, cmap=cm.plasma, linewidth=0, antialiased=False)
        plt.show()


if __name__ == '__main__':
    rastrigin_wrapper = RastriginWrapper(-4, 4, 100)
    rastrigin_wrapper.plot()
