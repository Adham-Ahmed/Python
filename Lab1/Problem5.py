# Problem 5
import sys

# The program takes a string and remove the vowels character from it then
# print its new version
# Implementation hint:
# So, “Mobile” becomes “Mbl”

inputString = sys.argv[1]
vowels=['a','e','o','u','i']

for i in inputString:
    if(i in vowels):
        inputString=inputString.replace(i,"")

print(inputString)
