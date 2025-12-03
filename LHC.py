import numpy as np

# create LHC
single_infection = np.linspace(start, stop, num= 100)
max_int = np.linspace(start, stop, num = 100)
param_4 = np.linspace(start, stop, num=100)
param_5 = np.linspace(start, stop, num=100)


# run through parameters
params = []
for i in single_infection:
    for j in max_int:
        for k in param_4:
            for l in param_5:
                # generate fit
                param = (i, j, k, l)
                params.append(params)

# calculate residuals
# data:
day = np.array([
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24, 26, 27, 28, 29, 30, 31, 34
])

count = np.array([
1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 10, 20, 61, 64, 70, 135, 174, 218, 285, 355, 454, 542, 621, 634, 691
])

residuals = []
for i in range(len(day)):
    c_real = count[i]
    c_gen = counts_generated[np.where(days_generated == day[i])] # handles the days w/ no data

    r = (c_real - c_gen)**2 / np.abs(c_real) # residual calculation- could be tweaked

    residuals.append(r)

res_min = fmin(residuals)

ind = residuals.index(res_min)

best_params = params[ind]