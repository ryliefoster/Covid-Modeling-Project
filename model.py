import random

import parameterFitting
import social_units as su
import matplotlib.pyplot as plt
import numpy as np
import covidConstants as cc


def model(indicies, singleExposureProb, maxInteractions):
    # Step 1: Generate populations (staff, non-staff, etc.)
    pop_size = cc.pop_size
    days = cc.days
    starting_num_infected = cc.start_infected

    peopleList = []
    data = []
    total_infected = []
    for k in range(pop_size):
        id = k
        x = random.uniform(0, 1)
        status = 'S'

        # if x < 0.01:
        #    status = 'I'
        if k < starting_num_infected:
            status = 'I'
        susceptibility = random.uniform(0, 1)
        peopleList.append(su.Person(id, status, susceptibility))


    passengers = su.Population(peopleList)

    #print(f"S={passengers.susceptible}, E={passengers.exposed}, I={passengers.infected}, R={passengers.removed}\n")
    data.append([passengers.susceptible, passengers.exposed, passengers.infected, passengers.removed])
    for day in range(days):
        passengers.updateSEIR(maxInteractions, singleExposureProb)
        #print(f"S={passengers.susceptible}, E={passengers.exposed}, I={passengers.infected}, R={passengers.removed}\n")
        data.append([passengers.susceptible, passengers.exposed, passengers.infected, passengers.removed])
        total_infected.append(passengers.total_infected)

    arr_converted_int = indicies.astype(np.int32)
    result = [total_infected[i] for i in arr_converted_int]
    #print(result)
    return result



