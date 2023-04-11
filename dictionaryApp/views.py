from nltk.corpus import wordnet
from django.shortcuts import render
from PyDictionary import PyDictionary
import nltk
# nltk.download("wordnet")
# Create your views here.
from nltk.corpus import wordnet


def homeView(request):
    return render(request, 'dictionaryApp/index.html')


def searchView(request):
    word = request.GET.get('search')

    # dictionary = PyDictionary()

    # meanings = dictionary.meaning(word)
    # synonyms = dictionary.synonym(word)
    # antonyms = dictionary.antonym(word)
    # context = {
    #     'word': word,
    #     'meanings': meanings,
    #     'synonyms': synonyms,
    #     'antonyms': antonyms
    # }

    wn = wordnet.synsets(word)

    meanings = {}
    for syn in wn:
        pos = syn.pos()
        definition = syn.definition()
        if pos not in meanings:
            meanings[pos] = [
                {'lemma_names': syn.lemma_names(), 'definition': definition, 'examples': syn.examples()}]
        else:
            meanings[pos].append(
                {'lemma_names': syn.lemma_names(), 'definition': definition, 'examples': syn.examples()})

    synonyms = []
    antonyms = []
    for syn in wn:
        for lemma in syn.lemmas():
            if lemma.name() != word:
                synonyms.append(lemma.name())
                if lemma.antonyms():
                    antonyms.append(lemma.antonyms()[0].name())

    context = {
        'word': word,
        'meanings': meanings,
        'synonyms': synonyms,
        'antonyms': antonyms
    }

    return render(request, 'dictionaryApp/search.html', context)
