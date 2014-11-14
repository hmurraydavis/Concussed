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
    subjectivities = getSubjectivity()
    trainingVector = zip(lengths, tones)
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
    from sklearn import svm
    X = [[0, 0], [1, 1]]
    y = [0, 1]
    clf = svm.SVC()
    clf.fit(X, y)  
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
