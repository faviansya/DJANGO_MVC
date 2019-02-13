from django.shortcuts import render

# Create your views here.


def blog(request):
    urls = {
        'halamanhome': '/',
        'halamanblog': '/blog',
        'halamanmentor': '/mentor',
        'halamanmentee': '/mentee',
        'halamanauthor': '/author',
    }
    return render(request, 'blog/index.html', urls)
