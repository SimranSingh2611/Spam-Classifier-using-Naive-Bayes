import _pickle as cPickel
import os
from sklearn import *
from sklearn.externals import joblib
from collections import Counter

def load(clf_file):
    with open(clf_file) as fp:
        clf=c.load(fp)
    return clf

def make_dict():
    direc= "enrov/emails/"
    files = os.listdir(direc)
    emails = [direc + email for email in files]
    words = []
    c=len(emails)


    for email in emails:
        f = open(email, encoding = "latin1")
        blob=f.read()
        words+=blob.split(" ")
        print (c)
        c-=1

    print ("\n" , words)
    print(len(words))

    dictionary = Counter(words)
    print(dictionary.most_common(1000))
    return dictionary.most_common(1000)

clf=joblib.load('text-classifier.mdl')
d = make_dict()

while True:
    features = []

    inp = input(">")
    for word in d:
        features.append(inp.count(word[0]))

    res=clf.predict([features])

    print (["Not Spam!" , "Spam!"][res[0]])
