# import unicodecsv as csv
import re
import  csv
import in

import string
import pandas as pd

dict1 = []
with open('SentimentTwitter.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    with open("ProcessedTweets.csv", 'w') as csvfile1:
        fieldnames = ['class', 'text']
        # spamwriter = csv.DictWriter(csvfile1, fieldnames=fieldnames,delimiter=',')
        spamwriter = csv.writer(csvfile1,delimiter=",")
        spamwriter.writerow(fieldnames)
        # spamwriter.writeheader()

        for row in spamreader:
            # print row[1]
            # stepZero = row[1][:m.start()] + row[1][m.end():]
            stepZero = row[1].strip(',.').lower()
            stepOnePointOne = stepZero.strip(',.').lower()
            stepOne = re.sub('(?:#|@)[a-zA-Z0-9_]+ ?', ' ', stepOnePointOne)
            stepTwo = re.sub("[a-zA-Z]*([0-9]{3,})[a-zA-Z0-9]* ?","",stepOne )
            stepThree = re.sub("[[:punct:]]", "", stepTwo)
            stepFour = re.sub("[\r\n]", "", stepThree)
            stepFive = re.sub(" {2,}", " ", stepFour)
            # stepSix = stepFive.translate(None, string.punctuation)
            stepsix = re.sub(r'\s*(?:https?://)?\S*\.[A-Za-z]{2,5}\s*', ' ', stepFive).strip()
            stepSeven = re.sub(r'\s*(?:http?://)?\S*\.[A-Za-z]{2,5}\s*', ' ', stepsix).strip()
            # stepSix = re.sub(r'^http?://.*[\r\n]*', '', stepFive, flags=re.MULTILINE)
            # stepSeven  = re.sub(r'^https?://.*[\r\n]*', '', stepFive, flags=re.MULTILINE)
            stepEight = re.sub('\S+', lambda m: re.sub('^\W+|\W+$', '', m.group()), stepSeven)

            if stepEight != "":
                try:
                    classType = row[0].decode("utf-8")
                    text = stepEight.decode("utf-8")
                    spamwriter.writerow([classType, text])
                except (UnicodeEncodeError, UnicodeDecodeError):
                    continue

target = '/Volumes/RamDisk/SentimentCoreML/Convert/test.csv'
src1 = '/Volumes/RamDisk/SentimentCoreML/Convert/ProcessedTweets.csv'
src2 = '/Volumes/RamDisk/SentimentCoreML/Convert/epinions.csv'
tf = open(target, 'a')
tf.write(open(src1).read())
tf.write(open(src2).read())
tf.close()



