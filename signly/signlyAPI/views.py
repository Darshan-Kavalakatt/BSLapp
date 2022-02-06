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
# from templates import *

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
    # Check long phrase
    if (url := check_signstation(text)):
        return HttpResponse(url)

    # Check word
    if (url := check_signbank(text.upper())):
        return HttpResponse(url)
    else:
        response = HttpResponse()
        response.status_code = 404
        return response


def check_signbank(word):
    url_parts = [
        'https://bslsignbank.ucl.ac.uk/media/bsl-video/', word[0:2] + '/', word + '.mp4']
    url = reduce(urllib.parse.urljoin, url_parts)
    req = requests.get(url)
    if (req.status_code == 200):
        return url
    else:
        return False


def check_signstation(phrase):
    url_parts = [
        'https://media.signbsl.com/videos/bsl/signstation/', phrase.lower().replace(' ', '-') + '.mp4']
    url = reduce(urllib.parse.urljoin, url_parts)
    req = requests.get(url)
    if (req.status_code == 200 or req.status_code == 304):
        return url
    else:
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
    context = {
        'content': ['hello', 'how are you', 'good afternoon']
    }
    return render(request, 'learn.html')
