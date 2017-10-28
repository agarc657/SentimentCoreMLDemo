import csv
import re
import string
import pandas as pd

dict1 = []
with open('SentimentTwitter.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    with open("ProcessedTweets.csv", 'w') as csvfile1:
        fieldnames = ['class', 'text']
        spamwriter = csv.DictWriter(csvfile1, fieldnames=fieldnames,delimiter=',')
        # spamwriter.writerow(fieldnames)
        spamwriter.writeheader()

        for row in spamreader:
            if row != "":
                m = re.search("@", row[1])
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
                spamwriter.writerow({'class':row[0],'text':stepEight})
            # print stepFive
            # print stepOne
            # print

a = pd.read_csv("ProcessedTweets.csv")
b = pd.read_csv("epinions.csv")
b = b.dropna(axis=1)
merged = a.merge(b, on='class')
merged.to_csv("output.csv", index=False)




