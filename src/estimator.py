import math


def estimator():
  impact = Impact()
  severImpact = severeImpact()
  return impact, severImpact 

if periodType == "days":
    timeToElapse *= 1
elif periodType == "months":
    timeToElapse *= 30
elif periodType == "weeks":
    timeToElapse *= 7


  
def Impact():
  print("Impact")
  currentlyInfected = (reportedCases * 10)
  return currentlyInfected
  infectionsByRequestedTime = currentlyInfected * (2  ** math.trunc
                                                   (timeToElapse / 3))
  return infectionsByRequestedTime
  severeCasesByRequestedTime = math.trunc(infectionsByRequestedTime * 0.15)
  return severeCasesByRequestedTime
  hospitalBedsByRequestedTime = math.trunc(0.35 * totalHospitalBeds) - severeCasesByRequestedTime
  return hospitalBedsByRequestedTime
  casesForICUByRequestedTime = math.trunc(infectionsByRequestedTime * 0.05)
  return  casesForICUByRequestedTime
  casesForVentilatorsByRequestedTime = math.trunc(infectionsByRequestedTime * 0.02)
  return casesForVentilatorsByRequestedTime
  dollarsInFlight = round(infectionsByRequestedTime * avgDailyIncomePopulation) * avgDailyIncomeInUSD * timeToElapse
  return  dollarsInFlight


def severeImpact():
  print("severImpact")
  severeCurrentlyInfected = (reportedCases * 50)
  return  severeCurrentlyInfected
  InfectionsByRequestedTime = currentlyInfected * (2  ** math.trunc
                                                   (timeToElapse / 3))
  return InfectionsByRequestedTime 
  SevereCasesByRequestedTime = math.trunc(infectionsByRequestedTime * 0.15)
  return SevereCasesByRequestedTime
  HospitalBedsByRequestedTime = math.trunc(0.35 * totalHospitalBeds) - severeCasesByRequestedTime
  return HospitalBedsByRequestedTime
  CasesForICUByRequestedTime = math.trunc(infectionsByRequestedTime * 0.05)
  return CasesForICUByRequestedTime
  CasesForVentilatorsByRequestedTime = math.trunc(infectionsByRequestedTime * 0.02)
  return CasesForVentilatorsByRequestedTime
  DollarsInFlight = round(infectionsByRequestedTime * avgDailyIncomePopulation) * avgDailyIncomeInUSD * timeToElapse
  return DollarsInFlight

  


  
estimator()
