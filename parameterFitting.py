import numpy as np
from scipy.optimize import curve_fit
from matplotlib import pyplot as plt

import model


def parameterFit():
    x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27], dtype=np.int32)
    y = np.array([1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 11, 11, 21, 62, 65, 71, 136, 136, 175, 219, 219, 286, 356, 455, 543, 622], dtype=np.int32)

    plt.plot(x, y, 'o')
    initial_params = [0.0008172448979591837, 0.00020506122448979593] #[0.02050612244897959, 0.06131836734693878]
    param, param_cov = curve_fit(model.model, x, y, p0=initial_params)
    x_line = np.arange(30)
    y_line = model.model(x_line, param[0], param[1])
    plt.plot(x_line, y_line)
    plt.plot()
    plt.show()
    return

def parameterFit1():
    x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27],
                 dtype=np.int32)
    y = np.array(
        [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 11, 11, 21, 62, 65, 71, 136, 136, 175, 219, 219, 286, 356, 455, 543,
         622], dtype=np.int32)

    exposureProb = np.linspace(0.000001, .01, 50)
    maxInteractions = np.linspace(0.000001, .01, 50)
    best = 1e20
    ep = 0
    mi = 0
    for i in exposureProb:
        print(i)
        for j in maxInteractions:
            output = model.model(x, i, j)
            total = 0
            for n in range(0, len(y)):
                total += np.abs(y[n]-output[n])**2
                #print(total)
            if total <= best:
                best = total
                ep = i
                mi = j
                print(best)
    print(ep, mi)

#data from: https://pmc.ncbi.nlm.nih.gov/articles/PMC7837082/pdf/477_2020_Article_1968.pdf