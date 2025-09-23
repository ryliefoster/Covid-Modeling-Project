import random
import social_units as su
import interactions as intr

# Step 1: Generate populations (staff, non-staff, etc.)

peopleList = []

for k in range(4000):
    id = k
    x = random.uniform(0,1)
    infStatus = "SUSCEPTIBLE"
    if x < 0.01:
        infStatus = "INFECTED"
    susceptibility = random.uniform(0,1)
    peopleList.append(su.Person(id, infStatus, susceptibility))

howdy