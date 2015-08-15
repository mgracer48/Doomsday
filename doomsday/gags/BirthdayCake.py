from doomsday.gags.Gag import Gag

class BirthdayCake(Gag):
    
    def __init__(self, minDamage, maxDamage, trainInterval, splatScale, splatColor):
        Gag.__init__(self, name = 'Birthday Cake', cls = self, model = 'phase_5/models/props/birthday-cake-mod.bam', anim = 'phase_5/models/props/birthday-cake-chan.bam')
        self.minDamage = minDamage
        self.maxDamage = maxDamage
        self.trainInterval = trainInterval
        self.splatScale = splatScale
        self.splatColor = splatColor
        
    def canLevelUp(self, exp):
        if(exp % self.trainInterval == 0):
            return True
        else:
            return False
        
    def levelUp(self):
        self.minDamage += 1
        self.maxDamage += 1
        
    def getTrainInterval(self):
        return self.trainInterval
    
    def getSplatScale(self):
        return self.splatScale
    
    def getSplatColor(self):
        return self.splatColor
        
    def getDamageCurve(self):
        return [self.minDamage, self.maxDamage]