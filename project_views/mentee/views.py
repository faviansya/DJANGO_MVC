from django.shortcuts import render

# Create your views here.


def mentee(request):
    urls = {
        'halamanhome': '/',
        'halamanblog': '/blog',
        'halamanmentor': '/mentor',
        'halamanmentee': '/mentee',
        'halamanauthor': '/author',
    }
    return render(request, 'mentee/index.html', urls)
