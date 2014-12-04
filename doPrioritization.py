# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import pattern.en
import messages as ms
import sklearn.linear_model 
from sklearn import svm
import sklearn.svm
import pickle
import pprint
import Queue
import os
import imaplib, re
import time
import socket
import email

messages=ms.getMessages()
prioritizedEmails = Queue.PriorityQueue()


class Message():
    def __init__(self):
        print 'init function ran'
#        Message=Message()

    def anounceMessagePresence(self, messageType):
        anouncement = 'You have a new %(messageType)s'% \
        {"messageType": messageType}
        os.system('espeak -v en-rp "%(anouncement)s"'%{"anouncement":anouncement})
    
    
    def getTones(self):
        '''Find the tone of all messages. '''
        tones = []
        for messageGroup in messages:
            messageBody=messageGroup[1]
            tone = self.getTone(messageBody)
            tones.append(tone)
        return np.array(tones)


    def getSubjectivities(self):
        subjectivities = []
        for messageGroup in messages:
            messageBody=messageGroup[1]
            subjectivity = self.getSentiment(messageBody)
            subjectivities.append(subjectivity)
        return np.array(subjectivities)
        

    def getImportances(self):
        importances = []
        for messageGroup in messages:
            importanceThisMessage = messageGroup[2]
            averageImportance=sum(importanceThisMessage)/len(importanceThisMessage)
            importances.append(averageImportance)
        return np.array(importances)


    def getLength(self, message):
        words=message.split(' ')
        return len(words)
        
        
    def getTone(self, message):
        (tone, subjectivity) = pattern.en.sentiment(message)
        return tone
        
        
    def getSentiment(self, message):
        (tone, subjectivity) = pattern.en.sentiment(message)
        return subjectivity
        

    def getLengths(self):
        lengths = []
        for messageGroup in messages:
            messageBody=messageGroup[1]
            lengths.append(self.getLength(messageBody))
        return np.array(lengths)
        
        
    def makeTrainingVector(self):
        lengths = self.getLengths()
        tones = self.getTones()
        subjectivities = self.getSubjectivities()
        trainingVector = zip(lengths, tones, subjectivities)
        return trainingVector

    def processNewEmail(self, email):
        length = self.getLength(email)
        tone = self.getTone(email)
        subjectivity = self.getSentiment(email)
        trainingVector = (length, tone, subjectivity)
        return trainingVector

        
    def runAIFitting(self):
        trainingVector = self.makeTrainingVector()
        importances = self.getImportances()
        C = 1.0  # SVM regularization parameter
    #    clf = sklearn.linear_model.Ridge(alpha=1.0)
        trainingVector = np.array(trainingVector)
        print importances
        rbf_svc = sklearn.svm.SVC(kernel='rbf', gamma=0.7, C=C).fit(trainingVector, importances)
    #    print clf.predict(trainingVector)
        return clf
        
    def runSVM(self):
        trainingVector = self.makeTrainingVector()
        importances = self.getImportances()
        clf = svm.SVC()
        clf.fit(trainingVector, importances)  
        trainingDataFound = svm.SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0, degree=3,
        gamma=0.0, kernel='rbf', max_iter=-1, probability=False, random_state=None,
        shrinking=True, tol=0.001, verbose=False)
        return clf
        
        
    def saveTrainingData(self, saveTrainingDataFile):
        trainingDataFound = self.runSVM()
        with open(saveTrainingDataFile, 'w') as f:
            pickle.dump(trainingDataFound, f)
                

    def prioritizeSingleEmail(self, saveTrainingDataFile,exampleInputMessage):
        global prioritizedEmails
        with open(saveTrainingDataFile, 'r') as f:
            clf = pickle.load(f)
        tupleMessageData=self.processNewEmail(exampleInputMessage)
        importanceMessage = -1*clf.predict(tupleMessageData)
#        print '\nimportance of a message: ', importanceMessage, '\n'
        prioritizedEmails.put( (importanceMessage, exampleInputMessage)) 
#        print prioritizedEmails.get()
        return prioritizedEmails


    def getMostImportantEmail(self):
        mostImportant = prioritizedEmails.get()
        print 'most important: ', mostImportant
    
    
class Email(Message):

    messageType = 'email'
#    mail = None #attribut should be here
    
    def __init__(self):
        imap_host = 'imap.gmail.com'
        self.mail = imaplib.IMAP4_SSL(imap_host)
        print self.mail
        password = open('password.txt','r')
        password = password.read()
        self.mail.login("messagespectrum@gmail.com", password) #this mail object needs to go int my get mail finction
        self.mail.select("inbox") # connect to inboxself.
        print self.get_mail()
        
     
    def get_mail(self): #mail object/attribute needs to go poof from the comment above into this function
        result, data = self.mail.uid('search', None, 'UNSEEN')
        uid_list = data[0].split()
        print len(uid_list), 'Unseen emails.'
     
        mails = []
     
        for messageID in uid_list:
            result, data = self.mail.fetch(messageID, "(RFC822)") # fetch the email body (RFC822) for the given ID
            raw_email = data[0][1] # here's the body, which is raw text of the whole email
            #print raw_email
            email_message = email.message_from_string(raw_email)
     
            bodytext=email_message.get_payload()[0].get_payload()
            if type(bodytext) is list:
                bodytext=','.join(str(v) for v in bodytext)
     
            mails.append({'from': email_message['From'], 'body': bodytext})
     
        return mails
     
    
        
class faceBook(Message):
   def __init__():
        return
        
class text(Message):
    def __init__():
        return

if __name__=='__main__':
#    runSVM()
    message = Message()
    Email = Email()
#    saveTrainingDataFile = 'trainingData'
#    message.saveTrainingData(saveTrainingDataFile)
#    exampleInputMessage = 'Hi, its mom. I love you.'
#    empty = ' '
#    
#    message.saveTrainingData(saveTrainingDataFile)
#    
#    message.prioritizeSingleEmail(saveTrainingDataFile, ms.newMessage1())
#    message.prioritizeSingleEmail(saveTrainingDataFile, ms.newMessage2())
#    message.prioritizeSingleEmail(saveTrainingDataFile, exampleInputMessage)
#    message.getMostImportantEmail()
    message.anounceMessagePresence('email')


