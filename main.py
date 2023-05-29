import time
startingFactor1Str = input("What is the starting factor1 number? ")
endingFactor1Str = input("What is the ending factor1 number? ")
factor2MaxNumberStr = input(" How far do you want each product to go up for factor2? ")
startingFactor1Int = int(startingFactor1Str)
endingFactor2Int = int(endingFactor1Str)
factor2MaxNumberInt = int(factor2MaxNumberStr)

for inputValueXInt in range(startingFactor1Int, endingFactor2Int+1, 1):
   for outputValueYInt in range(1, factor2MaxNumberInt+1, 1):
     answer = int(inputValueXInt * outputValueYInt)
     time.sleep(1)
     print(str(inputValueXInt) + " x " + str(outputValueYInt) + " = " + str(answer))