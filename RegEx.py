import re
from re import findall

#return all the matched values (Here all the lowecase letters in a range of a to f
text = "Messi is the greatest footballer of all time"
a = re.findall("[a-f]", text)           #findall - Returns a list containing all matches
print(a)                                       #range of a to f will be written under "closing bracket[-]"

#return Yes! if the string starts with Messi.
b = re.findall("^Messi", text)      # ^ - starts with
if b:
    print("Yes! it starts with", b)
else:
    print("Not Found")




