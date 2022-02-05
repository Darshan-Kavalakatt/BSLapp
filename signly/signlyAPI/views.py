from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Letter
from .serializers import *

# Create your views here.


@api_view(['GET', 'POST'])
def letters_list(request):
    if request.method == 'GET':
        alpha = request.data.get("letter")
        data = Letter.objects.filter(letter=alpha)

        serializer = LetterSerializer(
            data, context={'request': request}, many=True)

        return Response(serializer.data)
