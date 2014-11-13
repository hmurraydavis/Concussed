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
    
if __name__=='__main__':
    plot_LengthV_Importance()
