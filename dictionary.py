import json
import nltk
import operator
import difflib
data=json.load(open("data.json"))
#print type(data)
new_dic={}
def trans(word):
    if word.lower() in data:
        print data[word.lower()][0]
    else:
        for key in data.keys():
            new_dic[key]=nltk.edit_distance(word, key)
        print difflib.get_close_matches(word,data.keys())[0]  # using difflib function only 1 line :)
        sorted_new = sorted(new_dic.items(), key=operator.itemgetter(1))
        #print type(sorted_new)
        print "{} not found , you mean : {} ?  y/n".format(word,sorted_new[0][0])
        choice=raw_input()
        if choice=='y':
            trans(sorted_new[0][0])
        else :
            print "word not exsist"
print "enter the word"
word=raw_input()

trans(word)