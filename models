import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# SIR model differential equations
def sir_model(y, t, beta, gamma):
    S, I, R = y
    dSdt = -beta * S * I
    dIdt = beta * S * I - gamma * I
    dRdt = gamma * I
    return dSdt, dIdt, dRdt

# Initial conditions
S0 = 0.99   # 99% susceptible
I0 = 0.01   # 1% infected
R0 = 0.0    # 0% recovered
y0 = S0, I0, R0

# Time vector (days)
t = np.linspace(0, 160, 160)

# Parameters
beta = 0.3   # Infection rate
gamma = 0.1  # Recovery rate

# Solve ODE
solution = odeint(sir_model, y0, t, args=(beta, gamma))
S, I, R = solution.T

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(t, S, label='Susceptible', color='blue')
plt.plot(t, I, label='Infected', color='red')
plt.plot(t, R, label='Recovered (Immune)', color='green')
plt.title('Immune Response Simulation using SIR Model')
plt.xlabel('Time (days)')
plt.ylabel('Population Fraction')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

