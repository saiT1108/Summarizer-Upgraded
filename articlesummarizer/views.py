from django.shortcuts import render
from django.http import HttpResponse
from . import mainF


# Create your views here.

def index(request):
    context = {
        "title":'Article Summarizer',
        "summary": ' ',
        "origtext": 'Copy Article Here',
    }
    return render(request, 'index.html', context)

def summarize(request):
    if request.method == "POST":
        try:
            userinput = origtext = request.POST.get('input')
            userinput = mainF.runSummarizer(userinput) #Document Splitter Method
            originalwc = mainF.getOrigCount()
            sumcount = mainF.getSumCount()
            repetition = mainF.getRep()
            reduction = mainF.getReduction()
        except IndexError:
            userinput = origtext = request.POST.get('input')
            userinput = 'Text is too short to be summarized. Please try again :(' #Document Splitter Method
            originalwc = 0
            sumcount = 0
            repetition = 0
            reduction = 0
        context = {
        "origtext": origtext,
        "summary": userinput,
        "originalwc": originalwc,
        "sumcount": sumcount,
        "repetition": repetition,
        "reduction": reduction,
        "title": 'Article Summarizer',
        }
    return render(request, 'index.html', context)

    #shape input and output boxes
    #stats on top
    #center output

def about(request):
    context = {
        "title":'About The Creators'
    }
    return render(request, 'about.html', context)
