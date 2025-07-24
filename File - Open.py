#open & read the file
#I have created the text file for reading in the same directory of the python file
readtext = open("text.text", "r")       #open the text file, "r" for read
print(readtext.read())                  #read() - read the text for output
