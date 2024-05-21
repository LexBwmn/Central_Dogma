import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# inital conditions
y0 = [0,0] # 0 mRNA, 0 protien 

# timepoint array 
t = np.linspace(0, 200, num=100)

k_m = 0.2
gamma_m = 0.05
k_p = 0.4
gamma_p = 0.1

params = [k_m, gamma_m, k_p, gamma_p]

def sim(variables, t, params):
    
    m = variables[0]
    p = variables[1]

    k_m = params[0]
    gamma_m = params[1]
    k_p = params[2]
    gamma_p = params[3]

    dmdt = k_m - gamma_m * m
    dpdt = k_p * m - gamma_p * p

    return([dmdt, dpdt])

#runnnig the simulation 
y = odeint(sim, y0, t, args=(params,))

#plot the results

#defining the plot
f,ax = plt.subplots(1)

#plotting lines

#first element of y 
line1, = ax.plot(t,y[:,0], color="b", label="M")

#second element of y
line2, = ax.plot(t,y[:,1], color="r", label="P")

#labels of x and y axis 
ax.set_ylabel("Abundance")
ax.set_xlabel("Time")

# legend label line 
ax.legend(handles=[line1, line2])

plt.show()

