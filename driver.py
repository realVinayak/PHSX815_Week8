import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

MIN_MU = -10
MAX_MU = 10
N_exp = 10000
N_meas = 5
STD_DEV = 2
N_step = 100


def driver():
    true_values = []
    measured_values = []
    for mu_true in (np.linspace(MIN_MU, MAX_MU, N_step)):
        all_experiment_draw_as_meas = np.random.normal(mu_true, STD_DEV,
                                                       (N_exp, N_meas))
        data = np.sum(all_experiment_draw_as_meas, axis=1) / N_meas
        for temp in data:
            measured_values.append(temp)
            true_values.append(mu_true)

    return true_values, measured_values


if __name__ == '__main__':
    tr_val, m_val = driver()
    plt.hist2d(tr_val, m_val, bins=100, norm=mcolors.PowerNorm(0.4))
    plt.xlabel('true mean')
    plt.ylabel('measured mean')
    plt.savefig('plot.png')
