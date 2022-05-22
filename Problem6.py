# #Problem6

# The program takes a string and a character and returns a list with all the
# locations that character was found in the given string.
# Implementation hint:
# String “Google” char ‘o’
# Output: [1,2]

def indexFinder(inputString,inputChar):

    lst = []
    for pos,char in enumerate(inputString):
        if(char == inputChar):
            lst.append(pos)
    print(lst)


indexFinder("adham","a")
indexFinder("Google","o")