from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    #print(fulltext)
    wordList = fulltext.split()
    wordCount = len(wordList)
    wordDictionary = {}
    for word in wordList:
        if word in wordDictionary:
            wordDictionary[word] += 1
        else:
            wordDictionary[word] = 1
    sortedWordDict = {}
    for word in sorted(wordDictionary):
        sortedWordDict[word] = wordDictionary[word]

    return render(request, 'count.html', {'fulltext': fulltext, 'wordcount':wordCount,  'worddictionary':sortedWordDict})

def about(request):
    return render(request, 'about.html')
