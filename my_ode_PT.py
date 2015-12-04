# ode example
# AIMS-SN
# 8 Sept 2015

import numpy as np
import matplotlib.pyplot as plt

# dy/dt = f(y,t) = -3 * sin(t)
def f(y, t):
    dydt = -3 * np.sin(t)
    return dydt


# define arrays INITIALIZE
h = 0.005                    # step
t = np.arange(0, 10+h, h)  # 0<=t<=10
N = len(t)
y = np.zeros(N)            # solution values

# INITIAL CONDITION
y[0] = 3
for i in range(1,N):
    y[i] = y[i-1] + f(y[i-1], t[i-1])*h
    print y[i]

plt.axhline(color='cyan')
plt.axvline(color='magenta')
plt.plot(t, 3*np.cos(t),'r', lw=2, label="exact")
plt.plot(t,y,lw=2, label="solved") 
plt.legend()
plt.show()
