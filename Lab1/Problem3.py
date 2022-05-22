# Problem 3

def front_back(a, b):
    print (a, b)
    a_indx = int((len(a)+1)/2)
    b_indx = int((len(b)+1)/2)

    print (a[:a_indx] + b[:b_indx] + a[a_indx:] +b[b_indx:])
    print ("\n")

front_back("ab", "cd")
front_back("abc", "de")
front_back("ab", "cde")
front_back("abc", "def")



