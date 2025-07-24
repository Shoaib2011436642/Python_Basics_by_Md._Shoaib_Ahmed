createwrite = open("text.html", "w")        #"w" overwrites the entire data in the existing folder
                                            #we created the html file using open()
createwrite.write("<h1>Messi is the greatest footballer ever</h1>")

appendwr = open("text.text", "a")           #"a" - appends the added text in the end of the file

appendwr.write(". I love FC Barcelona")
appendwr.write(".\n I love FC Barcelona")   # \n - adds a new line