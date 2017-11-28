#Writed by: Valink, on: 27.11.2017

from sys import getsizeof, exit
from func import loadFile

res=loadFile("wordList")
fichier, size=res["content"], res["size"]
print("Loaded {}Kbs".format(size/1000))

wList=fichier.split("\n") #Getting the table of words

res=[] #Creating new tab, storing lowered words in it
for w in wList:
    res.append(w.lower())

finalStr="\n".join(res) #Reassembling res table into a single String

with open("wordList", "w") as file: #Saving lowered words in the opened file
    file.write(finalStr)