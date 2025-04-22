from django.http import HttpResponse
from django.shortcuts import render, redirect,reverse,get_object_or_404
from .models import Url
from .forms import UrlForm
from .utils import encode_url,decode_url


# Create your views here.


def encode(request):
    return redirect('home')

def getdata(request,long_url):
    addurl=Url(longurl=long_url)
    addurl.save()
    return HttpResponse('Datan')

def home(request):
    if request.method=='POST':
        form=UrlForm(request.POST)
        if form.is_valid():
            long_url = str(form.cleaned_data['longurl'])
            encoded_url=encode_url(long_url)
            form.save()
            return redirect(reverse(aftershort,kwargs={'lurl':encoded_url}))

    else:
        form=UrlForm()

    return render(request,'encoder/home.html')

def about(request):
    return render(request,'encoder/about.html')

def direct(request,short):
    if Url.objects.filter(shorturl=short).exists():
        sendingurl=get_object_or_404(Url,shorturl=short)
        sendingurl=sendingurl.longurl
        if "http" not in sendingurl:
            sendingurl="https://"+sendingurl

        return redirect(sendingurl)

    else:
        return render(request,'encoder/urlnotexist.html')


def aftershort(request,lurl):
    shorturl=Url.objects.filter(longurl=decode_url(lurl)).values()
    shorturl=str(shorturl[0]['shorturl'])
    shorturl="urlshortenerdeep.up.railway.app/"+shorturl
    return render(request,'encoder/aftershort.html',{'surl':shorturl})