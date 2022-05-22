# Problem 4
# notice this function is not optimized and the sole purpose is getting familiar with python's syntax

def textfileToCleanArray(file_name):
      f = open(file_name, "r")
      text=f.read()
      text=text.lower().strip()
      textAsArray=text.split(' ')
      return textAsArray;




def top20RepeatedWords(textAsArray):
      mostRepeatedWordsArray=[]
      for i in range(20): #getting the 20 most repeated words in the text file
          mostReaptedWord=max(set(textAsArray),key=textAsArray.count)
          mostRepeatedWordsArray.append(mostReaptedWord)
          for element in textAsArray: #removing the most repeated word from the main array
            if(mostReaptedWord in textAsArray):
              textAsArray.remove(mostReaptedWord)
      return mostRepeatedWordsArray

def fileWriter(array):
      f = open("outputfile.txt", "w")
      for word in array:
          f.write(word+"\n")
      f.close()



def top_20_repeated_word_finder_and_writer(file_name):
      
      textAsArray=textfileToCleanArray(file_name)
      mostRepeatedWordsArray=top20RepeatedWords(textAsArray)
      fileWriter(mostRepeatedWordsArray)
      
top_20_repeated_word_finder_and_writer("textfile.txt")


# problem 4 done



