import os
from sklearn.metrics import accuracy_score
from sklearn.externals import joblib
from collections import Counter
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split as tts

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

def make_dataset(dictionary):
    direc = "enrov/emails/"
    files = os.listdir(direc)
    emails = [direc + email for email in files]


    feature_set = []
    labels = []
    c = len(emails)

    for email in emails:
        data = []
        f = open(email, encoding="latin1")
        words=f.read().split(' ')
        for entry in dictionary:
            data.append(words.count(entry[0]))

        feature_set.append(data)
        if "ham" in email:
            labels.append(0)
        if "spam" in email:
            labels.append(1)
        print (c)
        c=c-1

    return feature_set, labels


d = make_dict()
features, labels = make_dataset(d)

print(len(features),len(labels))



x_train, x_test, y_train, y_test = tts(features, labels, test_size=0.2)
clf=MultinomialNB()
clf.fit(x_train , y_train)
preds = clf.predict(x_test)
print (accuracy_score(y_test,preds))

joblib.dump(clf, 'text-classifier.mdl')

#save(clf , "text-classifier.mdl")
