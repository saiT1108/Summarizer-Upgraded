# Article Summarizer 2.0
### Created by Sai Tippana(saiT1108)
#### Credit to Abhi Singh for Django integration

# About the software

Welcome to the article summarizer github. This is an open-source software that runs on an AI model that I made to help users cut down substantially on reading times on most pieces of literature. 

In many of my classes at college, I had to read a lot of articles and know their key points to then write about and discuss in class, but the articles were much too long for me to manage with all my other classwork. So I made this program to summarize it for me, and this helped me get through my classes much faster. This program will summarize just about anything with few exceptions, it works best with english articles but can produce some viable results for other latin-based languages (like French, Spanish, etc.) but be advised that I do not reccomend using it for non-english articles despite it working.

# How it works

The model checks each word of the input data and compares them with a locally-generated criteria in order to create a hierarchy of the most important sentences, and sorts through them with more hierarchal processing to produce a concise, accurate summary.

The code has been cleaned and commented for anyone interested in learning what each method and class does. It took a while to design, implement, and debug this code considering it's test data is essays with thousands of words, so if you use my code please remember to credit me.

This program works best with English articles that are well formatted into large paragraphs (prefereably at least 5 sentences each paragraph). Thesis and conclusion sentences are always kept intact unless they are very short and offer little value to the rest of the paragraph.

### Please note: This software cannot be used with scientific articles, as it will clear out a lot of data. This is a natural language processing program, not very well suited for numerical or other data.

The program is available here: https://guarded-forest-19610.herokuapp.com/articlesummarizer/
