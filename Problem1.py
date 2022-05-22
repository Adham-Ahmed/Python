import math

# Problem1

def distance(x1,y1,x2,y2):
      return math.sqrt(pow((x2-x1),2) + pow((y2-y1),2))
      
distancex = distance(4,2,3,6)
print("distance between the points is: "+str(distancex))