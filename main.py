# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import gensim
import io
import codecs
import csv
import re
import nltk
from gensim.parsing.preprocessing import remove_stopwords
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
porter_stemmer = PorterStemmer()
from nltk.tokenize import word_tokenize
stop_words = set(stopwords.words('english'))
def multiple_appends(listname, *element):
    listname.extend(element)
def stempuk(stringg):
    words = word_tokenize(stringg)
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

spamlist = []
hamlist = []
spamdict = {}
hamdict = {}
with open('sms-spam-corpus.csv', newline='') as f:
    reader = csv.DictReader(f, delimiter=',')
    for row in reader:
        if row['v1'] == "spam":
            spamlist.append(stempuk(remove_stopwords(re.sub(r'[^A-Za-z]+', r' ', row['v2']).lower())))
        elif row['v1'] == "ham":
            hamlist.append(stempuk(remove_stopwords(re.sub(r'[^A-Za-z]+', r' ', row['v2']).lower())))
for i in range(len(spamlist)):
    analysis(spamlist[i], spamdict)
for i in range(len(hamlist)):
    analysis(hamlist[i], hamdict)
with open("spamdict.csv", "w") as outfile:
    writer = csv.DictWriter(outfile, fieldnames=spamdict)
    writer.writeheader()
    writer.writerow(spamdict)
with open("hamdict.csv", "w") as outfile:
    writer = csv.DictWriter(outfile, fieldnames=hamdict)
    writer.writeheader()
    writer.writerow(hamdict)
#with open("repaired.csv", "w") as outfile:
 #   for item in sorted(spamdict):
  #      csv.writer(outfile).writerows(spamdict[item])
        #print("'%s':%s" % (item, spamdict[item]))
#print(ww[0])
#print(spamdict)
#analysis(spamlist,spamdict)
#analysis(hamlist,hamdict)
#for item in spamdict:
 #   print("'%s':%s" % (item, spamdict[item]))

#with open("repaired.csv", "w") as outfile:
    #csv.writer(outfile).writerows(slist)
#np.savetxt('file_2', slist, delimiter=",")
#with open('eggs.csv', 'w', newline='') as csvfile:
    #spamwriter = csv.writer(csvfile, delimiter=';')
   # spamwriter.writerow(slist)
#wtr = csv.writer(open('out.csv', 'w'), delimiter=',', lineterminator='\n')
#for x in slist: wtr.writerow([x])
#wr = csv.writer(open('out.csv', 'w'), delimiter=";")
#wr.writerows(slist)