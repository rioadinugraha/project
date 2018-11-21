import numpy

#calculations for time ratio
class timeDilation():

    def __init__(self,speedrelativeToLight):
        self.speedRelativeToLight = speedrelativeToLight
        self.TimeRatio = numpy.sqrt(1-self.speedRelativeToLight)

    def gettimeratio(self):
        return self.TimeRatio
