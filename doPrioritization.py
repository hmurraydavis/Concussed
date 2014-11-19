# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import pattern.en
import messages
import sklearn.linear_model 
from sklearn import svm
import sklearn.svm
import pickle
import pprint

messages=messages.getMessages()

def getTones():
    '''Find the tone of all messages. '''
    tones = []
    for messageGroup in messages:
        messageBody=messageGroup[1]
        tone = getTone(messageBody)
        tones.append(tone)
    return np.array(tones)


def getSubjectivities():
    subjectivities = []
    for messageGroup in messages:
        messageBody=messageGroup[1]
        subjectivity = getSentiment(messageBody)
        subjectivities.append(subjectivity)
    return np.array(subjectivities)
    

def getImportances():
    importances = []
    for messageGroup in messages:
        importanceThisMessage = messageGroup[2]
        averageImportance=sum(importanceThisMessage)/len(importanceThisMessage)
        importances.append(averageImportance)
    return np.array(importances)


def getLength(message):
    words=message.split(' ')
    return len(words)
    
    
def getTone(message):
    (tone, subjectivity) = pattern.en.sentiment(message)
    return tone
    
    
def getSentiment(message):
    (tone, subjectivity) = pattern.en.sentiment(message)
    return subjectivity
    

def getLengths():
    lengths = []
    for messageGroup in messages:
        messageBody=messageGroup[1]
        lengths.append(getLength(messageBody))
    return np.array(lengths)
    
    
def makeTrainingVector():
    lengths = getLengths()
    tones = getTones()
    subjectivities = getSubjectivities()
    trainingVector = zip(lengths, tones, subjectivities)
    return trainingVector

def processNewEmail(email):
    email = "The cat is new and really cool. Im enjoying her. Love, Mom."
    length = getLength(email)
    tone = getTone(email)
    subjectivity = getSentiment(email)
    trainingVector = (length, tone, subjectivity)
    return trainingVector

    
def runAIFitting():
    trainingVector = makeTrainingVector()
    importances = getImportances()
    C = 1.0  # SVM regularization parameter
    
#    clf = sklearn.linear_model.Ridge(alpha=1.0)
    trainingVector = np.array(trainingVector)
    print importances
    rbf_svc = sklearn.svm.SVC(kernel='rbf', gamma=0.7, C=C).fit(trainingVector, importances)
#    print clf.predict(trainingVector)
    return clf
    
def runSVM():
    X = [[0, 0], [1, 1]]
    y = [0, 1]
    trainingVector = makeTrainingVector()
    importances = getImportances()
    clf = svm.SVC()
    clf.fit(trainingVector, importances)  
    trainingDataFound = svm.SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0, degree=3,
    gamma=0.0, kernel='rbf', max_iter=-1, probability=False, random_state=None,
    shrinking=True, tol=0.001, verbose=False)
    return clf
    
    
def saveTrainingData(saveTrainingDataFile):
    trainingDataFound = runSVM()
    with open(saveTrainingDataFile, 'w') as f:
        pickle.dump(trainingDataFound, f)
            

def loadTrainingData(saveTrainingDataFile,exampleInputMessage):
    with open(saveTrainingDataFile, 'r') as f:
        clf = pickle.load(f)
    tupleMessageData=processNewEmail(exampleInputMessage)
    return clf.predict(tupleMessageData)


if __name__=='__main__':
#    runSVM()
    saveTrainingDataFile = 'trainingData'
    exampleInputMessage = 'Hi, its mom. I love you.'
    saveTrainingData(saveTrainingDataFile)
    print 'saved ', loadTrainingData(saveTrainingDataFile,exampleInputMessage)
#    pprint.pprint(type(makeTrainingVector()[0]))
#    print processNewEmail(exampleInputMessage)
