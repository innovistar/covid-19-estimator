import math


name = "Africa"
avgAge = 19.7
avgDailyIncomeInUSD = 4
avgDailyIncomePopulation = 0.73
periodType = "days"
timeToElapse = 38
reportedCases = 2747
population = 92931687
totalHospitalBeds = 678874


def Impact():
  print("Impact")
  currentlyInfected = (reportedCases * 10)
  print("currentlyInfected:", currentlyInfected)
  infectionsByRequestedTime = currentlyInfected * (2  ** math.trunc
                                                   (timeToElapse / 3))
  print("infectionsByRequestedTime:", infectionsByRequestedTime)
  severeCasesByRequestedTime = math.trunc(infectionsByRequestedTime * 0.15)
  print("severeCasesByRequestedTime:", severeCasesByRequestedTime)
  hospitalBedsByRequestedTime = math.trunc(0.35 * totalHospitalBeds) - severeCasesByRequestedTime
  print("hospitalBedsByRequestedTime:", hospitalBedsByRequestedTime)
  casesForICUByRequestedTime = math.trunc(infectionsByRequestedTime * 0.05)
  print("casesForICUByRequestedTime:", casesForICUByRequestedTime)
  casesForVentilatorsByRequestedTime = math.trunc(infectionsByRequestedTime * 0.02)
  print("casesForVentilatorsByRequestedTime:", casesForVentilatorsByRequestedTime)
  dollarsInFlight = (infectionsByRequestedTime * avgDailyIncomePopulation) * avgDailyIncomeInUSD * timeToElapse
  print("dollarsInFlight:", dollarsInFlight)


def severImpact():
  print("severImpact")
  currentlyInfected = (reportedCases * 50)
  print("currentlyInfected:", currentlyInfected)
  infectionsByRequestedTime = currentlyInfected * (2  ** math.trunc
                                                   (timeToElapse / 3))
  print("infectionsByRequestedTime:", infectionsByRequestedTime)
  severeCasesByRequestedTime = math.trunc(infectionsByRequestedTime * 0.15)
  print("severeCasesByRequestedTime:", severeCasesByRequestedTime)
  hospitalBedsByRequestedTime = math.trunc(0.35 * totalHospitalBeds) - severeCasesByRequestedTime
  print("hospitalBedsByRequestedTime:", hospitalBedsByRequestedTime)
  casesForICUByRequestedTime = math.trunc(infectionsByRequestedTime * 0.05)
  print("casesForICUByRequestedTime:", casesForICUByRequestedTime)
  casesForVentilatorsByRequestedTime = math.trunc(infectionsByRequestedTime * 0.02)
  print("casesForVentilatorsByRequestedTime:", casesForVentilatorsByRequestedTime)
  dollarsInFlight = (infectionsByRequestedTime * avgDailyIncomePopulation) * avgDailyIncomeInUSD * timeToElapse
  print("dollarsInFlight:", dollarsInFlight)


Impact()
severImpact()

