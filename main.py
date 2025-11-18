import random
import social_units as su
import matplotlib.pyplot as plt

POP_SIZE = 3000
DAYS = 30

# Step 1: Generate populations (staff, non-staff, etc.)

peopleList = []

for k in range(POP_SIZE):
    id = k
    x = random.uniform(0,1)
    status = 'S'
    if x < 0.01:
        status = 'I'
    susceptibility = random.uniform(0,1)
    peopleList.append(su.Person(id, status, susceptibility))

passengers = su.Population(peopleList)
data = []
print(f"S={passengers.susceptible}, E={passengers.exposed}, I={passengers.infected}, R={passengers.removed}\n")
data.append([passengers.susceptible, passengers.exposed, passengers.infected, passengers.removed])
for day in range(DAYS):
    passengers.updateSEIR()
    print(f"S={passengers.susceptible}, E={passengers.exposed}, I={passengers.infected}, R={passengers.removed}\n")
    data.append([passengers.susceptible, passengers.exposed, passengers.infected, passengers.removed])

plt.plot(data)
plt.show()
