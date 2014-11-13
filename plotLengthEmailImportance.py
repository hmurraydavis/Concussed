# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import pattern.en
import messages
import sklearn.linear_model 

lengths=[]
plt.clf()
    
messages=messages.getMessages()
importance=[10,10,0,4,4,3,3,0,6,1]
    
def plot_LengthV_Importance():
    importances=[]
    lengths=[]
    for messageGroup in messages:
        messageBody=messageGroup[1]
        importancesThisMessage = messageGroup[2]
        averageImportance=sum(importancesThisMessage)/len(importancesThisMessage)
        words=messageBody.split(' ')
        importances.append(averageImportance)
        lengths.append(len(words))

    #colors = np.random.rand(N)
    #x=[2,3,4,5]
    #y=[3,4,5,6]
    lengthOfMessages_VsImportance=plt.scatter(lengths, importances, s=50, alpha=0.5)
    #m, b = np.polyfit(lengths, importances, 1)
    #plt.plot(lengths, ((m*lengths) + b), '-')
    
    plt.xlabel('Length of message',fontsize=18)
    plt.ylabel('Importance of message', fontsize=18)
    plt.title('Importance vs Length of Email', fontsize=21)
    plt.show()
    return (lengths, importances)

def getSentiment():
    tones = []
    importances = []
    for messageGroup in messages:
        messageBody=messageGroup[1]
        (tone, subjectivity) = pattern.en.sentiment(messageBody)
        tones.append(tone)
        importancesThisMessage = messageGroup[2]
        averageImportance=sum(importancesThisMessage)/len(importancesThisMessage)
        importances.append(averageImportance)
    plt.scatter(tones,importances, s = 50, alpha = 0.5)
    #m, b = np.polyfit(tones,importances, 1)
    #plt.plot(tones, m*tones + b, '-')
    
    plt.xlabel('Tone of Message', fontsize = 18)
    plt.ylabel('importance of Message', fontsize = 18)
    plt.title('Importance vs. Tone of Message', fontsize=21)
    plt.show()
    return (tones, importances)
    
def ridgeFit():
    y = [[2,3],[3,4]]
    x = np.array([[3],[6]])
    print 'x1: ', x
    clf = sklearn.linear_model.Ridge(alpha=1.0)
    clf.fit(x,y,sample_weight=None)
    return clf

if __name__=='__main__':
    #plot_LengthV_Importance()
    #getSentiment()
    print 'ridge fit: ',ridgeFit()

