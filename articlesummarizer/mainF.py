from . import Paragraph
from . import Hierarchy

# Create the arrays that hold paragraphs and their respective sentences as global variables.
para_holder = []
para_sentence_holder = []
edited_para_list = []
para_list = []
orig = 0
sumCount = 0
rep = 0
reduc = 0
summary = ''

# Split input document into separate paragraphs and sentences.
def document_splitter(doc):
    global para_holder
    global para_sentence_holder
    global edited_para_list
    global para_list

    edited_para_list = []
    para_list = []
    para_holder = []
    para_sentence_holder = []
    words = doc.split(' ')
    orig_words = len(words)

    # Checks if document uses double new line to separate paragraphs or indents, then splits the paragraphs.
    if '\n\n' in doc:
        para_list = doc.split('\n\n')
    else:
        para_list = doc.split('\t')

    for n in range(len(para_list)):
        # Sends each paragraph to method sentSplit (read more in hierarchy class) to sort through syntax.
        para_temp = Hierarchy.sentSplit(para_list[n])

        # Adds modified paragraph to edited list by reference.
        edited_para_list.append(para_temp)

    n = 0
    x = 0

    while n < len(para_list):
        if len(edited_para_list[n]) > 1:
            # Passes nth paragraph, n (for ID purposes), and the edited paragraph to Paragraph class constructor
            # in order to build paragraph object.
            para = Paragraph.Paragraph(para_list[n], n, edited_para_list[n], orig_words)

            # Holds Paragraph objects to be modified later.
            para_holder.append(para)

            # If paragraph is less than 5 sentences long, it's summary will be less accurate.
            if para_holder[x].getSentenceCount() < 5:
                print('The length of paragraph {} is less than 5 sentences, so its summary will be less '
                      'accurate\n'.format(x + 1))
            x += 1
        n += 1

    # Paragraph ID details to be used by the Hierarchy class.
    lowest_para_index = para_holder[0].getParaIndex()
    highest_para_index = para_holder[len(para_holder) - 1].getParaIndex()

    # Sets every Paragraph object to know how many paragraphs there are in the document.
    para_holder[0].setLowestParaIndex(lowest_para_index)
    para_holder[len(para_holder) - 1].setHighestParaIndex(highest_para_index)

    global orig
    orig = orig_words

# Creates a summary of every paragraph before returning them as a final String.

def clearStats():
    global rep
    global orig
    global reduc
    global sumCount
    global summary
    rep = 0
    orig = 0
    reduc = 0
    summary = ''

def formSummary():
    global rep
    global orig
    global reduc
    global sumCount
    global summary
    sum_rep = 0
    print("prev summary =" + summary + "\n\nend\n")
    summary = ''
    for para in para_holder:
        summary += para.formFinalParagraph() + '\n'
        sum_rep += para.rep_avg

    sumCount = len(summary.split(' '))

    reduc = 100 - 100*(sumCount/orig)

    rep = sum_rep/(len(para_holder))

    print(summary)
    return summary

# GETTER METHODS
# ------------------------------------------------------------
# Returns integer
def getOrigCount():
    return orig

# Returns integer
def getSumCount():
    return sumCount

# Returns string
def getRep():
    return (str(round(rep/3, 1)) + "/10")

# Returns string
def getReduction():
    return (str(round(reduc, 1)) + "%")

def runSummarizer(userInput):
    clearStats()
    document_splitter(userInput)
    return formSummary()
