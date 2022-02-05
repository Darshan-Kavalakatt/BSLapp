import os
from django.http import HttpResponse
from django.shortcuts import render
from signly.settings import BASE_DIR
from django.http import HttpResponseRedirect
from django import forms
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