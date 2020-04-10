import math
import matplotlib.pyplot as plt
import numpy as np
#from ODESolver import *


import numpy as np 
from scipy.integrate import ode

class ODESolver:
    #ODESolver superclass
    #Any classes inheriting from this superclass must implement advance() method. 

    def __init__(self, f):
        self.f = f

    def advance(self):
        #advance solution one time step
        raise NotImplementedError

    def set_initial_conditions(self, U0):
        if isinstance(U0, (int, float)):
            #scalar ODE
                self.number_of_eqns = 1
                U0 = float(U0)
        else:
            # system if eqs
            U0 = np.asarray(U0)
            self.number_of_eqns = U0.size
            self.U0 = U0

    def solve(self, time_points):
        self.t = np.asarray(time_points)
        n = self.t.size
        self.u = np.zeros((n, self.number_of_eqns))
        self.u[0, :] = self.U0

        #Integrate
        for i in range(n-1):
            self.i = i 
            self.u[i+1] = self.advance()
        return self.u[:i+2], self.t[:i+2]

class ForwardEuler(ODESolver):
    def advance(self):
        u, f, i, t = self.u, self.f, self.i, self.t
        dt = t[i+1] - t[i]
        return u[i,:] + dt * f(u[i, :], t[i])


class SIR:
    """
    SIR disease model 
    s' = -beta*s*i
    i' = beta*S*i - nu*i
    """
    def __init__(self, nu, beta, SO, IO, RO):
        """
        nu, beta: parameters in the ODE system
        SO, IO, RO: initial values
        """

        self.beta = lambda t: beta
        self.nu = lambda t: nu

        self.inital_conditions = [SO, IO, RO]

    def __call__(self, u, t):
        S, I, R = u
        return np.asarray([
            -self.beta(t)*S*I, #Suspectible
            self.beta(t)*S*I - self.nu(t)*I, #Infected
            self.nu(t)*I #Removed/Recovered
        ])

"""
change in number of people who are S, I, R

"""

if __name__ == "__main__":
    sir = SIR(0.1, 0.0005, 1500, 1, 0)
    solver = ForwardEuler(sir)
    solver.set_initial_conditions(sir.inital_conditions)

    time_steps = np.linspace(0, 60, 1000)
    u, t = solver.solve(time_steps)

    plt.plot(t, u[:, 0], label="Susceptible")
    plt.plot(t, u[:, 1], label="Infected")
    plt.plot(t, u[:, 2], label="Recovered")

    plt.legend()
    plt.show()

