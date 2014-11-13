# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import pattern.en
import messages
import sklearn.linear_model 

messages=messages.getMessages()

def getTones():
    '''Find the tone of all messages. '''
    tones = []
    for messageGroup in messages:
        messageBody=messageGroup[1]
        (tone, subjectivity) = pattern.en.sentiment(messageBody)
        tones.append(tone)
    return np.array(tones)

def getSubjectivity():
    subjectivities = []
    for messageGroup in messages:
        messageBody=messageGroup[1]
        (tone, subjectivity) = pattern.en.sentiment(messageBody)
        subjectivities.append(subjectivity)
    return np.array(subjectivities)
    
def getImportances():
    importances = []
    for messageGroup in messages:
        importanceThisMessage = messageGroup[2]
#        averageImportance=sum(importancesThisMessage)/len(importancesThisMessage)
        importances.append(importanceThisMessage)
    return np.array(importances)
    
def getLengths():
    lengths = []
    for messageGroup in messages:
        messageBody=messageGroup[1]
        words=messageBody.split(' ')
        lengths.append(len(words))
    return np.array(lengths)
    
def makeTrainingVector():
    lengths = getLengths()
    tones = getTones()
    trainingVector = zip(lengths, tones)
    return trainingVector
    
def runAIFitting():
    trainingVector = makeTrainingVector()
    importances = getImportances()
    
    clf = sklearn.linear_model.Ridge(alpha=1.0)
    clf.fit(trainingVector,importances,sample_weight=None)
    print clf.predict(trainingVector)
    return clf

if __name__=='__main__':
    #print 'tone: ', getTones()
    #print 'import: ', getImportances()
    #print 'length is: ', getLengths()
    #print 'trainging vector: ', makeTrainingVector()
    print 'ridge: ', runAIFitting()
