from functools import reduce
from operator import truediv
import os
from django.http import HttpResponse
from django.shortcuts import render
import urllib
from signly.settings import BASE_DIR
import requests
from django.http import HttpResponseRedirect
from django import forms
path = "/image"

# Create your views here.


def letters_list(request):
    letter = request.GET.get('letters')
    context = {}
    file_path = os.path.join(
        BASE_DIR, 'images', os.path.basename(letter) + '.jpg')
    try:
        with open(file_path, 'rb') as fingerspell_image:
            return HttpResponse(fingerspell_image.read(), content_type='image/jpeg')
    except Exception as e:
        print(e)
        context = {'message': 'Letter not found ' + file_path}
    return render(request, 'message.html', context)


def get_video_link(request):
    text = request.GET.get('word')
    if (url := check_all_links(text)):
        return HttpResponse(url)
    else:
        response = HttpResponse()
        response.status_code = 404
        return response


def check_all_links(text):
    if (url := check_phrase_link(text)):
        return url

    # Check word
    if (url := check_signbank(text.upper())):
        return url

    return False


def check_signbank(word):
    url_parts = [
        'https://bslsignbank.ucl.ac.uk/media/bsl-video/', word[0:2] + '/', word + '.mp4']
    url = reduce(urllib.parse.urljoin, url_parts)
    req = requests.get(url)
    if (req.status_code == 200):
        return url
    else:
        return False


def check_phrase_link(phrase):
    if url := check_hardcoded(phrase):
        return url
    url_parts = [
        'https://media.signbsl.com/videos/bsl/signstation/', phrase.lower().replace(' ', '-') + '.mp4']
    url = reduce(urllib.parse.urljoin, url_parts)
    req = requests.get(url)
    if (req.status_code == 200 or req.status_code == 304):
        return url

    url_parts = [
        'https://media.signbsl.com/videos/bsl/deafway/mp4/', phrase.lower() + '.mp4']
    url = reduce(urllib.parse.urljoin, url_parts)
    req = requests.get(url)
    if (req.status_code == 200 or req.status_code == 304):
        return url

    if (phrase.lower() == 'how are you'):
        return 'https://media.signbsl.com/videos/bsl/signstation/101-06-76.mp4'

    return False


def check_hardcoded(phrase):
    if(phrase.lower() == 'how are you'):
        return 'https://media.signbsl.com/videos/bsl/signstation/101-06-76.mp4'
    return False


class NameForm(forms.Form):
    letters = forms.CharField(label='Your Letter', max_length=1)


def home_page(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()
    return render(request, 'home.html', {'form': form})


def learn(request):
    content = ['hello', 'how are you', 'good afternoon']
    urls = []
    for phrase in content:
        if url := check_all_links(phrase):
            urls.append({'url': url, 'phrase': phrase})
    context = {
        'urls': urls
    }
    return render(request, 'learn.html', context)

def quiz(request):
    return render(request, 'quiz.html')

def click(request):
    a = request.GET.get('a')
    b = request.GET.get('b')
    c = request.GET.get('c')
    d = request.GET.get('d')
    score=0
    if a=="boat":
        score+=1
    if b=="good-afternoon":
        score+=1
    if c=="howareyou":
        score+=1
    if d=="hello":
        score+=1
    print(score)
    return HttpResponse(score)
