"""signly URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from signlyAPI import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page),
    re_path(r'^api/letters/$', views.letters_list),
    path('api/videolink', views.get_video_link),
    path('learn', views.learn),
    path('quiz', views.quiz),
    path('submitclick',views.click)
    #re_path(r'^api/students/([0-9])$', views.students_detail),
]
