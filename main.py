import random, sys, time, os, re
import nltk
import numpy as np
import random
import string 
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def printt(thingggg, dela=.04):
    for i in thingggg:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(dela)
    print("")



f=open('corpus.txt', 'r', errors ='ignore')
raw=f.read()
raw=raw.lower()
nltk.download('punkt') 
nltk.download('wordnet') 
sent_tokens = nltk.sent_tokenize(raw)
word_tokens = nltk.word_tokenize(raw)

lemmer = nltk.stem.WordNetLemmatizer()
def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))



GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up","hey",)
GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]
def greeting(sentence):
 
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)

def response(user_response):
    robo_response=''
    sent_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx=vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if(req_tfidf==0):
        robo_response=robo_response+"I don undastand u human"
        return robo_response
    else:
        robo_response = robo_response+sent_tokens[idx]
        return robo_response

flag=True
printt("bily: My name is bily. So far I an answer questions about anything. If you want to exit, type Bye!, but dont...")
while(flag==True):
    user_response = input(": ")
    user_response=user_response.lower()
    if(user_response!='bye'):
        if(user_response=='thanks' or user_response=='thank you' ):
            flag=False
            printt("bily: You are welcome..")
        else:
            if(greeting(user_response)!=None):
                printt("bily: "+greeting(user_response))
            else:
                print("bily: ",end="")
                printt(response(user_response))
                sent_tokens.remove(user_response)
    else:
        flag=False
        printt("bily: Bye! take care...")