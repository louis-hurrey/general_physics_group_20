import numpy as np
import matplotlib.pyplot as plt

def dr_dt(t, r, gamma):
    return r[1], gamma / r[0]**2

def runge_kutta(h, t, r, gamma):
    k1 = np.array(dr_dt(t, r, gamma))
    k2 = np.array(dr_dt(t + h / 2, r + h / 2 * k1, gamma))
    k3 = np.array(dr_dt(t + h / 2, r + h / 2 * k2, gamma))
    k4 = np.array(dr_dt(t + h, r + h * k3, gamma))
    return r + h / 6 *  (k1 + 2 * k2 + 2 * k3 + k4)

def solve_differential_eq(gamma, t_max, h, initial_conditions):
    t_values = np.arange(0, t_max, h)
    r_values = np.zeros((len(t_values), 2))
    r_values[0] = initial_conditions

    for i in range(1, len(t_values)):
        r_values[i] = runge_kutta(h, t_values[i-1], r_values[i-1], gamma)

    return t_values, r_values

gamma = 1.0
t_max = 500.0
h = 0.01
#initial_guess = 40
target_r = 50

r_range = np.linspace(0.5,49.5,1000)
array = np.zeros(len(r_range))


for i in range(len(r_range)):
    t_values, r_values = solve_differential_eq(gamma, t_max, h, [r_range[i], 0.0])
    #print(t_values)
    index = np.where((np.abs(r_values[:, 0] - target_r)) == np.min(np.abs(r_values[:, 0] - target_r)))[0][0]
    #print(t_values[index])
    array[i] = t_values[index]

np.savetxt("optimisation.txt", array)