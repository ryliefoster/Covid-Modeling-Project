import numpy as np
from scipy.stats import qmc

'''
# create LHC
single_infection = np.linspace(start, stop, num= 1000)
max_int = np.linspace(start, stop, num = 1000)
#param_4 = np.linspace(start, stop, num=100)
#param_5 = np.linspace(start, stop, num=10)


# run through parameters
params = []
for i in single_infection:
    for j in max_int:
        param = (i, j)
        params.append(params)

# run through parameters
params = []
for i in single_infection:
    for j in max_int:
        for k in param_4:
            for l in param_5:
                # generate fit
                param = (i, j, k, l)
                params.append(params)
'''

#Generation of samples of paramter sets 
nparams = 2 #no. of parameters
nsample = 10000 #no. of samples
sampler = qmc.LatinHypercube(d=nparams)
sample = sampler.random(n=nsample)

#Uniform sampling
min_vals = [0, 0] #minimum values of parameters - get from Jordan
max_vals = [2, 2] #maximum values of parameters - get from Jordan
l_bounds = np.array(min_vals)
u_bounds = np.array(max_vals) 
sample_params = qmc.scale(sample, l_bounds, u_bounds)
a_sample = sample_params[:,0]
b_sample = sample_params[:,1]

gen_data = []

for i in range(nsample):
    a = a_sample[i]
    b = b_sample[i]

    model = # generate model data
    gen_data.append(model)


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