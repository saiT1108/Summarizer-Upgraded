
import numpy as np
from . import Sentences

# Constructor to hold all details of paragraph.
# Runtime: O(N^2)
class Paragraph:
    def __init__(self, para, num, sentence_lst, orig_count):
        self.para = para
        self.para_index = num
        self.orig_words = orig_count
        self.summ_words = 0
        self.rep_avg = 0

        # Array to hold sentence objects which will be processed for every paragraph.
        self.sentence_objs = []

        # Array to hold repetition values for each paragraph.
        self.rep_arr = []

        self.sent_list = sentence_lst
        self.lowest_para_index = 0
        self.highest_para_index = 1000

        # If sentence object at the end of the list is longer than a given length, accept it,
        # else, take the second last sentence as the last sentence instead.
        if len(self.sent_list[len(self.sent_list)-1]) > 3:
            self.last_sentence = self.sent_list[len(self.sent_list) - 1]
            self.last_index = len(self.sent_list) - 1
        else:
            self.last_sentence = self.sent_list[len(self.sent_list) - 2]
            self.last_index = len(self.sent_list) - 2

        self.first_sentence = self.sent_list[0]

        # Call main sentence sorting method.
        self.sentenceSplitter()

        # --
        # self.re_arr = []
        # for s in self.sentence_objs:
        #     self.re_arr.append(s.repetitionFinder())
        # --
        # print(self.re_arr)
        self.len_arr = []
        for sentence in self.sent_list:
            self.len_arr.append(len(sentence))
        # --

    # Runtime: O(1)
    def setPara(self, para):
        self.para = para
        self.sentenceSplitter()

    # Returns the paragraph as string.
    def getPara(self):
        return str(self.para)

    def getOriginalWordCount(self):
        return self.orig_words

    # Next 4 methods used only in constructor.
    # Runtime: O(1)
    def setLowestParaIndex(self, num):
        self.lowest_para_index = num

    def setHighestParaIndex(self, num):
        self.highest_para_index = num

    def getHighestParaIndex(self):
        return self.highest_para_index

    def getLowestParaIndex(self):
        return self.lowest_para_index

    # Return the index of the paragraph within the document, as passed to constructor.
    # Runtime: O(1)
    def getParaIndex(self):
        return self.para_index

    # Splits sentences into usable and unusable to determine what makes it into the final summary.
    # Runtime: O(N^2) - dependent on setSentencePriority
    def sentenceSplitter(self):
        if len(self.sent_list) > 2:
            self.removeBelowQ1()

        # Set limit for the maximum sentences the summarized paragraph can have, roughly 1/4th of the original.
        self.para_sum_limit = self.getSentenceCount() * .25

        # Creates Sentence objects after removing the smaller ones.
        self.assignSentences(self.sent_list)

        # Uses hierarchy to set the priority of sentences in terms of linguistic value.
        self.setSentencePriority()

    # Returns a list of sentence strings.
    # Runtime: O(1)
    def getParaSentences(self):
        return self.sent_list

    # Returns a string of the sentence at the requested index.
    # Runtime: O(1)
    def getSentencePara(self, index):
        return self.sentence_objs[index].getSentence()

    # Returns how many sentences are in the paragraph object, used for processing.
    # Runtime: O(1)
    def getSentenceCount(self):
        self.sent_count = len(self.sent_list)
        return self.sent_count

    # Finds the average length of sentences in the paragraph.
    # Runtime: O(N)
    def findAverage(self):
        self.sum = 0
        for n in range(len(self.sent_list)):
            self.sum+=len(self.sent_list[n])
        self.average = self.sum/(len(self.sent_list))
        return self.average

    # Runtime: O(N)
    def removeBelowQ1(self):
        lengths = []

        # Adds the lengths of each sentence into an array for comparison.
        for str in self.sent_list:
            lengths.append(len(str))

        # Reviews the length statistic for each sentence in paragraph (numpy) compared to the rest of the paragraph.
        for str in self.sent_list:
            q3 = np.percentile(lengths, 25)

            # If sentence length is less than certain amount of characters or if its not in the 4th quartile
            # of the paragraphs other sentences, then remove it.
            if len(str) < q3 and len(str) < 50:
                self.sent_list.remove(str)

    # Runtime: O(1)
    def getParaSumLimit(self):
        return round(self.para_sum_limit)

    # Creates sentence objects with comparable attributes.
    # Runtime: O(N)
    def assignSentences(self, list):
        n = 0
        ind = self.getParaIndex()
        while n < len(list):
            sent = Sentences.Sentences(list[n], ind, n)
            self.sentence_objs.append(sent)
            n += 1

    # Uses repetitionFinder to take the average repetition for every sentence in paragraph.
    # Runtime: O(N)
    def sentenceRepAverage(self):
        rep_total = 0
        for s in self.sentence_objs:
            rep_total += s.repetitionFinder()
        self.rep_avg = rep_total/len(self.sentence_objs)

    # Finds median repetition for processing.
    # Runtime: O(N)
    def sentenceRepMedian(self):
        re_arr = []
        for s in self.sentence_objs:
            re_arr.append(s.repetitionFinder())
        rep_median = np.percentile(re_arr, 50)
        return rep_median

    # Finds upper quarter of sentence repetition.
    # Runtime: O(N)
    def sentenceRepQ3(self):
        re_arr = []
        for s in self.sentence_objs:
            re_arr.append(s.repetitionFinder())
        q3 = np.percentile(re_arr, 75)
        return q3

    # Finds lower quarter of sentence repetition.
    # Runtime: O(N)
    def sentenceRepQ1(self):
        re_arr = []
        for s in self.sentence_objs:
            re_arr.append(s.repetitionFinder())
        q1 = np.percentile(re_arr, 25)
        return q1

    # Finds standard deviation of sentence repetition to compare.
    # Runtime: O(N)
    def sentenceSTD(self):
        re_arr = []
        for s in self.sentence_objs:
            re_arr.append(s.repetitionFinder())
        rep_median = np.std(re_arr)
        return rep_median

    # Reorganizes sentences based on length.
    # Runtime: O(N*x)
    def longestSentenceList(self):
        temp_list = self.sent_list
        max_list = []
        x=0
        while x < self.getParaSumLimit():
            max_sent = ''
            for n in range(len(temp_list)):
                if len(temp_list[n])>len(max_sent):
                    max_sent = temp_list[n]
            max_list.append(max_sent)
            temp_list.remove(max_sent)
            x+=1
        return max_list[0]

    # Returns the single largest sentence object in the paragraph.
    # Runtime: O(N)
    def longestSentenceObj(self):
        max_sent = ''
        max_ind = 0

        for n in range(len(self.sentence_objs)):
            if len(self.sentence_objs[n].getSentence()) > len(max_sent):
                max_ind = n
                max_sent = self.sentence_objs[n].getSentence()
        return self.sentence_objs[max_ind]

    # Find quartiles of sentence lengths, called on by other methods.
    # Runtime: O(N)
    def lengthQ1(self):
        len_arr = []
        for sentence in self.sent_list:
           len_arr.append(len(sentence))
        q1 = np.percentile(len_arr, 25)
        return q1

    def lengthQ2(self):
        len_arr = []
        for sentence in self.sent_list:
           len_arr.append(len(sentence))
        q2 = np.percentile(len_arr, 50)
        return q2

    def lengthQ3(self):
        len_arr = []
        for sentence in self.sent_list:
           len_arr.append(len(sentence))
        q3 = np.percentile(len_arr, 75)
        return q3

    def lengthSTD(self):
        len_arr = []
        for sentence in self.sent_list:
           len_arr.append(len(sentence))
        stdv = np.std(len_arr)
        return stdv

    # Uses Hierarchy class and all other comparable attributed to assign a priority number to each
    # sentence object, resulting in a list ordered based on the priority each sentence is given.
    # Runtime: O(N^2) - dependent on longestSentenceObject
    def setSentencePriority(self):
        rq1 = self.sentenceRepQ1()
        rq2 = self.sentenceRepMedian()
        rq3 = self.sentenceRepQ3()
        lstd = self.lengthSTD()
        q1 = self.lengthQ1()
        q2 = self.lengthQ2()
        q3 = self.lengthQ3()
        if self.getSentenceCount() <= 2:
            self.sentence_objs[0].setPriority(0)
            self.sentence_objs[1].setPriority(1)

        elif self.getSentenceCount() <= 4:
            self.longestSentenceObj().setPriority(0)
            for n in range(self.getSentenceCount()):
                if len(self.sentence_objs[n].getSentence()) >= (q3-lstd) and self.sentence_objs[n] !=  self.longestSentenceObj():
                    self.sentence_objs[n].setPriority(1)
                elif len(self.sentence_objs[n].getSentence()) >= q2:
                    self.sentence_objs[n].setPriority(2)
                else:
                    self.sentence_objs[n].setPriority(3)
        else:
            for n in range(self.getSentenceCount()):

                if self.sentence_objs[n] == self.longestSentenceObj():
                    self.sentence_objs[n].setPriority(0)
                elif len(self.sentence_objs[n].getSentence()) >= q3 and self.sentence_objs[n] != self.longestSentenceObj():
                    self.sentence_objs[n].setPriority(1)
                elif len(self.sentence_objs[n].getSentence()) >= q2 and self.sentence_objs[n].repetitionFinder() <= rq1:
                    self.sentence_objs[n].setPriority(2)
                elif len(self.sentence_objs[n].getSentence()) >= q2 and self.sentence_objs[n].repetitionFinder() <= rq2:
                    self.sentence_objs[n].setPriority(3)
                elif len(self.sentence_objs[n].getSentence()) >= q2 and self.sentence_objs[n].repetitionFinder() <= rq3:
                    self.sentence_objs[n].setPriority(4)
                elif len(self.sentence_objs[n].getSentence()) >= q1 and self.sentence_objs[n].repetitionFinder() <= rq2:
                    self.sentence_objs[n].setPriority(5)
                elif self.sentence_objs[n] != self.longestSentenceObj():
                    self.sentence_objs[n].setPriority(6)

    # Returns a list of sentence indices in priority order.
    # Runtime: O(N)
    def getPriorityHierarchy(self):
        PL = []
        for n in range(len(self.sentence_objs)):
            PL.append(self.sentence_objs[n].getPriority())
        return PL

    # Sorts the hierarchy list in terms of priority, regardless of sentence order.
    # Runtime: O(N^2)
    def hierarchySort(self):
        if len(self.sentence_objs) > 2:
            PLindex = self.sentence_objs
            if self.first_sentence == PLindex[0].getSentence():
                PLindex.remove(PLindex[0])
            PLindex.remove(self.sentence_objs[len(self.sentence_objs)-1])

            for n in range(len(PLindex)):
                for m in range(len(PLindex)):
                    if self.sentence_objs[n].getPriority() < self.sentence_objs[m].getPriority():
                        temp = PLindex[n]
                        PLindex[n] = PLindex[m]
                        PLindex[m] = temp
            final_PL = PLindex[0:self.getParaSumLimit()]
            return final_PL
        else:
            final_PL = []
            for n in range(2):
                final_PL.append(self.sentence_objs[n])
            return final_PL

    # Rearranges the sentence objects to match the original order instead of priority order.
    # Runtime: O(N^2)
    def indexSort(self):
        ini_list = self.hierarchySort()
        if len(self.sentence_objs) > 2:
            for n in range(len(ini_list)):
                for m in range(len(ini_list)):
                    if ini_list[n].getSentenceIndex() < ini_list[m].getSentenceIndex():
                        temp = ini_list[n]
                        ini_list[n] = ini_list[m]
                        ini_list[m] = temp
        return ini_list

    # Uses all previous attributes of sentence and paragraph objects to form the final, shorter summary.
    # Runtime: O(N)
    def formFinalParagraph(self):
        self.sentenceRepAverage()
        if len(self.sentence_objs) <= 2:
            return self.para
        else:
            list = self.indexSort()
            final_para = '\t'
            final_para += self.first_sentence.strip() + '. '
            for sent in list:
                self.summ_words += sent.getWordCount()
                final_para += sent.getSentence().strip() + '. '
            if (self.getParaIndex() == self.getLowestParaIndex()  or self.getParaIndex() == self.getHighestParaIndex()) and \
                    (self.last_sentence not in final_para):
                final_para += self.last_sentence.strip() + '.'
            return final_para

    def __repr__(self):
        return self.para + '\n'