import _pickle as cPickel
import os
from sklearn import *
from collections import Counter
from sklearn.externals import joblib


def load(clf_file):
    with open(clf_file) as fp:
        clf = c.load(fp)
    return clf


def make_dict():
    direc = "enrov/emails/"
    files = os.listdir(direc)
    emails = [direc + email for email in files]
    words = []
    c = len(emails)

    for email in emails:
        f = open(email, encoding='latin1')
        blob = f.read()
        words += blob.split(" ")
        print (c)
        c -= 1

    for i in range(len(words)):
        if not words[i].isalpha():
            words[i] = ""

    dictionary = Counter(words)
    del dictionary[""]
    return dictionary.most_common(2000)


clf=joblib.load('text-classifier1.mdl')
d = make_dict()


while True:
    features = []
    inp = input(">>>")
    if inp == "exit":
        break
    for word in d:
        features.append(inp.count(word[0]))
    res = clf.predict([features])
    print(res)
    print (["Not Spam", "Spam!"][res[0]])