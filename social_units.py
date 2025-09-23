class Person:
    def __init__(self, id, infStatus, susceptibility):
        self.id = id
        self.infStatus = infStatus
        self.susceptibility = susceptibility

    def __str__(self):
        return(f"{str(self.id)} {str(self.infStatus)} {str(self.susceptibility)}")

    def getId(self):
        return self.id
    
    def getInfStatus(self):
        return self.infStatus
    
    def getSusceptibility(self):
        return self.susceptibility

class Grouping:
    def __init__(self, members):
        self.members = members


class Population:
    def __init__(self, members):
        self.members = members


class SuperPop:
    def __init__(self, pops):
        self.pops = pops   



