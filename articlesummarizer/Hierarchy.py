
# Splits given document into sentences and deals with externalities in the paragraph so it can be
# processed cleanly.
def sentSplit(para):
    sent_list = para.split('.')
    for str in sent_list:
        if (len(str) < 1):
            sent_list.remove(str)
        ind = (len(str) - 3)
        # Handles external periods, i.e. not for ending a sentence.
        if (('etc' == str[ind:]) or ('Mr' == str[ind + 1:]) or ('Mrs' == str[ind:]) or
            ('Ms' == str[ind + 1:])) and (sent_list.index(str) + 1 <= len(sent_list) - 1):
            str1 = str
            indplus = sent_list.index(str)
            str2 = sent_list[indplus + 1]
            sent_list.remove(str2)
            str3 = str1 + '.' + str2
            sent_list[indplus] = str3
    for str in sent_list:
        ind = (len(str) - 3)
        if (('etc' == str[ind:]) or ('Mr' == str[ind + 1:]) or ('Mrs' == str[ind:]) or
            ('Ms' == str[ind + 1:])) and (sent_list.index(str) + 1 <= len(sent_list) - 1):
            str1 = str
            indplus = sent_list.index(str)
            str2 = sent_list[indplus + 1]
            sent_list.remove(str2)
            str3 = str1 + '.' + str2
            sent_list[indplus] = str3
    for s in range(len(sent_list)):
        sent_list[s] = removeContractions(sent_list[s])
    return sent_list

def formParagraph(list):
    paras = ''
    for sent in list:
        paras += str(sent) + "."
    return paras

# Re-formats contractions with their expanded forms to get the true lengths of words and phrases.
def removeContractions(sentence):
    contraction_str = "aren't we'll can't couldn't didn't doesn't don't hadn't hasn't haven't I'll I'm I've " \
                      "isn't let's mightn't mustn't shan't she'll shouldn't that's there's they'll they're " \
                      "they've we're we've weren't what's what'll what're what've who'll who're who've " \
                      "won't wouldn't you'll you're you've"
    cont_list = contraction_str.split(' ')
    expansion_str = "are not,we will,cannot,could not,did not,does not,do not,had not,had not,have not," \
                    "I will,I am,I have,is not,let us,might not,must not,shall not,she will,should not,that is,there is" \
                    "they will,they are,they have,we are,we have,were not,what is,what will,what are,what have,who will," \
                    "who are,who have,will not,would not,you will,you are,you have"
    exp_list = expansion_str.split(',')
    str = sentence
    word_list = str.split(' ')
    x=0
    while x < len(word_list):
        if word_list[x] in cont_list:
            word_list[x] = exp_list[cont_list.index(word_list[x])]
        x+=1
    final_str = ''
    for n in range(len(word_list)):
        final_str+=word_list[n] + ' '

    return final_str
