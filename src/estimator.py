import math


print("data")
name = "Africa"
print("name:", name)
avgAge = 19.7
print("avgAge:", avgAge)
avgDailyIncomeInUSD = 4
print("avgDailyIncomeInUSD:", avgDailyIncomeInUSD)
avgDailyIncomePopulation = 0.73
print("avgDailyIncomePopulation:", avgDailyIncomePopulation)
periodType = "days"
print("periodType:", periodType)
timeToElapse = 38
print("timeToElapse:", timeToElapse)
reportedCases = 2747
print("reportedCases:", reportedCases)
population = 92931687
print("population:", population)
totalHospitalBeds = 678874
print("totalHospitalBeds:", totalHospitalBeds)


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

