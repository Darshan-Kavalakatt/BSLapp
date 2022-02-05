from functools import reduce
import os
from django.http import HttpResponse
from django.shortcuts import render
import urllib
from signly.settings import BASE_DIR
import requests
path = "/image"
#from templates import *

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
    word = request.GET.get('word').upper()
    url_parts = [
        'https://bslsignbank.ucl.ac.uk/media/bsl-video/', word[0:2] + '/', word + '.mp4']
    url = reduce(urllib.parse.urljoin, url_parts)
    req = requests.get(url)
    if (req.status_code == 200):
        return HttpResponse(url)
    else:
        response = HttpResponse()
        response.status_code = 404
        return response
