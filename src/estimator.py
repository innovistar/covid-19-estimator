import math


def estimator():
  data = dataInput()
  impact = Impact()
  severImpact = severeImpact()
  return data, impact, severImpact 



name = "Africa"
avgAge = 19.7
avgDailyIncomeInUSD = 4
avgDailyIncomePopulation = 0.73
periodType = "days"
timeToElapse = 38
reportedCases = 2747
population = 92931687
totalHospitalBeds = 678874

if periodType == "days":
    timeToElapse *= 1
elif periodType == "months":
    timeToElapse *= 30
elif periodType == "weeks":
    timeToElapse *= 7


def dataInput():
  print("Region:", name)
  print("avgAge:", avgAge)
  print("avgDailyIncomeInUSD:", avgDailyIncomeInUSD)
  print("avgDailyIncomePopulation:", avgDailyIncomePopulation)
  print("periodType:", periodType)
  print("timeToElapse:", timeToElapse)
  print("reportedCases:", reportedCases)
  print("population:", population)
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
  dollarsInFlight = round(infectionsByRequestedTime * avgDailyIncomePopulation) * avgDailyIncomeInUSD * timeToElapse
  print("dollarsInFlight:", dollarsInFlight)


def severeImpact():
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
  dollarsInFlight = round(infectionsByRequestedTime * avgDailyIncomePopulation) * avgDailyIncomeInUSD * timeToElapse
  print("dollarsInFlight:", dollarsInFlight)

  


  
estimator()
