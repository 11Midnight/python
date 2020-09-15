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

slist = []
with open('sms-spam-corpus.csv', newline='') as f:
    reader = csv.DictReader(f, delimiter=',')
    for row in reader:
        slist.append(stempuk(remove_stopwords(re.sub(r'[^A-Za-z]+', r' ', row['v1']).lower())))
        slist.append(stempuk(remove_stopwords(re.sub(r'[^A-Za-z]+', r' ', row['v2']).lower())))
print(slist)
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