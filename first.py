import math


# Problem1

def distance(x1,y1,x2,y2):
      return math.sqrt(pow((x2-x1),2) + pow((y2-y1),2))
      


distancex = distance(4,2,3,6)
print("distance between the points is: "+str(distancex))

##


#Problem 2
def problem2(InputArray):
      OutputArray=[]
      for number in InputArray:
           if(number not in OutputArray): 
             OutputArray.append(number)
      return OutputArray;

output=problem2([1,2,2,3,2])
print(output)

#


# Problem 3


      





