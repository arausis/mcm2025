from ODE import *
import matplotlib.pyplot as plt

fig, ax = plt.subplots(2,2)
(ax1, ax2), (ax3, ax4) = ax

S = population(100, "S")
I = population(1, "I")
R = population(0, "R")

modl1 = model([S, I, R], (0.5, 0.1))
modl1.run_model(100, 100, ax1)


modl2 = model([S, I, R], (1, 0.1) )
modl2.run_model(100, 100, ax2)

modl3 = model([S, I, R], (0.6, 0.05) )
modl3.run_model(100, 100, ax3)

modl4 = model([S, I, R], (0.5, 0.3) )
modl4.run_model(100, 100, ax4)

fig.suptitle("SIR Models")

plt.show()
