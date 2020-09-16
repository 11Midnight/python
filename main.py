# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import gensim
import io
import codecs
import csv
import matplotlib.pyplot as plt
import re
from collections import OrderedDict
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
def analyslenofsentence(your_list,your_dict):
    for sentence in range(len(your_list)):
        if len(your_list[sentence]) in your_dict:
            your_dict[len(your_list[sentence])] += 1
        else:
            your_dict[len(your_list[sentence])] = 1
    summ = 0
    sumn = 0
    for item in your_dict:
        summ += (int(item) * int(your_dict[item]))
        sumn += int(your_dict[item])
    avgvalue = summ / sumn
    return avgvalue
def analyslenofword(your_dictone, your_dicttwo):
    for item in your_dictone:
        if len(item) in your_dicttwo:
            your_dicttwo[len(item)] += 1
        else:
            your_dicttwo[len(item)] = 1
    sorted(your_dicttwo)
    summ = 0
    sumn = 0
    for item in your_dicttwo:
        summ += (int(item) * int(your_dicttwo[item]))
        sumn += int(your_dicttwo[item])
    avgvalue = summ / sumn
    return avgvalue
def top20(your_dict):
    list_sorted = list(your_dict.items())
    list_sorted.sort(key=lambda i: i[1], reverse=True)
    top_20 = OrderedDict()
    for k, v in list_sorted:
        if k not in top_20:
            top_20[k] = v
            if len(top_20) == 20:
                break
    return top_20
spamlist = []
hamlist = []
spamdict = {}
spamdictlenwords = {}
spamdictlensentence = {}
hamdict = {}
hamdictlenwords = {}
hamdictlensentence = {}
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
avgvaluespamsentence=analyslenofsentence(spamlist, spamdictlensentence)
avgvaluehamsentence=analyslenofsentence(hamlist,hamdictlensentence)
avgvaluespam=analyslenofword(spamdict, spamdictlenwords)
avgvalueham=analyslenofword(hamdict, hamdictlenwords)
spam_top_20=top20(spamdict)
ham_top_20=top20(hamdict)
plt.bar(spamdictlenwords.keys(), spamdictlenwords.values(), color='g')
plt.title("Средняя длина слова: %.2f " % avgvaluespam)
plt.show()
plt.bar(hamdictlenwords.keys(), hamdictlenwords.values(), color='g')
plt.title("Средняя длина слова: %.2f " % avgvalueham)
plt.show()
plt.bar(spamdictlensentence.keys(), spamdictlensentence.values(), color='g')
plt.title("Средняя длина предложения: %.2f " % avgvaluespamsentence)
plt.show()
plt.bar(hamdictlensentence.keys(), hamdictlensentence.values(), color='g')
plt.title("Средняя длина предложения: %.2f " % avgvaluehamsentence)
plt.show()
plt.bar(spam_top_20.keys(), spam_top_20.values(), color='g')
plt.show()
plt.bar(ham_top_20.keys(), ham_top_20.values(), color='g')
plt.show()
#with open("repaired.csv", "w") as outfile:
 #   for item in sorted(spamdict):
  #      csv.writer(outfile).writerows(spamdict[item])
        #print("'%s':%s" % (item, spamdict[item]))
#print(ww[0])
#print(spamdict)
#analysis(spamlist,spamdict)
#analysis(hamlist,hamdict)
for item in sorted(spamdictlenwords):
 print("'%s':%s" % (item, spamdictlenwords[item]))
print("-------------------------------------------------------")
for item in sorted(hamdictlenwords):
    print("'%s':%s" % (item, hamdictlenwords[item]))
print("-------------------------------------------------------")
for item in sorted(spamdictlensentence):
    print("'%s':%s" % (item, spamdictlensentence[item]))
print("-------------------------------------------------------")
for item in sorted(hamdictlensentence):
    print("'%s':%s" % (item, hamdictlensentence[item]))
print("-------------------------------------------------------")
for item in spam_top_20:
    print("'%s':%s" % (item, spam_top_20[item]))
print("-------------------------------------------------------")
for item in ham_top_20:
    print("'%s':%s" % (item, ham_top_20[item]))
#new_input = [list_top20[0],list_top20]
#result = dict([new_input])
#print(result)
#print(sorted(list_top20)[-5:])

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