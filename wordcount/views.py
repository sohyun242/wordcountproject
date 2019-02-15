from django.shortcuts import render


# Create your views here.
def hi(request):
    return render(request, 'hi.html')

def hi2(request):
    return render(request, 'hi2.html')

def hi3(request):
    return render(request, 'hi3.html')

def hi4(request):
    return render(request, 'hi4.html')

def hi6(request):
    return render(request, 'hi6.html')


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    text=request.GET['fulltext']
    words=text.split()
    word_dict = {}

    for word in words:
        if word in word_dict:
            word_dict[word]+=1
        else:
            word_dict[word]=1

    return render(request, 'result.html', {'fulltext' : text, 'total' : len(words), 'dictionary' : word_dict.items()})

