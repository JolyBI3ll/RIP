"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from rest_framework import routers
from api.views.ParticipantsViews import *

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path(r'participants/', get_Participants, name='participants-get'),
    path(r'participants/post/', post_Participants, name='participants-post'),
    path(r'participants/<int:key>/', get_Participants_detail, name='participants-detail'),
    path(r'participants/<int:key>/put/', put_Participants_detail, name='participants-put'),
    path('admin/', admin.site.urls),
]