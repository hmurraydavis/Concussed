# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import pattern.en

lengths=[]
messages=['Looks just like Cagney! I swear she was part mule! Very cool', 
    'http://www.dressagedaily.com/article/mule-named-dyna-poised-make-dressage-history',
    'Hi Halie, Congratulations and thank you for signing up on Tab Bundler! Go to http://www.tabbundler.com/signup/authorize?authKey=72d95005-11be-401e-a7e1-5569fcb70163&userId=9421 to verify your email. By verifying your email, you will be able to sync bundles across multiple computers and even different browsers. You can also create links in order to share your bundles with people who do not use Tab Bundler. We sincerely hope you enjoy using our product, and if you are experiencing any difficulties at all, please visit http://www.tabbundler.com/instructions, or email support at tab.bundler@gmail.com. Warm Regards, The Tab Bundler Team www.tabbundler.com',
    'Sounds good! See you in the lab tonight/this afternoon!',
    'Sure! Lets meet from 3:30-5 tonight. I guess we should probably meet in the robo lab. Tomorrow the only time Im busy is from 2-3pm. We could meet from 12:30 to 2, and then play it by ear to see if we need to meet later that afternoon.',
    'Hi Cypress-- Im free today after my Babson class. That should end at 3:15 and I should be able to walk back by 3:30. Could you do 3:30-5 PM tonight? Tomorrow Im free from 12:30-3:30. Then Im free after 6:30, too, though Id love to get dinner before 7:30. I could bring that with me, though.',
    #'We need it so we can call him and find out where to go for a tour of a nuclear facility. Please reply soon so Saarth doesnt have to jump the fence!',
    'So Pink Floyds new album came out today.  All things considered, Im pretty excited. To mark the occasion, I’m going to play all of Floyd in my room.  I’m currently half way through Piper - I should get to The Endless River at around midnight. If you want to listen to some awesome music, come by at some point today.  WH425.  Feel free to hang out even if I’m not there.',
    "My key with an awesome multi-tool carabineer is still missing and it makes me really sad. If anyone finds either one (although key is attached to carabineer) I’d be happy to bake you brownies or come up with some other kind of reward!!!",
    "5:30 at Natick, $13. Get your imax on.",
    ">Part of my IPD project is performing sentiment analysis on emails to determine if the user actually wants to read that email from their mother-in-law! Currently, I'm really struggling to frame the problem and I think talking to you for 15-20 minutes would help me see a path through the challenge. I'm reading things online about how to do it, but they're pretty confusing and hard to understand. I'm pretty sure I'll be using nltk and scikit-learn. I'm just not really sure how to use them and am getting lost in how to approach solving it. I'm free Friday before 9:50, technically during lunch, though I suspect my bio lab will run long so then would not be ideal, and after Comp Robo. I'm free Monday before 10:50, during lunch, and after 3:30."
    ]
#print 'length mess: ', type(messages)
importance=[10,10,0,4,4,3,3,0,6,1]
    
def plot_LengthV_Importance():
    for message in messages:
        words=message.split(' ')
        #print 'type words: ', type(words)
        lengths.append(len(words))


    #colors = np.random.rand(N)
    x=[2,3,4,5]
    y=[3,4,5,6]
    lengthOfMessages_VsImportance=plt.scatter(lengths, importance, s=50, alpha=0.5)
    plt.xlabel('Length of message',fontsize=18)
    plt.ylabel('Importance of message', fontsize=18)
    plt.title('Importance vs Length of Email', fontsize=21)
    plt.show()

def getSentiment():
    tones = []
    for message in messages:
        (tone, subjectivity) = pattern.en.sentiment(message)
        tones.append(tone)
    plt.scatter(tones,importance, s = 50, alpha = 0.5)
    plt.xlabel('Tone of Message', fontsize = 18)
    plt.ylabel('importance of Message', fontsize = 18)
    plt.title('Importance vs. Tone of Message', fontsize=21)
    plt.show()

if __name__=='__main__':
    #plot_LengthV_Importance()
    getSentiment()


