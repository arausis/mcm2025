import os
import sys
from scipy.integrate import odeint
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotx
matplotlib.use('TkAgg')
import threading


# An object to represent each population that we want to simulate
class population:
    x_0 = 0
    name = ""
    param1 = None
    param2 = None

    def __init__(self, x0, name):
        self.x_0 = x0
        self.name = name


# An object for our ODE model

class model:
    # A list of population objects
    populations = []
    # Each of their starting values
    x_0 = []

    # A few model parameter constants
    beta, gamma = (0, 0)

    def __init__(self, populations, parameters):
        self.populations = populations
        self.x_0 = [p.x_0 for p in populations]
        self.beta, self.gamma = parameters

    """
    This function will be run by the ODE for each timestep
    input -> x: a list of population counts at each timestep, t: current time at each timestep
    output -> a list of slopes for each population
    """

    def calculate(self, x, t):
        dndt_list = []

        S, I, R = tuple(x)
        N = S + I + R

        dS =  - self.beta * S * I / N
        dI = self.beta * S * I / N - self.gamma * I
        dR =  self.gamma * I

        dndt_list = [dS, dI, dR]

        return dndt_list
    
    def run_model(self, tmax, ticks, ax):
        # Run the ODE
        t = np.linspace(0,tmax, ticks)
        x = odeint(self.calculate, self.x_0 ,t)

        # Plot lines 
        for i in range(len(x[0])):
            ax.semilogy(t, x[:,i], label=self.populations[i].name)

        # Graph parameters
        #ax.set_title("SIR Model")
        ax.set_xlim([0, tmax])
        ax.legend()

if __name__ == "__main__":
    DIR = os.path.dirname(os.path.abspath(__file__)) + "/vars"
    S = population(100, "S")
    I = population(1, "I")
    R = population(0, "R")
    modl = model([S, I, R], (0.5, 0.1) )
    modl.run_model(100, 100)

# Test (Nick)