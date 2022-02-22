#!/usr/bin/env python3
# Working from this article: https://towardsdatascience.com/my-absolute-go-to-for-sentiment-analysis-textblob-3ac3a11d524
# Using corpora and TextBlob
from asyncio.windows_events import NULL
import sys
from textblob import TextBlob

# Get polarity of sentence
def sentencePolarity(sentence):
    return TextBlob(sentence).sentiment.polarity

# Get subjectivity of sentence
def sentenceSubjectivity(sentence):
    return TextBlob(sentence).sentiment.subjectivity

def runFile(file, sub, pol):
    f = open(file, 'r')
    lines = f.readlines()

    for line in lines:
        if line != '' and line != '\n':
            print('Line: ' + line + '\n' )
            if sub:
                print('Subjectivity: ' + str(sentenceSubjectivity(line)) + '\n')
            if pol:
                print('Polarity: ' + str(sentencePolarity(line)) + '\n')
            print('\n')
            
    

# Main function, takes in file names as arguments and will print polarity/subjectivity of each line based on arguments
def main():
    argc = len(sys.argv) # Number of arguments
    argv = sys.argv # Arguments

    if(argc == 1):
        print('No file specified.')
        exit
    pol = False
    sub= False
    files = []

    for s in argv:
        if s == '-p':
            print('Run polarity.')
            pol = True
        elif s == '-s':
            print('Run subjectivity.')
            sub = True
        else:
            files.append(s)

    if files.__len__ == 0:
        print('No file specified.')
        exit
    if not pol and not sub:
        print('No output specified.')
        exit
    for file in files:
        runFile(file, sub, pol)



        



        
    

# Invoke main function
if __name__ == "__main__":
    main()