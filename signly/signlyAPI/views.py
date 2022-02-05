from django.shortcuts import render
path = "/image"
#from templates import *

# Create your views here.
def letters_list(request):
    param = request.GET.get('letters')
    print(param)
    model_image = path+"/"+(param)+".jpg" #get an instance of model which has an ImageField
    context = {'image' : model_image }
    html = render(request , 'some_html.html' , context)



