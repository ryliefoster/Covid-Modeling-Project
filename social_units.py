import random
import interactions
import covidConstants as cc

class Person:
    def __init__(self, id, status, susceptibility):
        self.id = id
        self.status = status
        self.susceptibility = susceptibility
        self.daysExposed = 0
        self.daysInfected = 0

    def __str__(self):
        return(f"{str(self.id)} {str(self.infStatus)} {str(self.susceptibility)}")

    def getId(self):
        return self.id
    
    def getStatus(self):
        return self.status
    
    def setStatus(self, status):
        self.status = status
    
    def getSusceptibility(self):
        return self.susceptibility
    
    def calculateExposureProbablity(self, maxInteractions, infected, total):
        if self.status == "S":
            interactions = random.randint(0, maxInteractions)
            exposureExents = interactions * infected / total
            nonExposureProb = (1-cc.singleExposureProb)**exposureExents
            return 1-nonExposureProb
    
    def updateStatus(self, exposureProb):
        if self.status == 'S':
            r = random.random()
            if r<= exposureProb:
                self.status = 'E'
        if self.status == 'E':
            self.daysExposed += 1
            if self.daysExposed >= cc.incubationPeriod:
                self.status = "I"
        if self.status == 'I':
            self.daysInfected += 1
            if self.daysInfected >= cc.infectionDuration:
                self.status = 'R'


class Population:
    def __init__(self, members):
        self.members = members
        self.susceptible = 0
        self.exposed = 0
        self.infected = 0
        self.removed = 0
        
        for member in members:
            if member.status == 'S':
                self.susceptible += 1
            if member.status == 'E':
                self.exposed += 1
            if member.status == 'I':
                self.infected += 1
            if member.status == 'R':
                self.removed += 1

    def updateSEIR(self):
        for m in self.members:
            exposureProb = m.calculateExposureProbablity(200, self.infected, len(self.members))
            m.updateStatus(exposureProb)
        self.susceptible = 0
        self.exposed = 0
        self.infected = 0
        self.removed = 0
        for m in self.members:
            if m.getStatus() == 'S':
                self.susceptible += 1
            if m.getStatus() == 'E':
                self.exposed += 1
            if m.getStatus() == 'I':
                self.infected += 1
            if m.getStatus() == 'R':
                self.removed += 1

        




