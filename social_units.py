import random

import numpy as np

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
        return (f"{str(self.id)} {str(self.status)} {str(self.susceptibility)}")

    def getId(self):
        return self.id

    def getStatus(self):
        return self.status

    def setStatus(self, status):
        self.status = status

    def getSusceptibility(self):
        return self.susceptibility

    def calculateExposureProbablity(self, maxInteractions, infected, total, singleExposureProb):
        if self.status == "S":
            interactions = random.randint(int(np.floor(maxInteractions*total*.9)), int(np.floor(maxInteractions*total))) #maxInteractions*.5
            exposureExents = interactions * infected / total
            nonExposureProb = (1 - singleExposureProb) ** exposureExents
            return self.susceptibility * (1 - nonExposureProb)

    def updateStatus(self, exposureProb):
        if self.status == 'S':
            r = random.random()
            if r <= exposureProb:
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
        self.total_infected = 0

        for member in members:
            if member.status == 'S':
                self.susceptible += 1
            if member.status == 'E':
                self.exposed += 1
            if member.status == 'I':
                self.infected += 1
            if member.status == 'R':
                self.removed += 1

    def updateSEIR(self, maxInteractions, singleExposureProb):
        for m in self.members:
            exposureProb = m.calculateExposureProbablity(maxInteractions*len(self.members), self.infected, len(self.members), singleExposureProb)
            m.updateStatus(exposureProb)
        self.susceptible = 0
        self.exposed = 0
        self.infected = 0
        self.removed = 0
        self.total_infected = 0
        for m in self.members:
            if m.getStatus() == 'S':
                self.susceptible += 1
            if m.getStatus() == 'E':
                self.exposed += 1
            if m.getStatus() == 'I':
                self.infected += 1
            if m.getStatus() == 'R':
                self.removed += 1
        self.total_infected = self.removed+self.infected





#number of interactions
#singleExposureProb
#incubation???
#incoming populations (4 parameters and a constraint)