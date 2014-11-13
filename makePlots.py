# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import pattern.en
import messages
import sklearn.linear_model 

plt.clf()
messages=messages.getMessages()


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
    lengthOfMessages_VsImportance=plt.scatter(lengths, importances, s=50, alpha=0.5)
    m, b = np.polyfit(lengths, importances, 1)
    lengths = np.array(lengths)    
    plt.plot(lengths, ((m*lengths) + b), '-')
    
    plt.xlabel('Length of message',fontsize=18)
    plt.ylabel('Importance of message', fontsize=18)
    plt.title('Importance vs Length of Email', fontsize=21)
    plt.show()
    return (lengths, importances)
    

def plotSentiment_vsImportance():
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
    m, b = np.polyfit(tones,importances, 1)
    tones = np.array(tones)
    plt.plot(tones, (m*tones) + b, '-')
    
    plt.xlabel('Tone of Message', fontsize = 18)
    plt.ylabel('importance of Message', fontsize = 18)
    plt.title('Importance vs. Tone of Message', fontsize=21)
    plt.show()
    return (tones, importances)
    
    
def plotSubjectivity_vsImportance():
    subjectivitys = []
    importances = []
    for messageGroup in messages:
        messageBody=messageGroup[1]
        (tone, subjectivity) = pattern.en.sentiment(messageBody)
        subjectivitys.append(subjectivity)
        importancesThisMessage = messageGroup[2]
        averageImportance=sum(importancesThisMessage)/len(importancesThisMessage)
        importances.append(averageImportance)
    plt.scatter(subjectivitys,importances, s = 50, alpha = 0.5)
    m, b = np.polyfit(subjectivitys,importances, 1)
    subjectivitys = np.array(subjectivitys)
    plt.plot(subjectivitys, (m*subjectivitys) + b, '-')
    
    plt.xlabel('Subjectivity of Message', fontsize = 18)
    plt.ylabel('importance of Message', fontsize = 18)
    plt.title('Importance vs. Subjectivity of Message', fontsize=21)
    plt.show()
    return (tones, importances)
    
if __name__=='__main__':
#    plot_LengthV_Importance()
#    plotSentiment_vsImportance()
    plotSubjectivity_vsImportance()
