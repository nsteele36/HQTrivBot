#HQ TRIVIA BOT
#Programmed by: Nick Steele

#use these commands to install dependencies
#pip install pillow
#pip install tesseract
#pip install cv2
#pip install ntlk
#pip install beautifulsoup4

#put the screenshot folder in the same directory as the script
#run this program using "time python hqtrivsolver.py"
#the time keywords will give you the run time in secs at the end of execution

import requests
from html.parser import HTMLParser
from PIL import Image
import pytesseract
import cv2
import os
import re
from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords
import subprocess #this is for using bash shell inside program
                  #dont need it if you are taking screen shots a different way

#this function finds the number of search results each answer has
def findDigits(s):
    r = ""
    for char in str(s):
        if char.isdigit():
            r += char
    return r

#this function queries google and returns the search results for each answer
def getNumOfResults(s):
    pattern = re.compile(r'\b(' + r'|'.join(stopwords.words('english')) + r')\b\s*')
    s = pattern.sub('', s)
    r = requests.get("https://www.google.com/search", params={'q':s.lower()})
    soup = BeautifulSoup(r.text, "html.parser")
    res = soup.find("div", {"id": "resultStats"})
    res = findDigits(res)
    return int(res)

#THIS IS THE START OF THE PROGRAM
print('getting screenshot...')

#Taking screenshots this way is only limited to UNIX Systems and Android Phones
#You'll have to look for your own solution to getting IOS screenshots 
#subprocess.call("/home/soandso/Documents/HACKUTD/sc.sh", shell=True)
#image = cv2.imread('./Screenshots/screen.png')

#IF YOU CANT SCREENSHOT FROM YOUR PHONE, you can still import an image with this line of code
#simply change the .png file to the file you want. I'll include a bunch of my screenshots for you to play with
image = cv2.imread('./Screenshots/screen8.png')
#run image through filter so that image is more saturated and text isnt skipped
imgFilter = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
imgFilter = cv2.medianBlur(imgFilter, 3)

#crop the image so it is just the question and answers
#***YOU WILL HAVE TO CHANGE THIS IF YOU FIND A SCREENSHOT SOLUTION FOR YOUR PHONE
imgFilter = imgFilter[500:1400,75:1000]
 
filename = "./screen.png".format(os.getpid())
cv2.imwrite(filename, imgFilter)

#these two commands will open the image in an image viewer
#they are just used for testing but if you want to see what the image that is being parsed looks like uncomment these lines
#cv2.imshow("sc", imgFilter)
#cv2.waitKey(0)

print('getting Q&A...')
#use tesseract to conver the image to string
text = pytesseract.image_to_string(Image.open(filename))
#remove temp file
os.remove(filename)

#split the text by a single question mark in the text
question, answers  = text.split('?', 1)
#puts all the question text on one line instead of separate lines
question = question.replace('\n', " ")
#removes empty lines from the answers
answers = os.linesep.join([s for s in answers.splitlines() if s])

#seperate the answers into different variables
a, b, c = answers.split('\n',2)
a = a.replace('\n', ' ')
b = b.replace('\n', ' ')
c = c.replace('\n', ' ')
#create a list including all of them
ANSWERS = [a, b, c]

print('forming searches...')

#concatenate the question and each answers to send to google for query
searches = [(question + " " + a), (question + " " + b), (question + " " + c)]

#start searching
print('searching...')
numOfResults = [0, 0, 0]
i = 0
for s in searches:
    numOfResults[i] = getNumOfResults(s)
    i = i + 1
    
#take the number of search results and compare them to each other and find the biggest
print('comparing results...')
if (numOfResults[0] > numOfResults[1]) and (numOfResults[0] > numOfResults[2]):
    biggest =  numOfResults[0]
elif (numOfResults[1] > numOfResults[0]) and (numOfResults[1] > numOfResults[2]):
    biggest = numOfResults[1]
else:
    biggest = numOfResults[2] 
    
#print the questions information
j = 0
print('***Question INFO***\n' + question + '?\nA. ' + a + '\nB. ' + b +'\nC. ' + c) 
print('printing results...')

#print the results
print('***RESULTS***')
for a in numOfResults:
    if a == biggest:
        print(str(ANSWERS[j]) + " " + "{:,}".format(numOfResults[j]) + " hits *WINNER!!!")
    else:
        print(str(ANSWERS[j]) + " " + "{:,}".format(numOfResults[j]) + " hits")
    j = j + 1





