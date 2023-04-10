from django.shortcuts import render
from PyDictionary import PyDictionary

# Create your views here.


def homeView(request):
    return render(request, 'dictionaryApp/index.html')


def searchView(request):
    word = request.GET.get('search')
    dictionary = PyDictionary()

    meanings = dictionary.meaning(word)
    synonyms = dictionary.synonym(word)
    antonyms = dictionary.antonym(word)

    context = {
        'word': word,
        'meanings': meanings,
        'synonyms': synonyms,
        'antonyms': antonyms
    }

    return render(request, 'dictionaryApp/search.html', context)
