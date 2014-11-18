# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import pattern.en
import messages
import sklearn.linear_model 
import sklearn.svm

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

def provessNewEmail():
    email = "The cat is new and really cool. Im enjoying her. Love, Mom."
    length = getLength(email)
#    trainingVector = zip(length, tones)

    
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
    from sklearn import svm
    X = [[0, 0], [1, 1]]
    y = [0, 1]
    trainingVector = makeTrainingVector()
    importances = getImportances()
    clf = svm.SVC()
    clf.fit(trainingVector, importances)  
    svm.SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0, degree=3,
    gamma=0.0, kernel='rbf', max_iter=-1, probability=False, random_state=None,
    shrinking=True, tol=0.001, verbose=False)

if __name__=='__main__':
    #print 'tone: ', getTones()
    #print 'import: ', getImportances()
    #print 'length is: ', getLengths()
    #print 'trainging vector: ', makeTrainingVector()
#    print 'ridge: ', runAIFitting()
    runSVM()
