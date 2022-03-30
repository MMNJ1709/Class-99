intro=input("enter your introduction: ")
charCount=0
wordCount=1
for i in intro:
    charCount=charCount+1
    if(i==" "):
        wordCount=wordCount+1
print("number of word in the intro: ")
print(wordCount)
print("number of characters in the intro: ")
print(charCount)
