from django.shortcuts import render
from django.http import HttpResponse
import operator

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


def count(request):
    data = request.GET['ourtext']

    data_list = data.split()
    worddict = {}

    for word in data_list:
        if word in worddict:
            worddict[word] += 1
        else:
            worddict[word] = 1

    new_list = sorted(worddict.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'data': data, 'count': len(data_list),'new_list':new_list})
