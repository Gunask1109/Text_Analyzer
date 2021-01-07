from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):

    #get the text
    djtext = request.POST.get('text', 'default')
    #check checkbox value
    removepunc= request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    if removepunc == "on":
        punctuations ='''!()-[];:'"\,<>./?@#$%^&*'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed+=char
        params= {'purpose':'Removed Punctuations','analyzed_text':analyzed}
        djtext=analyzed

    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed += char.upper()
        params = {'purpose': 'Changed to UpperCase', 'analyzed_text': analyzed}
        djtext = analyzed

    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed += char
        params = {'purpose': 'Changed to newlineremove', 'analyzed_text': analyzed}
        djtext = analyzed
        
        
    if extraspaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if djtext[index] == " " and djtext[index+1] == "":
                pass
            else:
                analyzed = analyzed+char
        params = {'purpose': 'Changed to Extraspace Remove', 'analyzed_text': analyzed}
        djtext = analyzed

    if charcount == "on":
        analyzed = 0
        for char in djtext:
            analyzed+=1
        params = {'purpose': 'Changed to Charcount', 'analyzed_text': analyzed}
        djtext = analyzed


    return render(request,'analyze.html',params)

