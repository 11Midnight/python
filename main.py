import csv
import matplotlib.pyplot as plt
import re
from collections import OrderedDict
from gensim.parsing.preprocessing import remove_stopwords
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import word_tokenize
porter_stemmer = PorterStemmer()
stop_words = set(stopwords.words('english'))
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
    for key, value in list_sorted:
        if key not in top_20:
            top_20[key] = value
            if len(top_20) == 20:
                break
    return top_20
def sortdict(your_dict):
    list_sorted = list(your_dict.items())
    list_sorted.sort()
    sorted = OrderedDict()
    for key, value in list_sorted:
        if key not in sorted:
            sorted[key] = value
    return sorted
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
            spamlist.append(stemming(remove_stopwords(re.sub(r'[^A-Za-z]+', r' ', row['v2']).lower())))
        elif row['v1'] == "ham":
            hamlist.append(stemming(remove_stopwords(re.sub(r'[^A-Za-z]+', r' ', row['v2']).lower())))
for i in range(len(spamlist)):
    analysis(spamlist[i], spamdict)
for i in range(len(hamlist)):
    analysis(hamlist[i], hamdict)
with open("output/spamdict.csv", "w") as outfile:
    writer = csv.DictWriter(outfile, fieldnames=spamdict)
    writer.writeheader()
    writer.writerow(spamdict)
with open("output/hamdict.csv", "w") as outfile:
    writer = csv.DictWriter(outfile, fieldnames=hamdict)
    writer.writeheader()
    writer.writerow(hamdict)
avgvaluespamsentence = analyslenofsentence(spamlist, spamdictlensentence)
avgvaluehamsentence = analyslenofsentence(hamlist, hamdictlensentence)
avgvaluespam = analyslenofword(spamdict, spamdictlenwords)
avgvalueham = analyslenofword(hamdict, hamdictlenwords)
spam_top_20 = top20(spamdict)
ham_top_20 = top20(hamdict)
spamdictlenwords_sorted = sortdict(spamdictlenwords)
hamdictlenwords_sorted = sortdict(hamdictlenwords)
spamdictlensentence_sorted = sortdict(spamdictlensentence)
hamdictlensentence_sorted = sortdict(hamdictlensentence)
# plt.bar(spamdictlenwords.keys(), spamdictlenwords.values(), color='g')
# plt.title("Средняя длина слова в спаме: %.2f " % avgvaluespam)
# plt.show()
# plt.bar(hamdictlenwords.keys(), hamdictlenwords.values(), color='g')
# plt.title("Средняя длина слова в хаме: %.2f " % avgvalueham)
# plt.show()
# plt.bar(spamdictlensentence.keys(), spamdictlensentence.values(), color='g')
# plt.title("Средняя длина предложения в спаме: %.2f " % avgvaluespamsentence)
# plt.show()
# plt.bar(hamdictlensentence.keys(), hamdictlensentence.values(), color='g')
# plt.title("Средняя длина предложения в хаме: %.2f " % avgvaluehamsentence)
# plt.show()
# plt.bar(spam_top_20.keys(), spam_top_20.values(), color='g')
# plt.show()
# plt.bar(ham_top_20.keys(), ham_top_20.values(), color='g')
# plt.show()
plt.plot(spamdictlenwords_sorted.keys(), spamdictlenwords_sorted.values(),label='spam',color='red')
plt.plot (hamdictlenwords_sorted.keys(),hamdictlenwords_sorted.values(),label='ham',color='blue')
plt.xlabel('Symbols in word', fontsize=15, color='green')
plt.ylabel('Amount', fontsize=15, color='green')
plt.legend()
plt.savefig('output/wordslen')
plt.show()
plt.plot(spamdictlensentence_sorted.keys(), spamdictlensentence_sorted.values(),label='spam',color='red')
plt.plot(hamdictlensentence_sorted.keys(), hamdictlensentence_sorted.values(),label='ham',color='blue')
plt.xlabel('Symbols in sentence', fontsize=15, color='green')
plt.ylabel('Amount', fontsize=15, color='green')
plt.legend()
plt.savefig('output/sentencelen')
plt.show()
plt.plot(spam_top_20.keys(), spam_top_20.values(),label='spam',color='red')
plt.xlabel('Top20 words', fontsize=15, color='green')
plt.ylabel('Amount', fontsize=15, color='green')
plt.legend()
plt.savefig('output/top20_spam')
plt.show()
plt.plot(ham_top_20.keys(), ham_top_20.values(),label='ham',color='blue')
plt.xlabel('Top20 words', fontsize=15, color='green')
plt.ylabel('Amount', fontsize=15, color='green')
plt.legend()
plt.savefig('output/top20_ham')
plt.show()
# for item in sorted(spamdictlenwords):
#  print("'%s':%s" % (item, spamdictlenwords[item]))
# print("-------------------------------------------------------")
# for item in sorted(hamdictlenwords):
#     print("'%s':%s" % (item, hamdictlenwords[item]))
# print("-------------------------------------------------------")
# for item in sorted(spamdictlensentence):
#     print("'%s':%s" % (item, spamdictlensentence[item]))
# print("-------------------------------------------------------")
# for item in sorted(hamdictlensentence):
#     print("'%s':%s" % (item, hamdictlensentence[item]))
# print("-------------------------------------------------------")
# for item in spam_top_20:
#     print("'%s':%s" % (item, spam_top_20[item]))
# print("-------------------------------------------------------")
# for item in ham_top_20:
#     print("'%s':%s" % (item, ham_top_20[item]))
