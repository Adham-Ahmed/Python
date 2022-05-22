#Problem 2
def problem2(InputArray):
      OutputArray=[]
      for number in InputArray:
           if(number not in OutputArray): 
             OutputArray.append(number)
      return OutputArray;

output=problem2([1,2,2,3,2])
print(output)
