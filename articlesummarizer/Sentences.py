class Sentences():
    # Constructor.
    def __init__(self, sentn, para_index, sent_ind):
        self.sentence = sentn
        self.word_list = self.sentence.split(' ')
        self.word_count = len(self.word_list)
        self.origin_index = para_index
        self.sentence_index = sent_ind
        self.priority_num = 0

    # Sets and gets the priority of given sentence.
    def setPriority(self, num):
        self.priority_num = num

    def getPriority(self):
        return self.priority_num

    # Returns what paragraph this sentence object belongs to.
    def getParagraphOriginIndex(self):
        return self.origin_index

    # Return the index of sentence within it's parent paragraph.
    def getSentenceIndex(self):
        return self.sentence_index

    # Return sentence.
    def getSentence(self):
        return self.sentence

    # Splits sentence into separate words for processing by the parent class.
    # Runtime: O(N)
    def word_splitter(self):
        for word in self.word_list:
            ind = self.word_list.index(word)
            if ',' in word:
                newword = word[:word.index(',')]
                self.word_list[ind] = newword
            elif '/' in word:
                neword = word[:word.index('/')]
                self.word_list[ind] = neword

    # Returns a list of words in sentence.
    def getWordList(self):
        return self.word_list

    def getWordCount(self):
        return self.word_count

    def getSentenceLength(self):
        return len(self.sentence)

    # Finds how many times words repeat in the sentence, for word like "the", "and", "of", etc. that
    # increase repetition but do not enrich the sentence.
    # Runtime: O(N)
    def repetitionFinder(self):
        self.rep = 0
        for word in self.word_list:
            ind = self.word_list.index(word)
            if word in self.word_list[ind+1:]:
                self.rep += 1
        return self.rep

    def __repr__(self):
        return self.sentence