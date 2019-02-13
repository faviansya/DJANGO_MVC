from django.shortcuts import render

# Create your views here.


def mentor(request):
    urls = {
        'halamanhome': '/',
        'halamanblog': '/blog',
        'halamanmentor': '/mentor',
        'halamanmentee': '/mentee',
        'halamanauthor': '/author',
    }
    return render(request, 'mentor/index.html', urls)
