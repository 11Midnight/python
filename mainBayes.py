import csv
import string

import re
from gensim.parsing.preprocessing import remove_stopwords
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import word_tokenize
porter_stemmer = PorterStemmer()
stop_words = set(stopwords.words('english'))
def pcalc(bodyText,your_dict,lenwhatword,PWhat):
    Pham_result = 1
    res = re.sub('['+string.punctuation+']', '', bodyText).split()
    for word in res:
        if word in your_dict:
            Pham_result = Pham_result*your_dict[word]/lenwhatword
        else: Pham_result = Pham_result*(1/(lenwhatword+len(your_dict)))
    return Pham_result*PWhat
def multiple_appends(listname, *element):
    listname.extend(element)
def stemming(string):
    words = word_tokenize(string)
    repear_sentence=[]
    for w in words:
        multiple_appends(repear_sentence, porter_stemmer.stem(w), " ")
    return "".join(repear_sentence)
def analysis(your_list, your_dict):
    words = word_tokenize(your_list)
    for i in words:
        if i in your_dict:
            your_dict[i] += 1
        else:
            your_dict[i] = 1
def analyslenofsentence(your_list,your_dict):
    for sentence in range(len(your_list)):
        if len(your_list[sentence]) in your_dict:
            your_dict[len(your_list[sentence])] += 1
        else:
            your_dict[len(your_list[sentence])] = 1
    sumn = 0
    for item in your_dict:
        sumn += int(your_dict[item])
    return sumn
def analyslenofword(your_dictone):
    sumn = 0
    for item in your_dictone:
        sumn += int(your_dictone[item])
    return sumn

spamlist = []
hamlist = []
spamdict = {}
spamdictlensentence = {}
hamdict = {}
hamdictlensentence = {}
with open('sms-spam-corpus.csv', newline='') as f:
    reader = csv.DictReader(f, delimiter=',')
    for row in reader:
        if row['v1'] == "spam":
            spamlist.append(stemming(remove_stopwords(re.sub(r'[^A-Za-z]+', r' ', row['v2']).lower())))
        elif row['v1'] == "ham":
            hamlist.append(stemming(remove_stopwords(re.sub(r'[^A-Za-z]+', r' ', row['v2']).lower())))
for i in range(len(spamlist)):
    analysis(spamlist[i], spamdict)
for i in range(len(hamlist)):
    analysis(hamlist[i], hamdict)
lenspamsentence = analyslenofsentence(spamlist, spamdictlensentence)
lenhamsentence = analyslenofsentence(hamlist, hamdictlensentence)
countspamword = analyslenofword(spamdict)
counthamword = analyslenofword(hamdict)
ALLlen = lenspamsentence+lenhamsentence
P_Spam = lenspamsentence / ALLlen
P_Ham = lenhamsentence / ALLlen
print("Введите строку:")
bodyText = input()
PSpam_res = pcalc(bodyText, spamdict, countspamword, P_Spam)
PHam_res = pcalc(bodyText, hamdict, counthamword, P_Ham)
PSpam_resNormal = PSpam_res/(PSpam_res+PHam_res)
PHam_resNormal = PHam_res/(PSpam_res+PHam_res)
print("P(spam | bodyText) =  %s" % PSpam_resNormal)
print("P(ham | bodyText) =  %s" % PHam_resNormal)
if PSpam_resNormal > PHam_resNormal:
    print("Its Spam")
elif PSpam_resNormal < PHam_resNormal:
    print("Its Ham")
else:
    print("P equals")



