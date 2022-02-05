from django.shortcuts import render
path = "/image"
#from templates import *

# Create your views here.


def letters_list(request):
    param = request.GET.get('letters')
    print(param)
    # get an instance of model which has an ImageField
    model_image = path + "/" + (param) + ".jpg"
    context = {'image': model_image}
    return render(request, 'some_html.html', context)
